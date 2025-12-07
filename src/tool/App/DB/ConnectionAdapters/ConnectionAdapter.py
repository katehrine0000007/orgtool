from App.Objects.Object import Object
from pydantic import Field

class ConnectionAdapter(Object):
    protocol: str = Field(default = 'none')
    delimiter: str = Field(default = ':///')

    def insertObject(self, item: Object):
        pass
