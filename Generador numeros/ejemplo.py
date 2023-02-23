import random

def generador(numeros):
    minimo = -10000000
    maximo = 10000000
    values = {}
    for i in range(numeros):
        values[i] = random.randint(minimo, maximo)
    with open("numeros.txt", "w") as file:
        for key, value in values.items():
            file.write(f"{key}\t{value}\n")

def ordenamiento():
    with open("numeros.txt", "r") as file:
        values = {}
        keys = []
        for line in file:
            key, value = line.strip().split("\t")
            values[int(key)] = int(value)
            keys.append(int(key))
        size = len(keys)
        gap = size // 2
        while gap > 0:
            for i in range(gap, size):
                temp = values[keys[i]]
                j = i
                while j >= gap and values[keys[j - gap]] > temp:
                    values[keys[j]] = values[keys[j - gap]]
                    j -= gap
                values[keys[j]] = temp
            gap //= 2
        with open("ordenados.txt", "w") as file:
            for key in keys:
                file.write(f"{key}\t{values[key]}\n")


def main():
    while True:
        menu = """
        Opciones
        1. Generar un millon de numeros.
        2. Ordenar los números generados.
        3. Salir
        """
        print(menu)
        op = int(input("Ingrese la opción que desea realizar: "))
        if op == 1:
            numeros = 1000000
            generador(numeros)
            print("\n Los números aleatorios han sido generados y almacenados en un archivo de texto. \n")
        elif op == 2:
            ordenamiento()
            print("\n Los números almacenados en el archivo de texto han sido ordenados y almacenados en un nuevo archivo. \n")
        elif op == 3:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
