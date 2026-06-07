#Encapsulation
class BikeStation:
    def __init__(self,name:str,total_docks:int,rented_bikes=0)->None:
        self._name=name
        self.total_docks=total_docks        
        self.rented_bikes=rented_bikes
    @property
    def name(self):
        return self._name
    @property
    def total_docks(self):
        return self._total_docks
    @total_docks.setter
    def total_docks(self, new_val:int):
        if new_val <1:
            raise ValueError("Total docks must be at least 1")
        self._total_docks=new_val
    @property
    def rented_bikes(self):
        return self._rented_bikes
    @rented_bikes.setter
    def rented_bikes(self,num_of_rented:int):
        if num_of_rented<0:
            raise ValueError("Rented bikes cannot be negative")
        if num_of_rented>self._total_docks:
            raise ValueError("Rented bikes cannot exceed total docks")
        self._rented_bikes=num_of_rented
    @property
    def available_bikes(self)->int:
        return self._total_docks-self._rented_bikes
    @property
    def rental_rate(self)->float:
        return round((self._rented_bikes/self._total_docks)*100,2)
    def rent(self,bikes:int)->None:
        if bikes<=0:
            raise ValueError("Number of bikes must be positive")
        if bikes>self.available_bikes:
            raise ValueError("Not enough available bikes")
        self._rented_bikes+=bikes
    def dock(self,bikes:int)->None:
        if bikes<=0:
            raise ValueError("Number of bikes must be positive")
        if bikes>self._rented_bikes:
            raise ValueError("Cannot dock more than rented")
        self._rented_bikes-=bikes
s = BikeStation("Central Park", 25)
print(s.name, s.available_bikes, s.rental_rate)
s.rent(15)
print(s.rented_bikes, s.rental_rate)
s.dock(5)
print(s.available_bikes)
try:
    s.rent(20)
except ValueError as e:
    print(e)
try:
    s.name = "X"
except AttributeError:
    print("Cannot change station name")
