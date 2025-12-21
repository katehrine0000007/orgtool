from abc import abstractmethod
from typing import Any

class AbstractAdapter():
    _adapter: Any = None
    uuid: int = None

    @classmethod
    @abstractmethod
    def getById(self, uuid: int):
        ...

    @abstractmethod
    def toPython(self):
        ...

    @abstractmethod
    def toDB(self, object):
        pass
