from src.shared.domain.entities.withdraw import Withdraw

class WithdrawViewmodel:
    num_serie: str
    email: str
    withdraw_time: int
    finish_time: int

    def __init__(self, withdraw: Withdraw):
        self.num_serie = withdraw.num_serie
        self.email = withdraw.email
        self.withdraw_time = withdraw.withdraw_time
        self.finish_time = withdraw.finish_time

    def to_dict(self):
        return {
            'num_serie' : self.num_serie,
            'email' : self.email,
            'withdraw_time' : self.withdraw_time,
            'finish_time' : self.finish_time
        }

class FinishWithdrawViewmodel:
    withdraw: Withdraw

    def __init__(self, withdraw: Withdraw):
        self.withdraw = withdraw

    def to_dict(self) -> dict:
        return {
            'withdraw' : WithdrawViewmodel(self.withdraw).to_dict(),
            'message' : 'the withdraw has been finished'
        }