from .finish_withdraw_usecase import FinishWithdrawUsecase
from .finish_withdraw_viewmodel import FinishWithdrawViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK, InternalServerError, NotFound
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock


class FinishWithdrawController:
    repo = WithdrawRepositoryMock()

    def __init__(self, usecase: FinishWithdrawUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('num_serie') is None:
                raise MissingParameters('num_serie')

            if type(request.data.get('num_serie')) is not str:
                raise WrongTypeParameter('num_serie', 'str', type(request.data.get('num_serie')))

            withdraw = self.usecase(
                num_serie=request.data.get('num_serie')
            )
            viewmodel = FinishWithdrawViewmodel(withdraw=withdraw).to_dict()
            return OK(viewmodel)

        except MissingParameters as err:
            return BadRequest(err.message)

        except WrongTypeParameter as err:
            return BadRequest(err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])