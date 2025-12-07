from App.Executables.Extractor import Extractor
from App.Arguments.Types.Int import Int
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.Number import Number
from App.Arguments.ArgumentsDict import ArgumentsDict
import random

class Random(Extractor):
    @classmethod
    def getArguments(cls):
        return ArgumentsDict.fromList([
            Int(
                name = "min",
                default = 0,
                assertions = [
                    NotNoneAssertion()
                ]
            ),
            Int(
                name = "max",
                default = 100,
                assertions = [
                    NotNoneAssertion()
                ]
            )
        ])

    def implementation(self, i) -> None:
        objects = Number()
        objects.number = random.randint(i.get('min'), i.get('max'))

        self.append(objects)
