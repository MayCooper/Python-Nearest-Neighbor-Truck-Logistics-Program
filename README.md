# Python-Nearest-Neighbor-Truck-Logistics-Program
The Python Logistics Planner optimizes routing for a delivery service using the Nearest Neighbor Algorithm and a dynamic hash table. This solution minimizes travel distances and adapts to real-time changes, ensuring efficient and timely deliveries. Built in Python, the program features a modular design for scalability and easy maintenance.

<h2>A.	Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.</h2>

I chose the Nearest Neighbor Algorithm for the Routing Program for its straightforward method that focuses on minimizing travel distances between delivery points. Starting from a central hub, the algorithm efficiently selects the nearest unvisited destination, ensuring routes are planned both logically and efficiently. This approach is not only easy to implement but also highly adaptable to dynamic routing changes, such as varying delivery deadlines and special handling requirements. In the implementation within my deliver_packages function, the algorithm considers the current location of the truck and the destination of each undelivered package, utilizing the distance_between function to determine the shortest path. This significantly optimizes route efficiency, crucial given the constraints of delivering all packages within a limited timeframe and under specific mileage.

Moreover, the Nearest Neighbor Algorithm's integration with real-time updates to the truck's state—adjusting the truck's position, the distance traveled, and the delivery time after each stop—ensures the routing dynamically adapts to the ongoing delivery scenario. This dynamic adaptability is vital for maintaining operational efficiency and meeting stringent delivery constraints, such as ensuring that Truck #3 starts its route only after one of the other trucks has completed its deliveries. 

My application of this method balances simplicity in execution with the ability to handle the complex logistical challenges of package delivery, demonstrating a robust application of theoretical algorithms to practical, real-world challenges in our delivery logistics domain (Programming Pearls [2nd Edition]   0201657880 - DOKUMEN.PUB, n.d.).


<h2>B.	Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data</h2>

I have identified a self-adjusting data structure called the "ResizableDict," which is an implementation of a dynamic hash table or hash map. This data structure is particularly suited for use with the package delivery routing algorithm described in the program. The hash table facilitates efficient retrieval and update of package data, which is crucial for the dynamic delivery scheduling and tracking tasks of the delivery service.
1)	Explain how your data structure accounts for the relationship between the data components you are storing.
In the Routing Program, I have implemented a Resizable Hash Table combined with the Nearest Neighbor Algorithm to efficiently manage and retrieve package data. This structure supports effective storage and quick retrieval of package details, which are essential for optimizing delivery routes.
Data Structure Overview:
Key-Value Pairing: The hash table uses package IDs as unique keys and associates them with corresponding package details (delivery address, deadline, weight, and status) stored as values. This setup ensures that all related data for each package is aggregated and quickly accessible, crucial for making routing decisions.
Handling Collisions: To maintain data integrity and ensure accessibility, I employ chaining to resolve collisions within the hash table. Each bucket in the table starts as an empty list, ready to store multiple entries if multiple keys hash to the same index. This approach ensures that the data for each package remains distinct and complete, preserving the accuracy and availability of package information.

Big O Notation for Hash Table Operations:

Insertion, Deletion, and Lookup: These operations typically run in O(1) time, contributing to the efficiency of the hash table. In scenarios where many keys hash to the same index—resulting in longer chains—these operations could degrade to O(n), although this is mitigated by the dynamic resizing of the hash table.

Dynamic Adjustability:

The hash table supports dynamic updates crucial for the real-time nature of delivery logistics. For instance, if a package's delivery status changes or an address needs to be updated, the relevant entry can be quickly located using the package ID and adjusted as needed. This adaptability is pivotal for managing deliveries and adjusting routes based on real-time conditions.
Pseudocode for Using Hash Table with Nearest Neighbor Algorithm:
function initializeHashmap():
    create hashmap
    for each package in package list:
        insert package into hashmap using packageID as key

function nearestNeighbor(currentLocation, hashmap):
    nearestPackage = null
    shortestDistance = infinity
    for each packageID in hashmap:
        package = hashmap.get(packageID)
        if not package.delivered:
            distance = calculateDistance(currentLocation, package.address)
            if distance < shortestDistance:
                shortestDistance = distance
                nearestPackage = package
    return nearestPackage

function deliverPackages():
    currentLocation = hub
    while packages remain undelivered:
        nearestPackage = nearestNeighbor(currentLocation, packageHashmap)
        deliver package(nearestPackage)
        update currentLocation to nearestPackage.address
        mark nearestPackage as delivered in hashmap

