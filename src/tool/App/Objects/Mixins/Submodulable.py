from App.Objects.Relations.Submodule import Submodule

class Submodulable:
    '''
    Allows to set objects that are connected with current object.
    It applies submodules by __mro__ and uses App.Objects.Submodule for linking
    '''

    @classmethod
    def getSubmodules(cls) -> list[Submodule]:
        return []

    @classmethod
    def getAllSubmodules(cls, with_role: list[str] | None = None) -> list[Submodule]:
        modules = []

        for item in cls.getMRO():
            if hasattr(item, 'getSubmodules') == False:
                continue

            _items = item.getSubmodules()
            if _items == None:
                continue

            for submodule in _items:
                if with_role != None:
                    contains_len = 0
                    for role in submodule.role:
                        if role in with_role:
                            contains_len += 1

                    if contains_len < len(with_role):
                        continue

                modules.append(submodule)

        return modules
