
from app.db import DataDatabaseSqlite3, SQLITE_FILENAME 

# charging one time when importing !

_db = DataDatabaseSqlite3(filename=SQLITE_FILENAME)
_db.db_init() 

def get_db() -> DataDatabaseSqlite3:
    return _db 


