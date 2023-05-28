import pytest
from src.shared.domain.entities.notebook import Notebook
from src.shared.helpers.errors.domain_errors import EntityError

class Test_Notebook:
    
    def test_notebook(self):
        notebook = Notebook(
            num_serie="34756",
            isActive=True
        )
        
        assert type(notebook) == Notebook
        assert notebook.num_serie == "34756"
        assert notebook.isActive == True
        
    def test_notebook_num_serie_is_none(self):
        with pytest.raises(EntityError):
            Notebook(
                num_serie=None,
                isActive=True
            )
            
    def test_notebook_num_serie_not_str(self):
        with pytest.raises(EntityError):
            Notebook(
                num_serie=34756,
                isActive=True
            )
            
    def test_notebook_num_serie_not_decimal(self):
        with pytest.raises(EntityError):
            Notebook(
                num_serie="34a56",
                isActive=True
            )
            
    def test_notebook_num_serie_wrong_length(self):
        with pytest.raises(EntityError):
            Notebook(
                num_serie="3475",
                isActive=True
            )
        
    def test_notebook_isActive_not_bool(self):
        with pytest.raises(EntityError):
            Notebook(
                num_serie="34756",
                isActive="True"
            )