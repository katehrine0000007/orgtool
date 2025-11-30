from pydantic import Field
from App.Objects.Object import Object

class Linkable:
    '''
    Object that can contain links to other objects (?)
    '''
    class Links(Object):
        items: list = Field()

    links: Links = Field(default=None)
