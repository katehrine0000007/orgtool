from pydantic import Field, BaseModel

class Source(BaseModel):
    '''
    Where from an object was obtained
    '''
    types: str = Field(default = None)
    content: str = Field(default = None)
