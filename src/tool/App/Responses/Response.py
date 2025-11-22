from App.Objects.Object import Object
from pydantic import Field
from typing import Any

class Response(Object):
    data: Any = Field(default = None)

    def toDict(self) -> Any:
        '''
        Returns data in json serializable format
        '''
        return self.data

    def show(self) -> Any:
        return self.data
