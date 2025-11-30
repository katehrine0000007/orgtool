from .BaseModel import BaseModel
from .Section import Section
from .Hookable import Hookable
from typing import ClassVar

class Object(BaseModel, Section, Hookable):
    '''
    The base class of app, extended pydantic BaseModel.
    Fields can be flushed to json, also there is Section (log) functions and hooks.
    '''

    self_name: ClassVar[str] = 'Object'
