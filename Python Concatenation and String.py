# Python Concatenation and String Reversal Program

def main():

    def manipulate_strings(Firststring, Secondstring, Thirdstring):
        concatenated_string = f"{Firststring}{Secondstring}"
        reversed_string = Thirdstring[::-1]
        print(f"Reversed String: {reversed_string}")
        return concatenated_string


    Firststring = input("Enter the first string: ")
    Secondstring = input("Enter the second string: ")
    Thirdstring = input("Enter the third string: ")

    result = manipulate_strings(Firststring, Secondstring, Thirdstring)
    print(f"Concatenated String: {result}")

if __name__ == "__main__":
    main()
