from App.Objects.Object import Object

class AuthToken(Object):
    user: Object

    def check_rights(self, obj: Object):
        return True
