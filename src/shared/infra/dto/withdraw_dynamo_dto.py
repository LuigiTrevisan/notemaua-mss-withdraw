from src.shared.domain.entities.withdraw import Withdraw


class WithdrawDynamoDTO:
    withdraw_id: int
    num_serie: str
    email: str
    withdraw_time: int
    finish_time: int = None
    
    def __init__(self,  withdraw_id: int, num_serie: str, email: str, withdraw_time: int, finish_time: int = None):
        self.withdraw_id = withdraw_id
        self.num_serie = num_serie
        self.email = email
        self.withdraw_time = withdraw_time
        self.finish_time = finish_time
        
    @staticmethod
    def from_entity(withdraw: Withdraw) -> "WithdrawDynamoDTO":
        return WithdrawDynamoDTO(
            withdraw_id=withdraw.withdraw_id,
            num_serie=withdraw.num_serie,
            email=withdraw.email,
            withdraw_time=withdraw.withdraw_time,
            finish_time=withdraw.finish_time
        )
    
    def to_dynamo(self) -> dict:
        data = {
            "entity" : "withdraw",
            "withdraw_id": self.withdraw_id,
            "num_serie": self.num_serie,
            "email": self.email,
            "withdraw_time": self.withdraw_time,
            "finish_time": self.finish_time if self.finish_time is not None else None
        }
        
        data_without_none_values = {k: v for k, v in data.items() if v is not None}
        return data_without_none_values
    
    @staticmethod
    def from_dynamo(withdraw_data: dict) -> "WithdrawDynamoDTO":
        return WithdrawDynamoDTO(
            withdraw_id=withdraw_data["withdraw_id"],
            num_serie=withdraw_data["num_serie"],
            email=withdraw_data["email"],
            withdraw_time=withdraw_data["withdraw_time"],
            finish_time=withdraw_data["finish_time"] if "finish_time" in withdraw_data else None
        )
        
    def to_entity(self) -> Withdraw:
        return Withdraw(
            withdraw_id=self.withdraw_id,
            num_serie=self.num_serie,
            email=self.email,
            withdraw_time=self.withdraw_time,
            finish_time=self.finish_time
        )
        
    def __repr__(self):
        return f"WithdrawDynamoDTO(withdraw_id={self.withdraw_id}, num_serie={self.num_serie}, email={self.email}, withdraw_time={self.withdraw_time}, finish_time={self.finish_time})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__