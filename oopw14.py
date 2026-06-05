# class Ledger:
#     def __init__(self):
#         self.entries=[]
#     def log(self,text):
#         self.entries.append(text)
#         print(f"# {text}")


# class Logger:
#     _instance = None  # class variable, shared by all

#     def __new__(cls):
#         if cls._instance is None:
#             print("Creating the one and only Logger")
#             cls._instance = super().__new__(cls)
#             cls._instance.logs = []
#         return cls._instance

#     def log(self, message):
#         self.logs.append(message)
#         print(f"[LOG] {message}")

# logger_a = Logger()   # Creating the one and only Logger
# logger_b = Logger()   # nothing prints, returns same object

# logger_a.log("Hello")
# logger_b.log("World")

# print(logger_a is logger_b)   # True
# print(logger_a.logs)          # ['Hello', 'World']

# class DatabaseConnection:
#     _instance = None  # This holds our single copy

#     def __new__(cls, *args, **kwargs):
#         # If no copy exists yet, create it
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# # --- Testing it out ---
# conn1 = DatabaseConnection()
# conn2 = DatabaseConnection()

# print(conn1 is conn2)  # Output: True (They are the exact same object in memory!)
# from abc import abstractmethod,ABC
# class Subscriber(ABC):
#     @abstractmethod
#     def update(self, video_title: str): pass

# class User(Subscriber):
#     def __init__(self, name: str):
#         self.name = name
        
#     def update(self, video_title: str):
#         print(f"Hey {self.name}, a new video is out: '{video_title}'")

# class YouTubeChannel:
#     def __init__(self):
#         self._subscribers = []  # List of observers

#     def subscribe(self, subscriber: Subscriber):
#         self._subscribers.append(subscriber)

#     def upload_video(self, title: str):
#         print(f"\nChannel uploaded: {title}")
#         # Notify everyone automatically
#         for sub in self._subscribers:
#             sub.update(title)

# # --- Testing it out ---
# channel = YouTubeChannel()
# peter = User("Peter")
# bruce = User("Bruce")

# channel.subscribe(peter)
# channel.subscribe(bruce)

# channel.upload_video("Design Patterns For Beginners!")

# class IDGenerator:
#     _instance=None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance=super().__new__(cls)
#             cls._instance.current=0
#         return cls._instance
#     def next_id(self):
#         self.current+=1
#         return self.current
# users_gen=IDGenerator()
# orders_gen=IDGenerator()
# messages_gen=IDGenerator()
# print(f"User ID: {users_gen.next_id()}")
# print(f"User ID: {users_gen.next_id()}")
# print(f"Order ID: {orders_gen.next_id()}")
# print(f"User ID: {users_gen.next_id()}")
# print(f"Message ID: {messages_gen.next_id()}")
# print(f"Order ID: {orders_gen.next_id()}")

from enum import Enum
from abc import abstractmethod,ABC
class DrinkType(Enum):
    COFFEE="COFFEE"
    TEA="TEA"
    JUICE="JUICE"

class Drink(ABC):
    def __init__(self,size):
        self.size=size
    @abstractmethod
    def prepare(self):
        pass
class Coffee(Drink):
    def prepare(self):
        print(f"Brewing {self.size} coffee ☕")
class Tea(Drink):
    def prepare(self):
        print(f"Steeping {self.size} tea 🍵")
class Juice(Drink):
    def prepare(self):
        print(f"Squeezing {self.size} juice 🧃")
class DrinkFactory:
    _types={
        DrinkType.COFFEE: Coffee,
        DrinkType.TEA: Tea,
        DrinkType.JUICE: Juice
    }
    @staticmethod
    def create(kind: DrinkType,size:str):
        if kind not in DrinkFactory._types:
            raise ValueError(f"Unknown drink: {kind}")
        # for drink  in cls._types:
        #     print(drink.get(kind).prepare(size))
        drink_class=DrinkFactory._types[kind]
        return drink_class(size)

orders = [
    (DrinkType.COFFEE, "large"),
    (DrinkType.TEA, "small"),
    (DrinkType.JUICE, "medium"),
    (DrinkType.COFFEE, "small"),
]

for kind, size in orders:
    drink = DrinkFactory.create(kind, size)
    drink.prepare()
