from pydantic import Field
#from App.Objects.Object import Object
from App.Objects.Link import Link

class Linkable:
    '''
    Object that can contain links to other objects
    '''

    links: list[Link] = Field(default=[], exclude = True)

    def addLink(self, item: Link) -> None:
        self.links.append(item)

    def getLinks(self) -> list[Link]:
        return self.links

    def linkItem(self, object, link_type: int):
        pass

    def addCommonLink(self, item: Link) -> None:
        pass

    def unlink(self, item: Link, type: int) -> None:
        pass
