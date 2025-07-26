# Python Tax Withholding Calculator Application

def main():
    tax_brackets = {
        500: 0.10,
        1500: 0.15,
        2500: 0.20
    }

    def calculate_tax_withholding(income):
        if income <= 500:
            base_tax_rate = 0.10
        elif income <= 1500:
            base_tax_rate = 0.15
        elif income <= 2500:
            base_tax_rate = 0.20
        else:
            base_tax_rate = 0.30

        tax_withheld = income * base_tax_rate
        return tax_withheld, base_tax_rate

    income = float(input("Enter weekly income: "))

    tax_withheld, base_tax_rate = calculate_tax_withholding(income)

    print(f"Income: ${income}")
    print(f"Base Tax Rate: {base_tax_rate * 100}%")
    print(f"Tax Withheld: ${tax_withheld}")

if __name__ == "__main__":
    main()
