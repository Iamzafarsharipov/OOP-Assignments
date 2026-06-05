class CocktailError(Exception):
    pass
class CocktailNotFoundError(CocktailError):
    def __init__(self,cocktail_name):
        self.cocktail_name=cocktail_name
        super().__init__(f"cocktail not found: {self.cocktail_name}")
class DuplicateCocktailError(CocktailError):
    def __init__(self,cocktail_name):
        self.cocktail_name=cocktail_name
        super().__init__(f"cocktail already exists: {self.cocktail_name}")
class InvalidServingsError(CocktailError):
    def __init__(self,servings):
        self.servings=servings
        super().__init__(f"invalid servings: {self.servings}. must be positive")
class MissingStockError(CocktailError):
    def __init__(self,cocktail_name,missing):
        self.cocktail_name=cocktail_name
        self.missing=missing
        super().__init__(f"cannot make {self.cocktail_name}: missing {self.missing}")
class CocktailMenu:
    def __init__(self):
        self.cocktails={}
    def add_cocktail(self,name,servings,ingredients):
        if name  in self.cocktails:
            raise DuplicateCocktailError(name)
        else:
            self.cocktails[name]={}
        if servings<0:
            raise InvalidServingsError(servings)
        else:
            self.cocktails[name]={"servings":servings, "ingredients":ingredients}
    def scale_cocktail(self,name,desired_servings):
        total=0
        try:
            cocktail=self.cocktails[name]
            if desired_servings<0:
                raise InvalidServingsError(desired_servings)
            else:
                cocktail[name]["servings"]+=desired_servings
            for ing,amount in cocktail[name]["ingredient"].items():
                total=round(amount*(desired_servings/cocktail[name]["servings"]),2)
            return total
        except KeyError:
            raise CocktailNotFoundError(name) from None
    def check_stock(self,name,bar_stock):
        possibe=False
        try:
            cocktail=self.cocktails[name]
            for ing,amount in bar_stock:
                if ing in cocktail[name]["ingredients"] and amount <= amount for ing,amount in cocktail[name]["ingredient"].items():
                    possibe=True
                else:
                    raise MissingStockError(name,bar_stock)
            return possibe
        except KeyError:
            raise 
menu = CocktailMenu()

menu.add_cocktail("Mojito", 2, {"rum": 3.0, "lime": 2.0, "mint": 1.0, "sugar": 0.5})
menu.add_cocktail("Margarita", 3, {"tequila": 4.5, "lime": 3.0, "salt": 0.75})

scaled = menu.scale_cocktail("Mojito", 6)
print(f"mojito for 6: {scaled}")

scaled = menu.scale_cocktail("Margarita", 1)
print(f"margarita for 1: {scaled}")

bar = {"rum": 3.0, "lime": 0.5, "mint": 1.0, "sugar": 0.5}
try:
    menu.check_stock("Mojito", bar)
except CocktailError as e:
    print(e)

bar2 = {"tequila": 10.0, "lime": 5.0, "salt": 2.0}
result = menu.check_stock("Margarita", bar2)
print(f"can make margarita: {result}")

tests = [
    lambda: menu.add_cocktail("Mojito", 2, {"rum": 1.0}),
    lambda: menu.scale_cocktail("Daiquiri", 4),
    lambda: menu.scale_cocktail("Mojito", -2),
]

for test in tests:
    try:
        test()
    except CocktailError as e:
        print(e)


    


            


        