import pytest

from src.shared.infra.repositories.withdraw_repository_mock import WithdrawRepositoryMock
from src.modules.get_all_notebooks.app.get_all_notebooks_usecase import GetAllNotebooksUsecase
from src.modules.get_all_notebooks.app.get_all_notebooks_viewmodel import GetAllNotebooksViewmodel

class Test_GetAllNotebooksViewModel:
    def test_get_all_notebooks_viewmodel(self):
        repo = WithdrawRepositoryMock()
        usecase = GetAllNotebooksUsecase(repo=repo)
        viewmodel = GetAllNotebooksViewmodel(notebooks=usecase()).to_dict()
        expected = {
   'notebooks':[
                {
                    'notebook':{
                        'num_serie':'34035',
                        'isActive':False
                    },
                    'withdraws':None
                },
                {
                    'notebook':{
                        'num_serie':'34036',
                        'isActive':True
                    },
                    'withdraws':[
                        {
                        'withdraw_id':1,
                        'num_serie':'34036',
                        'email':'22.01102-0@maua.br',
                        'withdraw_time':1682610909494,
                        'finish_time':None
                        }
                    ]
                },
                {
                    'notebook':{
                        'num_serie':'34037',
                        'isActive':False
                    },
                    'withdraws':None
                },
                {
                    'notebook':{
                        'num_serie':'34038',
                        'isActive':True
                    },
                    'withdraws':[
                        {
                        'withdraw_id':2,
                        'num_serie':'34038',
                        'email':'22.01049-0@maua.br',
                        'withdraw_time':1682611052153,
                        'finish_time':None
                        }
                    ]
                }
            ],
            'message':'Notebooks found successfully!'
            }
        
        assert viewmodel == expected
        