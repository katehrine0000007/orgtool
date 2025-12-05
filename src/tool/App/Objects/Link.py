from App.Objects.BaseModel import BaseModel
from App.Objects.Object import Object
from pydantic import Field
from enum import Enum

class LinkTypeEnum(Enum):
    CONTENT = 0 # will be used for json content insertion
    EXTERNAL = 1

class Link(BaseModel):
    '''
    Link to an object
    '''

    item: Object = Field()
    common: bool = Field(default = False)
    thumbnail: bool = Field(default = False)
    revision: bool = Field(default = False)
    link_type: LinkTypeEnum = Field(default = LinkTypeEnum.CONTENT.value)
