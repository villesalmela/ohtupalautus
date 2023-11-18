from entities.user import User
from string import ascii_letters

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserExistsError(Exception):
    pass


class BadUsernameError(Exception):
    pass


class BadPasswordError(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not len(username) >= 3:
            raise BadUsernameError("Bad username")
        
        if not all([char in ascii_letters for char in username]):
            raise BadPasswordError("Bad username")
        
        existing = self._user_repository.find_by_username(username)
        if existing is not None:
            raise UserExistsError("Username already taken")
        
        if not len(password) >= 8:
            raise BadPasswordError("Bad password")
        
        if all([char in ascii_letters for char in password]):
            raise BadPasswordError("Bad password")
        

        

