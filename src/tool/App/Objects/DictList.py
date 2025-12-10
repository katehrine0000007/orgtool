from typing import Any
from App.Objects.Object import Object

class DictList(Object):
    '''
    List with object that contains "name" field and so can be used as Dict
    '''

    items: list[Object] # name-field-containing

    def toList(self) -> list:
        return self.items

    def toNames(self) -> list:
        names = []
        for val in self.toList():
            names.append(val.name)

        return names

    def toDict(self) -> dict:
        dicts = {}
        for item in self.items:
            dicts[item.name] = item

        return dicts

    @staticmethod
    def fromDict(dict: dict):
        items = list()
        for key, val in dict.items():
            items.append(val)

        return DictList(items)

    def get(self, name: str) -> Any:
        return self.toDict().get(name)

    def append(self, item: Any):
        self.items.append(item)
