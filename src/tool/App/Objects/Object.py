from .BaseModel import BaseModel
from .Section import Section
from .Hookable import Hookable
from .Configurable import Configurable
from .Submodules import Submodules
from typing import ClassVar

class Object(BaseModel, Section, Submodules, Hookable, Configurable):
    '''
    The base class of app, extended pydantic BaseModel.
    Fields can be flushed to json, also there is Section (log) functions and hooks.

    MRO's:
    Validable, Configurable, Submodules, Variableable
    '''

    self_name: ClassVar[str] = 'Object'
