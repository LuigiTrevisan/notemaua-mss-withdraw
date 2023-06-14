from .create_withdraw_usecase import CreateWithdrawUsecase
from .create_withdraw_viewmodel import CreateWithdrawViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, NotebookAlreadyActive, UserAlreadyActiveNotebook
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound
from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO 


class CreateWithdrawController:
    repo = WithdrawRepositoryMock()
    
    def __init__(self, usecase: CreateWithdrawUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()
            
            if request.data.get('num_serie') is None:
                raise MissingParameters('num_serie')
            
            if type(request.data.get('num_serie')) is not str:
                raise WrongTypeParameter('num_serie', 'str', type(request.data.get('num_serie')))
            
            withdraw = self.usecase(
                num_serie=request.data.get('num_serie'),
                email=requester_user.email
            )
            viewmodel = CreateWithdrawViewmodel(withdraw=withdraw).to_dict()
            return Created(viewmodel)
        
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
        
        except UserAlreadyActiveNotebook as err:
            return BadRequest(body=err.message)        
        
        except NotebookAlreadyActive as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
            