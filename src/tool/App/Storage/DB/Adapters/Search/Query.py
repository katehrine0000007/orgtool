from typing import Any, Generator, Self
from abc import ABC, abstractmethod
from App.Storage.DB.Adapters.Search.Condition import Condition
from App.Storage.DB.Adapters.Representation.ObjectAdapter import ObjectAdapter

class Query(ABC):
    _query: Any = None
    _model: Any = None

    @abstractmethod
    def addCondition(self, condition: Condition) -> Self:
        ...

    @abstractmethod
    def addSorting(self, condition: Condition) -> Self:
        ...

    @abstractmethod
    def first(self) -> ObjectAdapter:
        ...
    '''
    @abstractmethod
    def page(self, page: int, per_page: int) -> None:
        ...
    '''
    @abstractmethod
    def getAll(self) -> Generator[ObjectAdapter]:
        ...
