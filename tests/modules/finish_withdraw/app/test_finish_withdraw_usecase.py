import pytest
from src.modules.finish_withdraw.app.finish_withdraw_usecase import FinishWithdrawUsecase
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role import ROLE
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_FinishWithdrawUsecase:

    def test_finish_withdraw_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        requester_user = User(
            ra=None,
            name="Rony Rustico",
            email="rony@maua.br",
            role=ROLE.EMPLOYEE
        )
        withdraw = usecase(num_serie='34036', user=requester_user)
        assert withdraw == repo.withdraws[0]
        assert repo.withdraws[0].finish_time != None

    def test_finish_withdraw_usecase_no_items_found(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        requester_user = User(
            ra=None,
            name="Rony Rustico",
            email="rony@maua.br",
            role=ROLE.EMPLOYEE
        )
        with pytest.raises(NoItemsFound):
            usecase(num_serie='34035', user=requester_user)
            
    def test_finish_withdraw_usecase_forbidden_action(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        requester_user = User(
            ra="22018440",
            name="Aluno",
            email="22.01844-0@maua.br",
            role=ROLE.STUDENT
        )
        with pytest.raises(ForbiddenAction):
            usecase(num_serie='34036', user=requester_user)