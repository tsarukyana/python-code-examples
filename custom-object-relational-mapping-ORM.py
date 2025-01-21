"""
Optimized ORM implementation using Python metaclasses and descriptors.
"""

from typing import Dict, Any, Type, TypeVar, List, Optional, Union
import sqlite3
from datetime import datetime

T = TypeVar('T', bound='Model')


class Field:
    def __init__(self, field_type: str, required: bool = True, default: Any = None):
        self.field_type = field_type
        self.required = required
        self.default = default
        self.name = None

    def __set_name__(self, owner: Type['Model'], name: str):
        self.name = name

    def __get__(self, instance: 'Model', owner: Type['Model']) -> Any:
        if instance is None:
            return self
        return instance._data.get(self.name, self.default)

    def __set__(self, instance: 'Model', value: Any):
        if self.required and value is None:
            raise ValueError(f"{self.name} is required")
        instance._data[self.name] = value


class TextField(Field):
    def __init__(self, required: bool = True, default: str = None):
        super().__init__('TEXT', required, default)


class IntegerField(Field):
    def __init__(self, required: bool = True, default: int = None):
        super().__init__('INTEGER', required, default)


class FloatField(Field):
    def __init__(self, required: bool = True, default: float = None):
        super().__init__('REAL', required, default)


class DateTimeField(Field):
    def __init__(self, required: bool = True, default: datetime = None):
        super().__init__('TIMESTAMP', required, default)

    def __set__(self, instance: 'Model', value: Union[datetime, str]):
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        super().__set__(instance, value)


class ModelMeta(type):
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> 'Model':
        if name == 'Model':
            return super().__new__(mcs, name, bases, attrs)

        fields = {key: value for key, value in attrs.items() if isinstance(value, Field)}
        attrs['_fields'] = fields
        attrs['_table_name'] = name.lower()

        return super().__new__(mcs, name, bases, attrs)


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs: Any):
        self._data: Dict[str, Any] = {}
        self._id: Optional[int] = kwargs.get('id')

        for name, field in self._fields.items():
            value = kwargs.get(name, field.default)
            setattr(self, name, value)

    @classmethod
    def create_table(cls, conn: sqlite3.Connection):
        """Create the database table for this model."""
        fields = [f"id INTEGER PRIMARY KEY AUTOINCREMENT"] + \
                 [f"{name} {field.field_type}" for name, field in cls._fields.items()]
        query = f"CREATE TABLE IF NOT EXISTS {cls._table_name} ({', '.join(fields)})"
        conn.execute(query)
        conn.commit()

    def save(self, conn: sqlite3.Connection) -> int:
        """Save the model instance to the database."""
        fields = list(self._data.keys())
        values = [self._data[field] for field in fields]

        if self._id is None:
            placeholders = ', '.join(['?' for _ in fields])
            query = f"INSERT INTO {self._table_name} ({', '.join(fields)}) VALUES ({placeholders})"
            cursor = conn.execute(query, values)
            self._id = cursor.lastrowid
        else:
            set_clause = ', '.join([f"{field}=?" for field in fields])
            values.append(self._id)
            query = f"UPDATE {self._table_name} SET {set_clause} WHERE id=?"
            conn.execute(query, values)

        conn.commit()
        return self._id

    @classmethod
    def get(cls: Type[T], conn: sqlite3.Connection, id: int) -> Optional[T]:
        """Retrieve a model instance by ID."""
        query = f"SELECT * FROM {cls._table_name} WHERE id=?"
        cursor = conn.execute(query, (id,))
        row = cursor.fetchone()

        if row is None:
            return None

        columns = [description[0] for description in cursor.description]
        row_dict = dict(zip(columns, row))

        return cls(**row_dict)

    @classmethod
    def filter(cls: Type[T], conn: sqlite3.Connection, **kwargs: Any) -> List[T]:
        """Filter records based on criteria."""
        conditions = [f"{key}=?" for key in kwargs.keys()]
        values = list(kwargs.values())
        query = f"SELECT * FROM {cls._table_name}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"

        cursor = conn.execute(query, values)
        results = []

        for row in cursor:
            columns = [description[0] for description in cursor.description]
            row_dict = dict(zip(columns, row))
            results.append(cls(**row_dict))

        return results

    def delete(self, conn: sqlite3.Connection):
        """Delete the model instance from the database."""
        if self._id is None:
            raise ValueError("Cannot delete unsaved instance")

        query = f"DELETE FROM {self._table_name} WHERE id=?"
        conn.execute(query, (self._id,))
        conn.commit()

    def __str__(self):
        fields_str = ', '.join(f"{k}={v!r}" for k, v in self._data.items())
        return f"{self.__class__.__name__}(id={self._id}, {fields_str})"


# Example usage:
class User(Model):
    name = TextField()
    age = IntegerField()
    email = TextField(required=True)
    created_at = DateTimeField(default=datetime.now())


class Post(Model):
    title = TextField()
    content = TextField()
    author_id = IntegerField()
    views = IntegerField(default=0)
    created_at = DateTimeField(default=datetime.now())


# Usage example:
def main():
    # Create database connection
    conn = sqlite3.connect(':memory:')

    # Create tables
    User.create_table(conn)
    Post.create_table(conn)

    # Create a user
    user = User(name="John Doe", age=30, email="john@example.com")
    user_id = user.save(conn)
    print(f"Created user: {user}")

    # Create some posts
    post1 = Post(
        title="First Post",
        content="Hello, World!",
        author_id=user_id
    )
    post1.save(conn)

    post2 = Post(
        title="Second Post",
        content="Another post",
        author_id=user_id
    )
    post2.save(conn)

    # Query examples
    # Get user by ID
    retrieved_user = User.get(conn, user_id)
    print(f"Retrieved user: {retrieved_user}")

    # Filter posts by author
    user_posts = Post.filter(conn, author_id=user_id)
    print(f"User posts: {len(user_posts)}")
    for post in user_posts:
        print(f"- {post}")

    # Update a post
    post1.content = "Updated content"
    post1.save(conn)

    # Delete a post
    post2.delete(conn)

    # Close connection
    conn.close()


if __name__ == "__main__":
    main()