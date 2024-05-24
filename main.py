# This script handles the logistics and routing of packages for the WGUPS service using custom data structures.

# Imports necessary libraries and modules for the program
from ResizableHashmap import ResizableDict
from DeliveryParcel import DeliveryParcel
from DeliveryTruck import DeliveryTruck
import csv
import datetime

# Reads CSV file data and converts it into a usable format, storing data for further operations.
# Complexity: Time O(n), Space O(n) — proportional to the number of records in the CSV.
def get_csv_data(filepath):
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)  # Time complexity: O(n), Space complexity: O(n)

# Loads the CSV data into memory for quick access during operations.
distance_data = get_csv_data("Distances.csv")  # Stores distance matrix
address_data = get_csv_data("Addresses.csv")  # Stores addresses and related data
package_data = get_csv_data("Packages.csv")    # Stores package details

# Loads package information into a hash map for efficient retrieval and update operations.
# Complexity: Time O(1) average per insert, Space O(n) — total space grows with number of packages.
def load_packages_file(file_path, package_hash_map):
    package_info = get_csv_data(file_path)  # Retrieves package data
    for row in package_info:
        # Parses and constructs a package object, then stores it in the hashmap
        parcel_id = int(row[0])
        address, delivery_city, delivery_state, delivery_zip_code = row[1:5]
        delivery_deadline, package_weight = row[5], float(row[6])
        delivery_status = "At Hub"
        package = DeliveryParcel(parcel_id, address, delivery_city, delivery_state,
                                 delivery_zip_code, delivery_deadline, package_weight, delivery_status)
        package_hash_map.put(parcel_id, package)  # Time complexity: O(1) average, Space complexity: O(1) per package

# Initialize the hashmap with an initial capacity for package storage
package_hash_map = ResizableDict(capacity=40)
load_packages_file('Packages.csv', package_hash_map)

# Calculates the distance between two addresses using their indices in the distance matrix.
# Complexity: Time O(1), Space O(1) — direct retrieval from a two-dimensional list.
def distance_between(address_index1, address_index2):
    # Retrieves distance from matrix, handling potential non-symmetric entries
    distance = distance_data[address_index1][address_index2] or distance_data[address_index2][address_index1]
    return float(distance)

# Retrieves the index of an address in the address list for distance calculations.
# Complexity: Time O(n), Space O(1) — linear search through the address list.
def get_address(address_name):
    for row in address_data:
        if address_name in row[2]:  
            return int(row[0])
    print(f"Address not found: {address_name}") 
    return None  

# Simulates the delivery process by a truck, optimizing route based on distances.
# Complexity: Time O(n^2), Space O(n) — involves complex route calculation and updating the truck's state.
def deliver_packages(truck):
    # Retrieve undelivered packages using their IDs.
    not_delivered = [package_hash_map.get(packageID) for packageID in truck.packages]
    current_location = "HUB"  # Start at the hub.
    current_location_index = get_address(current_location)  # Index for current location.

    # Set initial departure time for each package.
    for package in not_delivered:
        package.time_left_hub = truck.clock

    # Process delivery until all packages are delivered.
    while not_delivered:
        # Select the nearest package to deliver next.
        next_package = min(not_delivered, key=lambda package: distance_between(current_location_index, get_address(package.address)))
        next_nearest_distance = distance_between(current_location_index, get_address(next_package.address))
        
        # Update truck's travel distance and package's delivery status.
        truck.distance_traveled += next_nearest_distance
        next_package.status = "Delivered"
        next_package.time_delivered = truck.clock + datetime.timedelta(hours=next_nearest_distance / 18)

        # Move truck to new location and update time.
        current_location = next_package.address
        current_location_index = get_address(current_location)
        truck.clock += datetime.timedelta(hours=next_nearest_distance / 18)
        
        # Remove delivered package from the list.
        not_delivered.remove(next_package)

# Initialize three delivery trucks with capacity, speed, starting location, and assigned packages.
Truck1 = DeliveryTruck(16, 18, 0.0, "HUB", datetime.timedelta(hours=8), [8, 13, 14, 15, 16, 19, 20, 21, 27, 30, 34, 35, 37, 39])
Truck2 = DeliveryTruck(16, 18, 0.0, "HUB", datetime.timedelta(hours=10, minutes=20), [3, 5, 9, 10, 11, 12, 17, 18, 23, 28, 36, 38])
Truck3 = DeliveryTruck(16, 18, 0.0, "HUB", datetime.timedelta(hours=9, minutes=5), [1, 2, 4, 6, 7, 22, 24, 25, 26, 29, 31, 32, 33, 40])

# Assigns packages to specific trucks for delivery.
# Complexity: Time O(p), Space O(1) — where p is the number of packages on the truck.
def assign_packages_to_truck(truck, truck_number):
    for parcel_id in truck.packages:
        package = package_hash_map.get(parcel_id)
        if package:
            package.truck_number = f"Truck #{truck_number}"

# Assign packages to trucks and initiate the delivery process
assign_packages_to_truck(Truck1, 1)  # Load Truck1 with its packages.
assign_packages_to_truck(Truck2, 2)  # Load Truck2 with its packages.
assign_packages_to_truck(Truck3, 3)  # Load Truck3 with its packages.

deliver_packages(Truck1)  # Start delivery for Truck1.
deliver_packages(Truck2)  # Start delivery for Truck2.

# Set Truck3's leave time based on the earliest return of Truck1 or Truck2.
Truck3.leave_time = min(Truck1.clock, Truck2.clock)
deliver_packages(Truck3)  # Start delivery for Truck3 after the first two trucks.

# Main user interface function for the delivery management system
def main_user_interface():
    print("WGUPS Delivery Management System")
    total_mileage = sum(truck.distance_traveled for truck in [Truck1, Truck2, Truck3])
    print(f"Total mileage traveled by all trucks: {total_mileage} miles")
    initiate_tracking_process()

def initiate_tracking_process():
    choice = input("Type 'begin' to start tracking, or any other key to exit: ").lower()
    if choice == "begin":
        user_time_input()
    else:
        print("Exiting program.")
        exit()

def user_time_input():
    try:
        user_time = input("Enter the time (HH:MM) to check the package status: ")
        hours, minutes = map(int, user_time.split(':'))
        current_time = datetime.timedelta(hours=hours, minutes=minutes)
        package_status_input(current_time)
    except ValueError:
        print("Input error: Please enter a valid time format (HH:MM).")
        user_time_input()  # Recursive call for correct time input

def package_status_input(current_time):
    choice = input("Enter 'single' to track one package or 'all' for a general status report: ").lower()
    if choice == "single":
        single_package_input(current_time)
    elif choice == "all":
        all_packages_status(current_time)
    else:
        print("Exiting. Please enter a valid option next time.")
        exit()

def single_package_input(current_time):
    try:
        package_id = int(input("Enter the package ID for status update: "))
        package = package_hash_map.get(package_id)
        if package:
            package.update_delivery_status(current_time)
            print(package)
        else:
            print(f"No package found with ID: {package_id}")
    except ValueError:
        print("Invalid input: Please enter a numeric package ID.")
        single_package_input(current_time)  # Recursive call for correct input

def all_packages_status(current_time):
    # Complexity: Time O(n), Space O(1) — Iterates over all packages for status update.
    for parcel_id in range(1, package_hash_map.count() + 1):
        package = package_hash_map.get(parcel_id)
        if package:
            package.update_delivery_status(current_time)
            print(package)

# Entry point for the program
if __name__ == "__main__":
    main_user_interface()
