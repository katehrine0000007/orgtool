from pydantic import Field, BaseModel
from typing import Optional

class Source(BaseModel):
    '''
    Where from an object was obtained
    '''
    types: Optional[str] = Field(default = None)
    content: Optional[str] = Field(default = None)
