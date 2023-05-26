import pytest
from src.modules.finish_withdraw.app.finish_withdraw_usecase import FinishWithdrawUsecase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock

class Test_FinishWithdrawUsecase:

    def test_finish_withdraw_usecase(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        withdraw = usecase(num_serie='34036')
        assert withdraw == repo.withdraws[0]
        assert repo.withdraws[0].finish_time != None

    def test_finish_withdraw_usecase_no_items_found(self):
        repo = WithdrawRepositoryMock()
        usecase = FinishWithdrawUsecase(repo=repo)
        with pytest.raises(NoItemsFound):
            usecase(num_serie='34035')