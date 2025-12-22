from App.Objects.Mixins.BaseModel import BaseModel
from pydantic import Field

class Key(BaseModel):
    '''
    Description of something (english default)
    '''

    value: str = Field(default = '')
    id: str = Field(default = '')
