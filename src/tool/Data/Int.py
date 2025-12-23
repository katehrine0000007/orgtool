from App.Objects.Object import Object
from App.Objects.Displayment import Displayment

class Int(Object):
    value: int = None

    @classmethod
    def getDisplayments(cls):
        class DisplayAsString(Displayment):
            role = ['str']

            def implementation(self, i):
                orig = i.get('orig')
                return str(orig.value)

        return [DisplayAsString()]

    @classmethod
    def asArgument(cls, val):
        if val == None:
            return None

        return int(val)
