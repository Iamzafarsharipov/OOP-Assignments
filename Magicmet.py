class Prescription:
    def __init__(self,medication_name:str,price_per_pill:float,pill_count:int)->None:
        self.medication_name=medication_name
        self.price_per_pill=price_per_pill
        self.pill_count=pill_count
    def __str__(self):
        return f"{self.medication_name} : {self.pill_count} pill(s) at ${self.price_per_pill}"
    def __repr__(self):
        return f"Prescription('{self.medication_name}', {self.price_per_pill}, {self.pill_count})"
    def __add__(self,other):
        if isinstance(other,Prescription):
            if self.medication_name==other.medication_name:
                new_prescription=Prescription(other.medication_name,
                                    other.price_per_pill,
                                    self.pill_count+other.pill_count,
                                    )
                return new_prescription
            return NotImplemented
        elif isinstance(other,int):
            return Prescription(
                self.medication_name,
                 self.price_per_pill,
                self.pill_count+other,
            )               
        return NotImplemented
    def __eq__(self,other):
        if isinstance(other,Prescription):
            return (self.medication_name==other.medication_name
                    and self.price_per_pill==other.price_per_pill
                    )

        return NotImplemented
    def __bool__(self):
        return self.pill_count>0
script1 = Prescription("Amoxicillin", 1.2, 30)
script2 = Prescription("Amoxicillin", 1.2, 15)
script3 = Prescription("Ibuprofen", 0.8, 0)

print(str(script1))
print(repr(script1))
print(script1 + script2)
print(script1 + 10)
print(script1 == script2)
print(bool(script1))
print(bool(script3))


class CargoTrain:
    def __init__(self,train_id:str):
        self.train_id=train_id
        self.cars=[]
    def add_car(self,weight):
        self.cars.append(weight)
    def __len__(self):
        return len(self.cars)
    def __str__(self):
        return f"Train {self.train_id} with {len(self)} cars "
    def __repr__(self):
        return f"CargoTrain('{self.train_id}')"
    def __add__(self,other):
        if isinstance(other,CargoTrain):
            train_id=f"{self.train_id}-{other.train_id}"
            new_train = CargoTrain(train_id)
            new_train.cars=self.cars+other.cars
            return new_train
        return NotImplemented
    def __eq__(self,other):
        if isinstance(other,CargoTrain):
            return sum(self.cars)==sum(other.cars)
    def __bool__(self):
        return len(self)>0

t1 = CargoTrain("Express")
t1.add_car(50)
t1.add_car(40)

t2 = CargoTrain("Local")
t2.add_car(30)
t2.add_car(60)

t4 = CargoTrain("Empty")

print(str(t1))
print(repr(t1))
print(len(t1))

t3 = t1 + t2
print(str(t3))
print(t3.cars)

print(t1 == t2)
print(bool(t1))
print(bool(t4))
    

