from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, Forbidden, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO

from .get_all_notebooks_usecase import GetAllNotebooksUsecase
from .get_all_notebooks_viewmodel import GetAllNotebooksViewmodel

class GetAllNotebooksController:
    
    def __init__(self, usecase: GetAllNotebooksUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()
            notebooks = self.usecase(user=requester_user)
            viewmodel = GetAllNotebooksViewmodel(notebooks=notebooks)
            return OK(viewmodel.to_dict())
        
        except MissingParameters as err:
            return BadRequest(err.message)
        
        except ForbiddenAction as err:
            return Forbidden(err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])
        