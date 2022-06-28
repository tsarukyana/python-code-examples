class Employee(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        employee = cls(first_name, last_name)
        return employee


ahmed = Employee.from_string('Ahmed Besbes')
