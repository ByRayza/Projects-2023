# Python Cartesian Product Program

def main():

    from itertools import product

    user_input = input("Input the values for List A. Values inputted must be separated by spaces: ")
    A = [int(item) for item in user_input.split()]

    user_input = input("Input the values for List B. Values inputted must be separated by spaces: ")
    B = [int(item) for item in user_input.split()]

    AxB = list(product(A, B))

    print(f"AxB = {AxB}")

if __name__ == "__main__":
    main()

