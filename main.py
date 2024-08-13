# Importing objects =============
from animal import Dog, Cat, Bird
from products import Ball, Scratcher, Portion

# Main ================
def main():
    # Central config
    print("""
        WELCOME TO ANIMAL SHELTER
        [1] Adopt pet
        [2] Buy products
        [3] Exit""")
    
    ball = Ball(1, 12.5, 'red')
    print(ball.color)

#while True:
main()