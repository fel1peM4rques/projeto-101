import random

while True:
    response = input("Você deseja jogar um dado? (y/n): ")
    if response.lower() == 'n':
        print("Saindo...")
        break
    else:
        no = random.randint(1, 6)
        print("Você jogou o dado e obteve: ", end="")
        for i in range(no):
            print("*", end="")
        print()