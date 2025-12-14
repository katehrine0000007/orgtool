from pydantic import BaseModel

class DBInfo(BaseModel):
    uuid: int
    db_name: str
