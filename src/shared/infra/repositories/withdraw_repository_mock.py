from typing import List
from src.shared.domain.enums.role import ROLE
from src.shared.domain.repositories.withdraw_repository_interface import IWithdrawRepository
from src.shared.domain.entities.user import User
from src.shared.domain.entities.notebook import Notebook
from src.shared.domain.entities.withdraw import Withdraw

class WithdrawRepositoryMock(IWithdrawRepository):
    users: List[User]
    notebooks: List[Notebook]
    withdraws: List[Withdraw]
    
    def __init__(self):
        self.users = [
            User(ra="22011020", name="Luigi Television", email="22.01102-0@maua.br", role=ROLE.STUDENT),
            User(ra="22010490", name="Vitor Negro", email="22.01049-0@maua.br", role=ROLE.STUDENT),
            User(ra="22015892", name="Gabriel Milanesa", email="22.01589-2@maua.br", role=ROLE.STUDENT),
            User(ra=None, name="Rony Rustico", email="rony@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Arthur Television", email="arthur@maua.br", role=ROLE.EMPLOYEE),
            User(ra=None, name="Pana Aula", email="pana@maua.br", role=ROLE.ADMIN),
        ]
        
        self.notebooks = [
            Notebook(num_serie="34035", isActive=False),
            Notebook(num_serie="34036", isActive=True),
            Notebook(num_serie="34037", isActive=False),
            Notebook(num_serie="34038", isActive=True),
        ]
        
        self.withdraws = [
            Withdraw(withdraw_id=1, num_serie="34036", email="22.01102-0@maua.br", withdraw_time=1682610909494),
            Withdraw(withdraw_id=2, num_serie="34038", email="22.01049-0@maua.br", withdraw_time=1682611052153),
            Withdraw(withdraw_id=3, num_serie="34037", email="22.01589-2@maua.br", withdraw_time=1682604600000, finish_time=1682611200000),
    ]
        
    def get_withdraw_by_email(self, email):
        for withdraw in self.withdraws:
            if withdraw.email == email:
                return withdraw
        return None
