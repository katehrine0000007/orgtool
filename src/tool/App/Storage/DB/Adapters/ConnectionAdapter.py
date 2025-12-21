from App.Objects.Object import Object
from pydantic import Field
from typing import Any, ClassVar
from snowflake import SnowflakeGenerator

class ConnectionAdapter(Object):
    '''
    Adapter for some object store (for example, db)
    '''

    __abstract__ = True
    protocol_name: ClassVar[str] = ''
    _unserializable = ['_storage_item', '_id_gen', 'ObjectAdapter', 'LinkAdapter']

    protocol: str = Field(default = 'none')
    delimiter: str = Field(default = ':///')
    name: str = Field(default = 'objects')

    _storage_item: Any = None # Storage item DI
    _id_gen: Any = None
    ObjectAdapter: Any = None
    LinkAdapter: Any = None

    def _set_id_get(self):
        self._id_gen = SnowflakeGenerator(32)

    def flush(self, item: Object):
        unit = self.ObjectAdapter()
        unit.toDB(item)

        return unit

    def getQuery(self):
        return self.ObjectAdapter.getQuery()
