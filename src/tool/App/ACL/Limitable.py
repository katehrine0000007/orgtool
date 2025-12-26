class Limitable():
    @classmethod
    def canBeUsedBy(self, token):
        if token == None:
            return False

        return token.check_rights(self)
