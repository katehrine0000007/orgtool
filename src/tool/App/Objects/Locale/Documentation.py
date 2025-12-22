from App.Objects.Mixins.BaseModel import BaseModel
from App.Objects.Locale.Documentation import Key
from pydantic import Field

class Documentation(BaseModel):
    '''
    Description of something on english text
    '''

    name: Key = Field(default = None)
    description: Key = Field(default = None)
