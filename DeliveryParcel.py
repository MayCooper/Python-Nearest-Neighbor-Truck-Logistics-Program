"""
Manages a delivery parcel's journey from hub to destination. Ensures efficient, constant time (O(1))
performance for initializations and methods.

"""

import datetime

# Initializes a new parcel with all necessary delivery details, setting attributes based on provided parameters.
class DeliveryParcel:
    def __init__(self, parcel_id, address, city, state, zip_code, deadline, weight, status):
        """
        Complexity:
            Time: O(1) - Assigning input values to instance variables occurs in constant time.
            Space: O(1) - No additional space is utilized; the space is only used for the storage of input parameters as instance variables.
            Note:
                - The initialization involves direct assignment of parameters to attributes, which does not depend on any external factors.
        """
        self.parcel_id = parcel_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.time_left_hub = None  # Time when parcel leaves the hub, initially undefined.
        self.time_delivered = None  # Time when parcel gets delivered, initially undefined.
        self.assigned_truck = None  # Truck assigned for delivery, initially undefined.

# Constructs a readable string format of the DeliveryParcel details suitable for display or logging purposes.
    def __str__(self):
        """
        Complexity:
            Time: O(1) - The concatenation of fixed attribute values into a single string is a constant time operation.
            Space: O(1) - The space required is constant as it only involves returning a concatenated string of existing attribute values.
            Note:
                - The operation is performed irrespective of the number of parcels or their specific attributes, ensuring constant complexity.
        """
        return (f"Parcel ID {self.parcel_id} - Assigned Truck: {self.truck_number}, "
                f"Delivery Address: {self.address}, {self.city}, {self.state} {self.zip_code}, "
                f"Deadline: {self.deadline}, Weight: {self.weight}KG, Status: {self.status}, "
                f"Delivered At: {self.time_delivered if self.time_delivered else 'Not Delivered'}")

# Updates the status of the parcel based on the current time. This method handles status updates and address corrections.
    def update_delivery_status(self, current_time):
        """
        Complexity:
            Time: O(1) - The method executes a few conditions and updates in constant time.
            Space: O(1) - Uses existing attributes and parameters without needing extra space.
            Note:
                - The method includes fixed logic paths that do not increase in complexity regardless of the parcel's data or the number of parcels.
        """
        # Update package status based on current time relative to key event times.
        if self.time_delivered and self.time_delivered < current_time:
            self.status = "Delivered"  # Package has been delivered before current time.
        elif self.time_left_hub and current_time < self.time_left_hub:
            self.status = "At Hub"  # Package is still at the hub, has not left yet.
        elif self.time_left_hub and current_time > self.time_left_hub:
            self.status = "En Route"  # Package has left the hub and is on its way.


        # Special logic for address correction of parcel ID 9 after specific time.
        if self.parcel_id == 9:
            # Determine new or original address based on time comparison.
            special_update_time = datetime.timedelta(hours=10, minutes=20)
            new_address = "410 S State St, Salt Lake City, UT 84111"
            original_address = "300 State St, Salt Lake City, UT 84103"
            self.address = new_address if current_time > special_update_time else original_address