Scalability and Adaptability:
The hash table is engineered to scale efficiently with the addition of more packages. As the load factor increases, the table resizes to maintain operational efficiency. Chaining as a collision resolution method ensures that even with a high number of entries, the system can swiftly retrieve and update package information, adapting to changes such as route modifications or urgent delivery needs.
Conclusion:
This setup makes the hash table a robust structure for storing package data and aligns perfectly with the operational demands of the Nearest Neighbor Algorithm. Quick access to detailed package information enables the algorithm to efficiently plan and adjust routes, ensuring timely deliveries under varying logistical constraints (Book Details - MIT Press, 2024). The integration of this data structure with the routing algorithm demonstrates a high level of competence in handling the complexities of real-world package delivery systems .
C.	Write an overview of your program in which you do the following:
1.	Explain the algorithm’s logic using pseudocode.

Algorithm: SimulateDeliveryProcess(trucks)
Input: List of delivery trucks

1. InitializeHashMap(package_hash_map):
   - Create a resizable hashmap to store package information.

2. ReadPackageDataFromCSVFiles(package_hash_map):
   - Read package data from CSV files (Packages.csv) and load it into the hashmap.
   - Each package is stored with its unique ID as the key and package details as the value.

3. InitializeTrucks(trucks):
   - Initialize delivery trucks with their characteristics such as capacity, speed, starting location, leave time, and assigned packages.

4. AssignPackagesToTrucks(trucks):
   - Assign packages to trucks for delivery based on predetermined assignments.

5. For each truck in trucks:
   5.1. RetrieveUndeliveredPackages(truck):
       - Retrieve undelivered packages for the current truck from the hashmap.
   5.2. SetInitialDepartureTimeForPackages(truck):
       - Set initial departure time for each package on the truck.
   5.3. While there are undelivered packages on the truck:
       5.3.1. FindNextPackageToDeliver(truck):
           - Select the nearest undelivered package to deliver next based on distance.
       5.3.2. UpdateTruckAndPackage(truck, next_package):
           - Update truck's travel distance and package's delivery status.
           - Calculate travel time to the next package's location.
           - Move the truck to the next package's location.
           - Update package status to "Delivered" and set delivery time.
           - Remove delivered package from the list of undelivered packages.
   5.4. UpdateTruckLeaveTime(truck):
       - Update truck's leave time based on the time it returns after delivering all packages.

6. CalculateTotalMileage(trucks):
   - Sum up the distance traveled by each truck to get the total mileage traveled by all trucks.

7. ProvideUserInterfaceForPackageTracking():
   - Display the main menu of the delivery management system.
   - Prompt the user to begin tracking package status.
   - If the user chooses to track:
       - Prompt user to enter time (HH:MM) for package status update.
       - Based on user input, track single package or provide general status report for all packages.

End of Algorithm


<h2>2.	Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.</h2>

Specs:
Computer: ASUS Custom-Built PC 
Memory: 32 GB RAM
Processor: Intel(R) Core(TM) i7-10700 CPU @ 2.90GHz, 2904 Mhz, 8 Core(s), 16 Logical Processor(s)
Operating System: Microsoft Windows 11 Pro
Programming Language: Python 3.13
IDE: VS Code

<h2>3.	Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.</h2>

<h3>Main.py</h3>

CSV Data Loading (get_csv_data function)
Time Complexity: O(n) where n is the number of records in the CSV file. Each record is read sequentially.
Space Complexity: O(n) as the data is stored in a list, consuming space proportional to the number of records.
Loading Packages into Hash Map (load_packages_file function)
Time Complexity: O(n) for reading and inserting n package records into the hash map. Although the average time complexity for each insert is O(1), reading n records results in a linear time complexity.
Space Complexity: O(n) as each package object is stored in the hash map.
Distance Calculations (distance_between function)
Time Complexity: O(1) since the distance retrieval from a pre-loaded two-dimensional list is a direct access operation.
Space Complexity: O(1) as no additional space is required for performing this operation.
Address Index Retrieval (get_address function)
Time Complexity: O(n) where n is the number of addresses. The function performs a linear search through the address list.
Space Complexity: O(1) as the operation does not allocate additional space proportional to the input size.
Package Delivery Simulation (deliver_packages function)
Time Complexity: O(n^2) as it involves finding the nearest package for each undelivered package, which includes a nested operation of finding the minimum distance which itself iterates over the list of packages.
Space Complexity: O(n) due to storing the list of not_delivered packages.

