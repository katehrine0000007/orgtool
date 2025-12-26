from App.Objects.Object import Object
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Arguments.Argument import Argument
from pydantic import Field
from App.ACL.User import User
from App.ACL.GetHash import GetHash
from App import app

class AuthLayer(Object):
    users: list[User] = Field(default = [])

    def addUser(self, user: User):
        self.users.append(user)

    def getUserByName(self, name: str) -> User:
        for item in self.users:
            if item.name == name:
                return item

    def login(self, name: str, password: str):
        user = self.getUserByName(name)

        assert user != None, 'user not found'
        _usr = user.auth(password)
        assert _usr, 'invalid username or password'

        self.log(f"logged as {name}")

        return _usr

    @classmethod
    def mount(cls):
        default_root_password = 'root'

        _layer = cls()
        has_root = False
        for user in _layer.getOption('app.auth.users'):
            if user.name == 'root':
                has_root = True

            _layer.addUser(user)

        if has_root == False:
            _layer.addUser(User(
                    name = 'root',
                    # 2manywraps
                    password_hash = GetHash().implementation({'string': default_root_password}).data
                )
            )

        app.mount('AuthLayer', _layer)

    @classmethod
    def getSettings(cls):
        return [
            ListArgument(
                name = 'app.auth.users',
                default = [
                    {
                        'name': 'root',
                        'password_hash': '123'
                    }
                ],
                orig = User
            )
        ]
