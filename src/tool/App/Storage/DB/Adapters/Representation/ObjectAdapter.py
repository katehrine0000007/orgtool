from Data.JSON import JSON
from App import app
from App.Objects.Link import Link as CommonLink
from typing import Any, Generator
from App.Objects.Object import Object
from abc import ABC, abstractmethod
from App.Storage.DB.Adapters.Representation.AbstractAdapter import AbstractAdapter

class ObjectAdapter(AbstractAdapter):
    content: str = None # Encoded json

    @classmethod
    @abstractmethod
    def getQuery(self):
        ...

    @abstractmethod
    def flush_content(self, item: Object):
        ...

    @abstractmethod
    def getLinks(self) -> Generator[CommonLink]:
        ...

    @abstractmethod
    def addLink(self, link: CommonLink):
        ...

    @abstractmethod
    def removeLink(self, link: CommonLink):
        ...

    def toPython(self):
        _content = JSON().fromText(self.content)
        _object_name = _content.data.get('saved_via').get('object_name')
        _class = app.ObjectsList.getByName(_object_name).getModule()
        _item = _class.model_validate(_content.data, strict = False)
        _item.setDb(self)

        return _item
