"""
Manages the operational details of a delivery truck, including its capacity, speed, and route progress. This class
encapsulates the functional aspects necessary for scheduling and tracking deliveries.

"""
# Initializes the truck with specified configurations and readies it for its delivery tasks.
class DeliveryTruck:
    def __init__(self, load_capacity, velocity, distance_traveled, position, leave_time, packages):
        """     
        Complexity:
            Time: O(1) - Assigning values to attributes is a constant time operation.
            Space: O(n) - The amount of space needed depends linearly on the number of packages loaded.
            Note:
                - Time: Each attribute assignment (load_capacity, velocity, etc.) happens in constant time.
                - Space: Space complexity primarily comes from the packages list, which scales with the number of packages.
        """
        # Initialize the delivery truck with specified attributes.
        self.load_capacity = load_capacity  # Maximum number of packages the truck can carry.
        self.velocity = velocity  # Speed of the truck in miles per hour.
        self.distance_traveled = distance_traveled  # Total distance the truck has covered.
        self.position = position  # Current location of the truck.
        self.leave_time = leave_time  # Time when the truck departs.
        self.clock = leave_time  # Tracks time during the truck's journey.
        self.packages = packages  # List of packages loaded on the truck.

# Provides a comprehensive textual description of the truck’s current status, including its speed,
# traveled distance, location, and the list of packages.
    def __str__(self):
        """        
        Complexity:
            Time: O(n) - The time to build the description scales with the number of packages.
            Space: O(n) - Space complexity grows with the length of the string, which depends on the number of packages.
            Note:
                - Time: Iterating over each package to form its description impacts the time complexity.
                - Space: The resulting string's size increases as more packages are described.
        """
        # Generate a descriptive status of the truck.
        package_details = ', '.join(str(package) for package in self.packages) # Format package details.
        status = (f"Velocity: {self.velocity} mph,\n"
                  f"Distance Traveled: {self.distance_traveled},\n"
                  f"Position: {self.position},\n"
                  f"Leave Time: {self.leave_time},\n"
                  f"Packages: [{package_details}]") # Compile the full status.
        return status # Return the compiled status.
