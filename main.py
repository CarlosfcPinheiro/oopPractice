# Importing objects =============
from animal import Dog, Cat, Bird
from products import Ball, Scratcher, AnimalFood

# Main ================
def main():
    # Central config
    option = int(input(
        """       
        [1] Adopt pet
        [2] Buy products
        [3] Exit Petshop
        
        Enter an option: """
    ))
    
    match (option):
        case 1:
            addoptPet()
        case 2:
            BuyProducts()
        case 3:
            Exit()
        case _:
            TryAgain()


#while True:
while True:
    # Funcs ==============
    def addoptPet():
        Animal = int(input("""
        [1] Dog
        [2] Cat
        [3] Bird
        Enter an option: """))
        match (Animal):
            case 1:
                pet = Dog(
                    str(input("Pet's name: ")),
                    int(input("Pet's age: ")),
                    str(input("Pet's breed: "))
                )
            case 2:
                pet = Cat(
                    str(input("Pet's name: ")),
                    int(input("Pet's age: ")),
                    str(input("Pet's breed: "))
                )
            case 3:
                pet = Bird(
                    str(input("Pet's name: ")),
                    int(input("Pet's age: ")),
                    str(input("Pet's breed: "))
                )
            case _:
                pet = Dog(
                    str(input("Pet's name: ")),
                    int(input("Pet's age: ")),
                    str(input("Pet's breed: "))
                )
        print(pet.name)

    def BuyProducts():
        pass

    def Exit():
        print("Exiting from the petshop... Always times")
        pass

    def TryAgain():
        print('This option is not allowed.. Try again.')
        pass
    main()