# Python Vehicle Information Dictionary Application

def main():
    vehicle_information_dictionary = {
        "Brand of the Car": input("Enter brand of the car: "),
        "Model of the Car": input("Enter model of the car: "), 
        "Year of the Car": input("Enter year of the car: "), 
        "Starting Odometer Reading": (input("Enter starting odometer reading: ")),
        "Ending Odometer Reading": (input("Enter ending odometer reading: ")),
        "estimated Miles_Per_Gallon": (input("Enter the estimated Miles Per Gallon of the car: "))
    }

    print("Vehicle Details:")
    for key, value in vehicle_information_dictionary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
