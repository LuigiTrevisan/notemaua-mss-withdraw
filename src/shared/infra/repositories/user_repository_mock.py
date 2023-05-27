from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users = List[User]
    
    def __init__(self):
        self.users = [
            User(ra="22011020", name="Luigi Television", email="22.01102-0@maua.br", role=ROLE.STUDENT),
            User(ra="22010490", name="Vitor Negro", email="22.01049-0@maua.br", role=ROLE.STUDENT),
            User(ra="22015892", name="Gabriel Milanesa", email="22.01589-2@maua.br", role=ROLE.STUDENT),
            User(ra=None, name="Rony Rustico", email="rony@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Arthur Television", email="arthur@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Pana Aula", email="pana@maua.br", role=ROLE.ADMIN),
        ]
        
        
    def get_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
        