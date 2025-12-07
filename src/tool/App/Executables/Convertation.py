from App.Objects.Executable import Executable
from App.Responses.ObjectsList import ObjectsList
from App.Arguments.ArgumentsDict import ArgumentsDict
from App.Arguments.Objects.Orig import Orig
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from typing import ClassVar

class Convertation(Executable):
    '''
    Executable that converts X model to Y model. Convertation logic needs to be writed in "implementation()"
    
    To get "X" in implementation:
    
    i.get("orig")
    self.converts_from

    To get "Y" class in implementation:

    self.converts_to
    '''
    converts_from: ClassVar = None
    converts_to: ClassVar = None

    @classmethod
    def getArguments(cls) -> ArgumentsDict:
        return ArgumentsDict.fromList([
            Orig(
                name = "orig",
                orig = cls.converts_from,
                assertions = [
                    NotNoneAssertion()
                ]
            )
        ])

    async def implementation(self, i) -> ObjectsList:
        pass
