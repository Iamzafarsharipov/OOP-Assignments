#problem 1
from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    pages:int

b1=Book("Atomic Habits","James Clear", 260)
b2=Book("Atomic Habits","James Clear", 260)
print(b1)
print(b1==b2)
#problem2
from dataclasses import dataclass,field
@dataclass
class CoffeeOrder:
    drink:str
    customer:str
    size:str=field(default="Medium")
    price:float=field(default=3.5)
o1 = CoffeeOrder("Latte", "Paul", "Large", 4.75)
o2 = CoffeeOrder("Espresso", "Chani")
print(o1)
print(o2)
#problem 3
from dataclasses import dataclass,field
@dataclass
class CargoCrate:
    crate_id:str
    destination:str
    max_weight:str
    items:list=field(default_factory=list[tuple[str,float]])
    def total_weight(self)->float:
        all_weight=0
        # for item in self.items:
        for name,weight in self.items:
            all_weight+=weight
        return all_weight
    def add_item(self,name:str,weight:float)->bool:
        if self.total_weight()+weight<=self.max_weight:
            self.items.append((name,weight))
            return True
        return False
    def manifest(self):
        print(f"{self.crate_id} -> {self.destination}")
        # for item in self.items:
        for name,weight in self.items:
            print(f"  - {name}: {weight}kg")
        print(f"Total: {self.total_weight()}/{self.max_weight}")
c = CargoCrate("CR-401", "Arrakis", 50.0)
print(c.add_item("Stillsuit", 8.5))
print(c.add_item("Spice Melange", 28.0))
print(c.add_item("Shield Generator", 5.0))
print(c.total_weight())
c.manifest()
#problem 4
from dataclasses import dataclass,field
@dataclass
class TrainingSession:
    trainee:str
    discipline:str
    scores:list[int]=field(default_factory=list)
    average:float=field(init=False)
    rank:str=field(init=False)
    def __post_init__(self):
        self.average=self.average_calculator()
        self.rank=self.assign_rank()

    
    def average_calculator(self):
        if len(self.scores)!=0:
            return sum(self.scores)/len(self.scores)
        else:
            return 0.0
    def assign_rank(self):
        if self.average>=90:
            self.rank="Elite"
        elif self.average>=70:
            self.rank="Skilled"
        else:
            self.rank="Novice"  
        return self.rank

      
    def add_score(self,score:int):
        self.scores.append(score)
        self.average=self.average_calculator()
    def outperforms(self,other:'TrainingSession')->bool:
        if isinstance(other,TrainingSession):
            return  self.average>=other.average
        return NotImplemented
t1 = TrainingSession("Duncan", "Swordsmanship", [85, 92, 78])
print(t1)
t1.add_score(95)
print(t1.average)
print(t1.rank)

t2 = TrainingSession("Feyd", "Swordsmanship", [95, 90, 98])
print(t2.rank)
print(t1.outperforms(t2))

t3 = TrainingSession("Rabban", "Swordsmanship")
print(t3.rank)



