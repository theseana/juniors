# File Structure

- database
    - `models.py`
    - `connection.py`
- `main.py`

## First Step
### `connection.py`
1. Create a database
   - `CREATE DATABASE club`
2. Edit `connection.py` file
```
self.engine = create_engine(
    'mysql://poulstar:poulstar@localhost/club'
)
```
### 'models.py
Now create our Class model, for table.

### gui.py
UI of project

### main.py
Use GUI class and run the program