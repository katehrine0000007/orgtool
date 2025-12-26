from App.Objects.Object import Object
from App.ACL.AuthToken import AuthToken
from argon2 import PasswordHasher
from pydantic import Field

class User(Object):
    name: str = Field()
    password_hash: str = Field(default = None, repr = False, exclude = True)

    def auth(self, password: str):
        hasher = PasswordHasher()

        if self.password_hash == None or hasher.verify(self.password_hash, password):
            return AuthToken(
                user = self
            )

    def check_rights(self, object: Object):
        return True
