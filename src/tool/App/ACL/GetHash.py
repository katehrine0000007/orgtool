from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Responses.AnyResponse import AnyResponse
from argon2 import PasswordHasher
from Data.String import String

class GetHash(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'string',
                orig = String,
                assertions = [NotNoneAssertion()]
            )
        ])
    
    def implementation(self, i):
        hasher = PasswordHasher()

        return AnyResponse(data = hasher.hash(i.get('string')))
