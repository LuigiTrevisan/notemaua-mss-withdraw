from src.shared.domain.entities.notebook import Notebook
from src.shared.infra.dto.notebook_dynamo_dto import NotebookDynamoDTO


class Test_NotebookDynamoDTO:
    def test_notebook_dynamo_dto_from_entity(self):
        notebook = Notebook(num_serie="34036", isActive=True)
        notebook_dto = NotebookDynamoDTO.from_entity(notebook)
        assert notebook_dto == NotebookDynamoDTO(num_serie="34036", isActive=True)
        
    def test_notebook_dynamo_dto_to_dynamo(self):
        notebook_dto = NotebookDynamoDTO(num_serie="34036", isActive=True)
        assert notebook_dto.to_dynamo() == {
            "entity" : "notebook",
            "num_serie": "34036",
        }
        
    def test_notebook_dynamo_dto_from_dynamo(self):
        notebook_dto = NotebookDynamoDTO.from_dynamo({
            "entity" : "notebook",
            "num_serie": "34036",
            "isActive": True
        })
        assert notebook_dto == NotebookDynamoDTO(num_serie="34036", isActive=True)
        
    def test_notebook_dynamo_dto_to_entity(self):
        notebook_dto = NotebookDynamoDTO(num_serie="34036", isActive=True)
        assert notebook_dto.to_entity() == Notebook(num_serie="34036", isActive=True)
        
    def test_notebook_dynamo_dto_from_entity_to_dynamo(self):
        notebook = Notebook(num_serie="34036", isActive=True)
        notebook_dto = NotebookDynamoDTO.from_entity(notebook).to_dynamo()
        assert notebook_dto == {
            "entity" : "notebook",
            "num_serie": "34036",
        }
        
    def test_notebook_dynamo_dto_from_dynamo_to_entity(self):
        notebook = NotebookDynamoDTO.from_dynamo({
            "entity" : "notebook",
            "num_serie": "34036",
            "isActive": True
        }).to_entity()
        assert notebook == Notebook(num_serie="34036", isActive=True)