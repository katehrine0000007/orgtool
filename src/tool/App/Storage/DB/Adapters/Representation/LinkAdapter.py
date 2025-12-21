from App.Objects.Link import Link
from Data.JSON import JSON
from abc import abstractmethod
from App.Storage.DB.Adapters.Representation.AbstractAdapter import AbstractAdapter
from App.Storage.DB.Adapters.Representation.ObjectAdapter import ObjectAdapter

class LinkAdapter(AbstractAdapter):
    owner: int = None
    target: int = None
    role: str = None
    order: int = None

    @abstractmethod
    def getTarget(self) -> ObjectAdapter:
        pass

    def toPython(self) -> Link:
        _role = []
        if self.role != None:
            _role = JSON().fromText(self.role)

        _link = Link(item = None)
        _link.item = self.getTarget().toPython()
        _link.role = _role
        _link.setDb(self)

        return _link