<h3>Truck and Package Management</h3>

Time Complexity: O(p) where p is the number of packages on a truck during the assignment of packages to trucks. Each assignment is O(1), and this is done for each package.
Space Complexity: O(1) as the operation modifies existing objects without allocating new proportional space.
User Interface Functions (main_user_interface, initiate_tracking_process, etc.)
Time Complexity: Varies; most operations are O(1), except for package status updates which are O(n) where n is the number of packages.
Space Complexity: Generally O(1), except where package data is iteratively accessed or modified, still using existing data structures without new allocations.

<h3>DeliveryParcel.py</h3>

Initialization and Status Updates

Time Complexity: O(1) for both initialization and status update methods as these involve direct assignments and condition checks.
Space Complexity: O(1) as no additional space is used beyond what is necessary for storing instance variables.
ResizableHashmap.py

Hash Table Operations (put, get, remove, _resize)
Time Complexity:
put: Average O(1), worst O(n) when resizing is needed.
get: Average O(1), worst O(n) in case of many collisions.
remove: Average O(1), worst O(n) similar to get.
_resize: O(n) as it rehashes all elements to new buckets.
Space Complexity:
All operations are O(1) in space except for _resize, which temporarily requires additional space but this is managed within the method.

<h3>DeliveryTruck.py</h3>

Initialization and String Representation
Time Complexity: O(1) for initialization; O(n) for string representation where n is the number of packages due to iterating over packages.
Space Complexity: O(n) for both, as space depends on the number of packages handled.
Overall Program Complexity
•	Time Complexity: The most time-consuming operations involve package delivery simulation and user interface functions which handle package data iteratively. Hence, the overall time complexity could be considered O(n^2) due to the quadratic behavior in the delivery simulation.
•	Space Complexity: The program primarily stores data in structures proportional to the number of packages and addresses, resulting in an overall space complexity of O(n), where n is the sum of packages and address data points.
4.	Explain the capability of your solution to scale and adapt to a growing number of packages.

<h2>Scalability</h2>

Resizable Hash Map (ResizableDict):

•	The ResizableDict is a central feature designed to handle a growing number of packages efficiently. As the number of packages increases, the hash map automatically increases its capacity to maintain a low load factor, which is crucial for keeping the average time complexity for operations like insertions, deletions, and retrievals at O(1). This dynamic resizing helps avoid performance degradation due to excessive collisions, which typically occur in hash tables as they fill up.
•	The resizing operation itself is O(n), as it involves rehashing all entries into a new, larger bucket array. However, because resizing happens progressively less frequently as the size grows (doubling the capacity each time), the average cost of insertions (including occasional resizing) remains amortized constant.
Efficient Data Retrieval and Update:
•	Using a hash map ensures that accessing and updating package information, such as status or location updates, is efficient. This allows the system to manage more packages without significantly impacting the response time for queries, which is essential in a real-time delivery tracking context.
Adaptability

<h2>Modular Design:</h2>

•	The program's modular design, with separate components for managing package data (DeliveryParcel), routing and delivery simulation (deliver_packages), and truck management (DeliveryTruck), facilitates adaptability. This modular architecture allows individual components to be modified or replaced as requirements evolve, without extensive reworking of the entire system.
Dynamic Routing and Delivery Management:
•	The delivery simulation (deliver_packages) adapts to the real-time status of deliveries, including changes in package priorities or delivery routes. The algorithm's ability to dynamically select the next nearest package for delivery means the routing logic can adapt on-the-fly to changes such as traffic conditions or priority updates.
User Interaction and Real-time Updates:
•	The user interface functions, which provide real-time updates on package status and facilitate user interactions, are designed to handle varying loads and can be easily extended to include more features such as predictive delivery times, alternative routing options, or customer notifications.

<h2>General Considerations</h2>

