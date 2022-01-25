class Games:
    def __init__(self,name,price,rating):
        self.name = name
        self.price = price
        self.rating = rating
    
    def toString(self):
        print(f"Name:{self.name},Price:{self.price},Rating:{self.rating}")

game1 = Games("Mario",1000,4.5)
game1.toString()