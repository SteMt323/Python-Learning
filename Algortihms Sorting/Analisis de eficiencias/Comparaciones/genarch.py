import random

def generar_random():
    with open("10k-random.txt", "w") as archivo:
        for _ in range(10000):
            numero = random.randint(1, 10000)
            archivo.write(f"{numero}\n")
            
    with open("1k-random.txt", "w") as archivo:
        for _ in range(1000):
            numero = random.randint(1, 1000)
            archivo.write(f"{numero}\n")
            
    with open("100-random.txt", "w") as archivo:
        for _ in range(100):
            numero = random.randint(1, 100)
            archivo.write(f"{numero}\n")

def generar_sorted():
    with open("10k-sorted.txt", "w") as archivo:
        for numero in range(1, 10001):
            archivo.write(f"{numero}\n")
            
    with open("1k-sorted.txt", "w") as archivo:
        for numero in range(1, 1001):
            archivo.write(f"{numero}\n")
            
    with open("100-sorted.txt", "w") as archivo:
        for numero in range(1, 101):
            archivo.write(f"{numero}\n")

def generar_reversed():
    with open("10k-reversed.txt", "w") as archivo:
        for numero in range(10000, 0, -1):
            archivo.write(f"{numero}\n")
            
    with open("1k-reversed.txt", "w") as archivo:
        for numero in range(1000, 0, -1):
            archivo.write(f"{numero}\n")
            
    with open("100-reversed.txt", "w") as archivo:
        for numero in range(100, 0, -1):
            archivo.write(f"{numero}\n")

def main():
    print("Generando archivos...")
    generar_random()
    generar_sorted()
    generar_reversed()
    print("¡Archivos generados con éxito!")

if __name__ == "__main__":
    main()