Handling Increased Load:
•	The system's current implementation should handle moderate increases in package volume effectively. However, for significant scale-ups, additional considerations like distributed computing resources, more sophisticated routing algorithms (e.g., using machine learning for predictive analysis), and enhanced data synchronization across multiple locations would be necessary to maintain performance.
Potential Bottlenecks:
•	While the hash map handles package data efficiently, the O(n^2) complexity of the package delivery simulation could become a bottleneck as the number of packages grows very large. Exploring more advanced algorithms that can provide near-optimal solutions with lower complexity, such as using approximate or heuristic methods like Genetic Algorithms, Simulated Annealing, or Ant Colony Optimization, could be beneficial.
•	Overall, the current design balances efficiency and adaptability well for a growing number of packages but would require further enhancements to handle large-scale operations typical of major logistics and courier companies.

<h2>5.	Discuss why the software design would be efficient and easy to maintain.</h2>

Software Efficiency
Use of a Resizable Hash Map:
•	The implementation of a ResizableDict for managing package data significantly enhances efficiency. By dynamically resizing based on the load factor, it ensures that the hash table maintains a balance between space and time efficiency, keeping average access, insertion, and deletion times close to O(1). This is crucial for high-performance scenarios where quick data retrieval and update are essential.
Optimized Data Access Patterns:
•	The software design strategically utilizes data structures such as lists and hash maps to optimize access patterns. For example, packages are accessed via their unique IDs using the hash map, ensuring constant-time complexity on average for queries. This leads to fast response times even as the number of packages grows.
Modular Function Design:
•	Functions like get_csv_data, load_packages_file, and deliver_packages are clearly defined with specific roles, reducing dependencies between components of the software. This separation of concerns not only makes the system more efficient by isolating changes to individual modules but also enhances performance by allowing focused optimizations.
Easy Maintenance
Clear Separation of Concerns:
•	The program structure is divided into distinct modules (ResizableHashmap.py, DeliveryParcel.py, DeliveryTruck.py, and Main.py), each handling a specific aspect of the application. This separation simplifies understanding the system as a whole, making it easier for developers to identify where changes should be made without unintended side effects on other parts of the system.
Self-Documenting and Descriptive Code:
•	The codebase includes extensive comments and documentation, particularly explaining the purpose of each function and class, the expected input and output, and the complexity of operations. This level of documentation facilitates easier onboarding of new developers and assists in maintaining the code, as the intended design and functionality are clearly communicated.
Scalable and Extendable Architecture:
•	The software's architecture is designed to be scalable, as seen with the use of a dynamic hash map and adaptable routing logic. New functionalities, such as adding different types of deliveries or support for new types of routing algorithms, can be integrated with minimal changes to the existing system. The object-oriented design allows for easy extension of classes and functionality.
Testability:
•	Each module and function is designed to be self-contained, which enhances testability. Unit tests can be easily written and executed for individual components without the need for complex setup or dependencies. This modularity in design supports continuous integration and deployment practices, ensuring that changes can be tested and deployed with confidence.
Error Handling and Robustness:
•	The program includes basic error handling and validation, particularly in user input and file reading operations, which contributes to the overall robustness of the application. Enhancing this aspect with more comprehensive error management and recovery strategies could further improve maintainability.
Overall, the software design of the Routing Program combines efficiency with maintainability through thoughtful architecture, data structure choices, and coding practices. This not only facilitates current operational requirements but also lays a foundation for future enhancements and scalability.

<h2>6.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).</h2>

<h3>Strengths</h3>

Dynamic Resizing:

1.	I find one of the key strengths of the ResizableDict to be its ability to dynamically adjust its size based on the load factor. This ensures that the hash table remains efficient in terms of access, insertion, and deletion operations even as the number of elements grows. By maintaining a balance between the number of elements and the bucket size, it significantly reduces the likelihood of hash collisions, which can degrade performance.
Efficient Access Times:
2.	The hash table provides average O(1) time complexity for access, insert, and delete operations under typical conditions. This efficiency is crucial for real-time applications where quick data retrieval and updates are essential. For example, in the package delivery system I've developed, the status of deliveries needs to be updated and queried frequently, making this characteristic extremely valuable.
Scalability:
3.	As the hash table automatically resizes, it can handle growth in data smoothly without significant manual adjustments in the underlying data structure. This scalability is advantageous for applications that experience varying loads or need to scale up to accommodate more data over time.
Space Efficiency:
4.	While resizing increases capacity, the hash table only uses space proportional to the number of entries it contains, ensuring that space is not wasted. This space efficiency is critical in environments where memory resources may be constrained.
Weaknesses

<h2>Cost of Resizing:</h2>

