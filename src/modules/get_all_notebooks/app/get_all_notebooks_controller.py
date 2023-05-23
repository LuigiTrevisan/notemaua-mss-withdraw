from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError

from .get_all_notebooks_usecase import GetAllNotebooksUsecase
from .get_all_notebooks_viewmodel import GetAllNotebooksViewmodel

class GetAllNotebooksController:
    
    def __init__(self, usecase: GetAllNotebooksUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            
            viewmodel = GetAllNotebooksViewmodel(self.usecase)
            return OK(viewmodel.to_dict())
        
        except Exception as err:
            return InternalServerError(body=err.args[0])