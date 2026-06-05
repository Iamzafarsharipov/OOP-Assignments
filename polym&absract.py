
#1
from abc import abstractmethod,ABC
class Exchanger(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def exchange(self,value):
        pass
    def describe(self,value):
        exchanged=self.exchange(value)
        result=f"{self.name}: {value} -> {exchanged}"
        return result
#2
class USDToEUR(Exchanger):
    def __init__(self):
        super().__init__("USDToEUR")
    def exchange(self,value):
        result=round(value*0.9216,2)
        return result
#3
class USDToGBP(Exchanger):
    def __init__(self):
        super().__init__("USDToGBP")
    def exchange(self,value):
        result= round(value * 0.7893, 2)
        return result
#4
class USDToJPY(Exchanger):
    def __init__(self):
        super().__init__("USDToJPY")
    def exchange(self,value):
        result=round(value*149.52, 2)
        return result
#5
class CustomExchanger:
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
    def exchange(self, value):
        result=round(value*self.rate, 2)
        return result
    def describe(self,value):
        exchanged=self.exchange(value)
        result=f"{self.name}: {value} -> {exchanged}"
        return result
#6
class ExchangeLog:
    def __init__(self):
        self.entries_list=[]
    def record(self, exchanger_name, original, exchanged):
        self.entries_list.append(f"{exchanger_name}: {original} -> {exchanged}")
    def show(self):
        for entry in self.entries_list:
            print(entry)
#7
class ExchangeDesk:
    def __init__(self,name):
        self.name=name
        self.exchangers_list=[]
        self.log=ExchangeLog()
    def add_exchanger(self,exchanger):
        self.exchangers_list.append(exchanger)
    def exchange_all(self,value):
        print(f"=== {self.name} ===")
        for exchanger in self.exchangers_list:
            description=exchanger.describe(value)
            print(description)
            exchanged=exchanger.exchange(value)
            self.log.record(
                exchanger.name,
                value,
                exchanged
            )
        return None
    def show_log(self):
        print(f"--- Log for {self.name} ---")
        result=self.log.show()
        return result
desk = ExchangeDesk('Airport Kiosk')
desk.add_exchanger(USDToEUR())
desk.add_exchanger(USDToGBP())
desk.add_exchanger(USDToJPY())
desk.add_exchanger(CustomExchanger('USDToUZS', 12850.0))

desk.exchange_all(200)
print()
desk.exchange_all(75)
print()
desk.show_log()

try:
    e = Exchanger('test')
except TypeError:
    print('Cannot instantiate abstract class')

