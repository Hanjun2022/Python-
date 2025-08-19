def price(people):
    print("{0} 명 가격은 {1} 입니다.".format(people,people*10000))

def price_morining(people):
    print("{0}명 가격은 {1} 입니다.".format(people,people*400))
    
def price_solider(people):
    print("{0} 명 군인 할인 가격은 {1} 입니다.".format(people,people*1000))
    

class Lover:
    def __init__(self,name,like):
        self.name=name
        self.like=like 
    def print(self):
        print("안녕")