1.	While resizing helps maintain operational efficiency, the resizing operation itself can be costly. It involves rehashing all existing elements into new buckets, which has a time complexity of O(n). During the resizing process, there can be a temporary performance hit, which might affect system responsiveness, especially if the hash table is very large.
Worst-Case Time Complexity:
2.	In the worst case, where many elements hash to the same bucket (high collision scenario), the time complexity for access and update operations can degrade to O(n). While this scenario is less likely with a good hash function and proper load management, it is still a potential weakness that can impact performance under certain conditions.
Complexity in Concurrency:
3.	Managing concurrency in a hash table can be challenging, especially during resizing operations. Synchronization mechanisms are necessary to ensure data consistency, which can complicate the implementation and may reduce performance in multi-threaded environments.
Dependence on Hash Function:
4.	The performance of the hash table heavily depends on the quality of the hash function used. A poor hash function can lead to increased collisions, undermining the efficiency advantages of the hash table. Ensuring a uniform distribution of hash values is critical but can be challenging depending on the data characteristics.
Handling of Large Data Values:
5.	If the data elements stored in the hash table are large, the resizing operation can become more resource-intensive, both in terms of time and memory usage. This can be a drawback in systems where data payloads are substantial.
In summary, the ResizableDict in my Routing Program offers significant strengths in terms of scalability, efficiency, and dynamic sizing, making it well-suited for the program’s needs. However, I am always mindful of its weaknesses, especially regarding performance under high collision conditions and during resizing, to optimize its use and ensure robust system performance.

<h2>7.  Justify the choice of a key for efficient delivery management from the following components:</h2>
   
•	delivery address
•	delivery deadline
•	delivery city
•	delivery zip code
•	package ID
•	package weight
•	delivery status (i.e., at the hub, en route, or delivered), including the delivery time

<h2>Uniqueness:</h2>

1.	The package ID is unique to each package, which eliminates the possibility of key collisions within the data storage system. This uniqueness ensures that each query or update operation targets precisely the intended package without confusion or error.
Efficiency in Access and Updates:
2.	Using package ID as the key allows for constant-time complexity (O(1) on average) for accessing, updating, or deleting package information in the hash map (ResizableDict). This is because hash tables provide extremely fast access to elements when the keys distribute uniformly, as they do with unique identifiers like package IDs.
Integration with Other System Operations:
3.	Package ID serves as a straightforward reference that can be used across various components of the system, such as during the loading and unloading of packages onto trucks, during the tracking of packages, and when updating delivery status. This integration simplifies the system’s architecture by reducing the need for complex joins or searches across different attributes.
Independence from Variable Data:
4.	Other potential keys such as delivery address, deadline, or status could change over the lifecycle of a delivery (e.g., a change in delivery address due to customer request or an update in status as it moves from "at the hub" to "delivered"). Using a mutable attribute as a key could complicate the management of data integrity and consistency. In contrast, package ID is immutable – once assigned, it does not change, which makes it ideal for stable and reliable indexing.
Irrelevance of Other Attributes to Indexing Efficiency:
5.	Attributes like delivery address, city, zip code, and deadline are important for sorting and routing decisions but are not efficient for quick data retrieval as keys because they are not unique and can be shared by multiple packages, potentially leading to inefficiencies and the need for further filtering.
6.	Package weight and delivery status, including time, are attributes subject to frequent updates and thus are unsuitable for use as primary keys. Their use as keys would lead to inefficiencies in rehashing or reindexing the data as these values change.

<h2>Summary</h2>

Choosing package ID as the key for managing package data within the Routing Program offers significant advantages in terms of data access speed, system simplicity, and maintenance. It supports efficient operations across the system's lifecycle, from package intake through delivery. This choice aligns with the principles of effective database and hash map design by leveraging the inherent properties of uniqueness and immutability, which are critical for ensuring robust and efficient data handling in dynamic and complex delivery systems like the Routing Program (Art of Computer Programming, the: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada, n.d.).


D.	Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

Programming Pearls [2nd edition]   0201657880 - DOKUMEN.PUB. (n.d.). dokumen.pub. https://dokumen.pub/programming-pearls-2nd-edition-0201657880.html 
Book Details - MIT Press. (2024, January 12). MIT Press. https://mitpress.mit.edu/9780262533058/introduction-to-algorithms/ 
Art of Computer Programming, The: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada. (n.d.). https://www.amazon.ca/Art-Computer-Programming-Sorting-Searching/dp/0201896850
