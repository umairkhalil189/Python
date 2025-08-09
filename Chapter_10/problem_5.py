from random import randint

class train:

    def __init__(self, train_no):
        self.train_no= train_no

    def book(self , fro, to):
        print(f"Ticket is booked in train no: {self.train_no} from {fro} to {to}")
    
    def getstatus(self):
        print(f"Train no: {self.train_no} is running on time.")

    def getFare(self,  fro, to):
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is {randint(1, 555)}")


t= train(12399)
t.book("ISB", "KHI")
t.getstatus()
t.getFare("ISB", "KHI")

# t= train()
# t.book(12399, "ISB", "KHI")
# t.getstatus(12399)

