# python-code-examples

### The Simple Flask CRUD Application

#### Installing (for linux)

open the terminal and follow the white rabbit.

```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=main.py
```
```
flask db init
```
```
flask db migrate -m "entries table"
```
```
flask db upgrade
```
```
flask run
```
