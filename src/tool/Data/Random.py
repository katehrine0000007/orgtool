from App.Objects.Extractor import Extractor
from App.Arguments.Argument import Argument
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.Int import Int
from App.Arguments.ArgumentDict import ArgumentDict
import random

class Random(Extractor):
    @classmethod
    def getArguments(cls):
        return ArgumentDict(items=[
            Argument(
                name = "min",
                default = 0,
                orig = Int,
                assertions = [
                    NotNoneAssertion()
                ]
            ),
            Argument(
                name = "max",
                default = 100,
                orig = Int,
                assertions = [
                    NotNoneAssertion()
                ]
            )
        ])

    async def implementation(self, i) -> None:
        objects = Int()
        objects.value = self.randomInt(i.get('min'), i.get('max'))

        self.append(objects)

    def randomInt(self, min: int, max: int):
        return random.randint(min, max)

    def randomFloat(self, min: float, max: float):
        return random.uniform(min, max)
