from App.Storage.DB.Adapters.Connection.SQLAlchemyAdapter import SQLAlchemyAdapter
from pydantic import Field

class SQLiteAdapter(SQLAlchemyAdapter):
    protocol_name = 'sqlite'
    content: str = Field(default = None)

    def getConnectionStringContent(self):
        if self.content != None:
            return str(self.content)
        else:
            return str(self._storage_item.getDir().joinpath(self.name + '.db'))
