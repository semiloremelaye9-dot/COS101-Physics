#Physics Formulas 

# PHYSICS CALCULATOR
# Python Assignment

# 1. Function to calculate Speed
def calculate_speed():
    distance = float(input("Enter distance (metres): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed is:", speed, "m/s")


# 2. Function to calculate Force
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    force = mass * acceleration
    print("Force is:", force, "Newtons")


# 3. Function to calculate Density
def calculate_density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))

    if volume == 0:
        print("Volume cannot be zero.")
    else:
        density = mass / volume
        print("Density is:", density, "kg/m^3")


# 4. Function to calculate Work Done
def calculate_work():
    force = float(input("Enter force (Newtons): "))
    distance = float(input("Enter distance (metres): "))

    work = force * distance
    print("Work done is:", work, "Joules")


# 5. Function to calculate Kinetic Energy
def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    kinetic_energy = 0.5 * mass * velocity ** 2
    print("Kinetic Energy is:", kinetic_energy, "Joules")


# Main program
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Work Done")
    print("5. Kinetic Energy")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_work()

    elif choice == "5":
        calculate_kinetic_energy()

    else:
        print("Invalid choice. Please select between 1 and 5.")
        continue

    # Ask user whether to continue
    answer = input("\nDo you want to perform another calculation? (yes/no): ")

    if answer.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
