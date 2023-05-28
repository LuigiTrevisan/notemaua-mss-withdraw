from src.shared.domain.entities.notebook import Notebook

class NotebookDynamoDTO:
    num_serie: str
    isActive: bool
    
    def __init__(self, num_serie: str, isActive: bool):
        self.num_serie = num_serie
        self.isActive = isActive
        
    @staticmethod
    def from_entity(notebook: Notebook) -> "NotebookDynamoDTO":
        return NotebookDynamoDTO(
            num_serie=notebook.num_serie,
            isActive=notebook.isActive
        )
        
    def to_dynamo(self) -> dict:
        return {
            "entity" : "notebook",
            "num_serie": self.num_serie,
        }
        
    @staticmethod
    def from_dynamo(notebook_data: dict) -> "NotebookDynamoDTO":
        return NotebookDynamoDTO(
            num_serie=notebook_data["num_serie"],
            isActive=notebook_data.get("isActive")
        )
        
    def to_entity(self) -> Notebook:
        return Notebook(
            num_serie=self.num_serie,
            isActive=self.isActive
        )
        
    def __repr__(self):
        return f"NotebookDynamoDTO(num_serie={self.num_serie}, isActive={self.isActive})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__