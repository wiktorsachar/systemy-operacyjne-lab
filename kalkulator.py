import sys
def calculate(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Błąd: Podane argumenty nie są liczbami."

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        return "Błąd: Nieprawidłowa operacja. Dostępne operacje to + lub -."
if len(sys.argv) != 4:
    print("Użycie: python calc.py <liczba_1> <operacja: + lub -> <liczba_2>")
    sys.exit(1)
num1, operation, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
result = calculate(num1, operation, num2)

path = "/tmp/wynik.txt"
with open(path, "w") as file:
    file.write(f"Wynik: {result}\n")

