from .Mixins.BaseModel import BaseModel
from .Mixins.Section import Section
from .Mixins.Hookable import Hookable
from .Mixins.Configurable import Configurable
from .Mixins.Linkable import Linkable
from .Mixins.Convertable import Convertable
from .Mixins.ModuleRequireable import ModuleRequireable
from .Mixins.Submodulable import Submodulable
from .Mixins.Saveable import Saveable
from App.ACL.Limitable import Limitable
from App.Storage.DB.DBInsertable import DBInsertable
from App.Daemons.Daemonable import Daemonable
from typing import ClassVar
from pydantic import ConfigDict
from App import app

class Object(BaseModel, Linkable, Saveable, ModuleRequireable, Section, Submodulable, Hookable, Configurable, Convertable, DBInsertable, Daemonable, Limitable):
    '''
    The base class of app
    '''

    model_config = ConfigDict(extra='allow')
    self_name: ClassVar[str] = 'Object'

    @classmethod
    def asArgument(cls, val: str) -> BaseModel:
        if type(val) == str:
            _val = app.ObjectsList.getByName(key = val)
            if _val == None:
                return None

            return _val.getModule()

        return super().asArgument(val)
