from pydantic import Field
from datetime import datetime
from pydantic import BaseModel as PydanticBaseModel
from .Object import Object
from .Source import Source
from typing import ClassVar

class Saveable(Object):
    '''
    Item that can be flushed into DB

    display_name: title that will be shown in the ui, is changeable
    original_name: title that was written after creation, meant to be unchangeable
    display_description: description that will 

    "unlisted" is probaly not needed here;
    '''

    self_name: ClassVar[str] = 'Saveable'

    class Outer(PydanticBaseModel):
        '''
        Additional data about object
        '''
        thumbnail: dict = Field(default = None)
        duration: int = Field(default = None)

    class Saved(PydanticBaseModel):
        name: str = Field(default = None)
        method: str = Field(default = None)
        call: int = Field(default = None)

    display_name: str = Field(default=None)
    original_name: str = Field(default=None)
    display_description: str = Field(default=None)
    original_description: str = Field(default=None)
    index_description: str = Field(default=None)

    created_at: datetime = Field(default_factory=lambda: datetime.now())
    declared_created_at: datetime = Field(default_factory=lambda: datetime.now())
    edited_at: datetime = Field(default=None)

    '''
    If you want to extend these fields, extend them as internal classes and annotate again
    '''
    source: Source = Field(default = Source())
    outer: Outer = Field(default = Outer())
    saved: Saved = Field(default = Saved())

    collection: bool = Field(default=False)
    unlisted: bool = Field(default=False)

    def getContent(self):
        '''
        TODO: return all fields except those listed above
        '''
        pass

    def toContentUnit(self):
        pass

    def fromContentUnit(self):
        pass
