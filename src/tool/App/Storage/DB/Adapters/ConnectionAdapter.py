from App.Objects.Object import Object
from pydantic import Field
from typing import Any, ClassVar
from snowflake import SnowflakeGenerator

class ConnectionAdapter(Object):
    '''
    Adapter for some object store (for example, db)
    '''

    protocol_name: ClassVar[str] = ''

    protocol: str = Field(default = 'none')
    delimiter: str = Field(default = ':///')
    name: str = Field(default = 'objects')

    _storage_item: Any = None # Storage item DI
    _id_gen: Any = None
    ObjectAdapter: Any = None
    ObjectLinkAdapter: Any = None

    def _set_id_get(self):
        self._id_gen = SnowflakeGenerator(32)

    def flush(self, item: Object):
        unit = self.ObjectAdapter()
        unit.flush(item)

        return unit
