from App.Objects.Object import Object
from App.Arguments.Argument import Argument
from pydantic import Field

class ArgumentsDict(Object):
    items: dict = Field(default= { })

    def add(self, name, argument: Argument):
        self.items[name] = argument

    def get(self, name, default = None):
        _out = self.items.get(name)
        if _out == None:
            return default

        if getattr(_out, "val", None) != None:
            return _out.value
        else:
            return _out

    def toNames(self) -> list:
        items = []
        for name, item in self.items.items():
            items.append(name)
        
        return items

    def toDict(self, exclude: list = []):
        _items = {}
        for name, item in self.items.items():
            if name in exclude:
                continue

            _items[name] = self.get(name)

        return _items
