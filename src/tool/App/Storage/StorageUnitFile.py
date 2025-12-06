from App.Objects.Object import Object
from pydantic import Field

class StorageUnitFile(Object):
    path: str = Field(default = None)
    name: str = Field(default = None)
    ext: str = Field(default = None)
    mime: str = Field(default = None)
    size: int = Field(default = None)
    is_common: bool = Field(default = False)
