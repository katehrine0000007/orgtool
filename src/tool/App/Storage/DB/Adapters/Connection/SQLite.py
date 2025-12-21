from App.Storage.DB.Adapters.Connection.SQLAlchemy import SQLAlchemy
from pydantic import Field

class SQLite(SQLAlchemy):
    protocol_name = 'sqlite'
    content: str = Field(default = None)

    def getConnectionStringContent(self):
        if self.content != None:
            return str(self.content)
        else:
            return str(self._storage_item.getDir().joinpath(self.name + '.db'))
