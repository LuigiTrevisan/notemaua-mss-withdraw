import pytest
from src.shared.domain.entities.notebook import Notebook
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Notebook:
    
    def test_notebook(self):
        notebook = Notebook(
            serial="34756",
            isActive=True
        )
        
        assert type(notebook) == Notebook
        assert notebook.serial == "34756"
        assert notebook.isActive == True
        
    def test_notebook_serial_is_none(self):
        with pytest.raises(EntityError):
            Notebook(
                serial=None,
                isActive=True
            )
            
    def test_notebook_serial_not_str(self):
        with pytest.raises(EntityError):
            Notebook(
                serial=34756,
                isActive=True
            )
            
    def test_notebook_serial_not_decimal(self):
        with pytest.raises(EntityError):
            Notebook(
                serial="34a56",
                isActive=True
            )
            
    def test_notebook_serial_wrong_length(self):
        with pytest.raises(EntityError):
            Notebook(
                serial="3475",
                isActive=True
            )
            
    def test_notebook_isActive_is_none(self):
        notebook = Notebook(
                serial="34756",
                isActive=None
            )
        
        assert notebook.isActive == False
        
    def test_notebook_isActive_not_bool(self):
        with pytest.raises(EntityError):
            Notebook(
                serial="34756",
                isActive="True"
            )