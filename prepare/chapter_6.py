class Carculator:

    def __init__(self, first, second):
        self.first = first 
        self.second = second

    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second
    
    def add(self):
        return self.first + self.second
    def div(self):
        return self.first / self.second
    
class MoreCalculator(Carculator):

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            return "INFINITE"
        else:
            return self.first / self.second
        
# a = Carculator(1,0)
# print(a.div())

s = MoreCalculator(1,0)     
print(s.div())

