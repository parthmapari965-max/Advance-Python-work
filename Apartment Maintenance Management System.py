class Resident:
    def __init__(self, name, flat_number, maintenance_fee, status):
        self.name = name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee
        self.status = status

    def display_details(self):
        print("Resident Name:", self.name)
        print("Flat Number:", self.flat_number)
        print("Maintenance Fee: Rs.", self.maintenance_fee)
        print("Payment Status:", self.status)
        print("-----------------------------")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self):
        name = input("Enter Resident Name: ")
        flat_number = input("Enter Flat Number: ")
        maintenance_fee = float(input("Enter Maintenance Fee: "))

        status = input("Enter Payment Status (Paid/Pending): ").capitalize()

        if status not in ["Paid", "Pending"]:
            print("Invalid Status! Please enter Paid or Pending.")
            return

        resident = Resident(name, flat_number, maintenance_fee, status)
        self.residents.append(resident)

        print("Resident Record Added Successfully!")

    def display_all_details(self):
        if not self.residents:
            print("No Resident Records Found!")
        else:
            print("\n===== Apartment Maintenance Details =====")
            for resident in self.residents:
                resident.display_details()


# Main Program
society = Society()

while True:
    print("\n===== Apartment Maintenance Management =====")
    print("1. Add Resident")
    print("2. Display All Maintenance Details")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        society.add_resident()

    elif choice == "2":
        society.display_all_details()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")