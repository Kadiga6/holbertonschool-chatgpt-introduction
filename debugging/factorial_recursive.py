#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule la factorielle de n de manière récursive."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Fonction principale pour gérer l'entrée et afficher le résultat."""
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <non-negative integer>")
        return

    try:
        n = int(sys.argv[1])
        result = factorial(n)
        print(f"The factorial of {n} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("An unexpected error occurred.")

if __name__ == "__main__":
    main()

