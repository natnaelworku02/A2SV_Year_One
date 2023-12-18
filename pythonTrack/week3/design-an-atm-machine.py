class ATM:

    def __init__(self):
        self.bank_notes = [20,50,100,200,500]
        self.bank_note_count = [0]*5
        
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,notes_count in enumerate(banknotesCount):
            self.bank_note_count[i] += notes_count
        

    def withdraw(self, amount: int) -> List[int]:
        note_index = 4
        withdraw_note_count = [0] * 5

        while amount > 0 and note_index > -1:
            withdraw_note_count[note_index]=min (self.bank_note_count[note_index], amount// self.bank_notes[note_index])
            
            amount-= withdraw_note_count[note_index] * self.bank_notes[note_index]
            note_index-=1
        if amount>0:
            return [-1]
        else:
            for i,n in enumerate(withdraw_note_count):
                self.bank_note_count[i]-=n
            return withdraw_note_count        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)