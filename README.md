# Python-Nearest-Neighbor-Truck-Logistics-Program
The Python Logistics Planner optimizes routing for a delivery service using the Nearest Neighbor Algorithm and a dynamic hash table. This solution minimizes travel distances and adapts to real-time changes, ensuring efficient and timely deliveries. Built in Python, the program features a modular design for scalability and easy maintenance.

<h1>Project Overview</h1>
<h2>A. Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.</h2>
<p>I chose the Nearest Neighbor Algorithm for the Routing Program for its straightforward method that focuses on minimizing travel distances between delivery points. Starting from a central hub, the algorithm efficiently selects the nearest unvisited destination, ensuring routes are planned both logically and efficiently.</p>
<p>This approach is not only easy to implement but also highly adaptable to dynamic routing changes, such as varying delivery deadlines and special handling requirements.</p>
<p>In the implementation within my deliver_packages function, the algorithm considers the current location of the truck and the destination of each undelivered package, utilizing the distance_between function to determine the shortest path. This significantly optimizes route efficiency, crucial given the constraints of delivering all packages within a limited timeframe and under specific mileage.</p>
<p>Moreover, the Nearest Neighbor Algorithm's integration with real-time updates to the truck's state—adjusting the truck's position, the distance traveled, and the delivery time after each stop—ensures the routing dynamically adapts to the ongoing delivery scenario. This dynamic adaptability is vital for maintaining operational efficiency and meeting stringent delivery constraints, such as ensuring that Truck #3 starts its route only after one of the other trucks has completed its deliveries.</p>
<p>My application of this method balances simplicity in execution with the ability to handle the complex logistical challenges of package delivery, demonstrating a robust application of theoretical algorithms to practical, real-world challenges in our delivery logistics domain (Programming Pearls [2nd Edition] 0201657880 - DOKUMEN.PUB, n.d.).</p>

<h2>B. Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.</h2>
<p>I have identified a self-adjusting data structure called the "ResizableDict," which is an implementation of a dynamic hash table or hash map. This data structure is particularly suited for use with the package delivery routing algorithm described in the program. The hash table facilitates efficient retrieval and update of package data, which is crucial for the dynamic delivery scheduling and tracking tasks of the delivery service.</p>
<p><strong>1) Explain how your data structure accounts for the relationship between the data components you are storing.</strong></p>
<p>In the Routing Program, I have implemented a Resizable Hash Table combined with the Nearest Neighbor Algorithm to efficiently manage and retrieve package data. This structure supports effective storage and quick retrieval of package details, which are essential for optimizing delivery routes.</p>
<h3>Data Structure Overview:</h3>
<h4>Key-Value Pairing:</h4>
<p>The hash table uses package IDs as unique keys and associates them with corresponding package details (delivery address, deadline, weight, and status) stored as values. This setup ensures that all related data for each package is aggregated and quickly accessible, crucial for making routing decisions.</p>
<h4>Handling Collisions:</h4>
<p>To maintain data integrity and ensure accessibility, I employ chaining to resolve collisions within the hash table. Each bucket in the table starts as an empty list, ready to store multiple entries if multiple keys hash to the same index. This approach ensures that the data for each package remains distinct and complete, preserving the accuracy and availability of package information.</p>

<h3>Big O Notation for Hash Table Operations:</h3>
<p><strong>Insertion, Deletion, and Lookup:</strong> These operations typically run in O(1) time, contributing to the efficiency of the hash table. In scenarios where many keys hash to the same index—resulting in longer chains—these operations could degrade to O(n), although this is mitigated by the dynamic resizing of the hash table.</p>

<h3>Dynamic Adjustability:</h3>
<p>The hash table supports dynamic updates crucial for the real-time nature of delivery logistics. For instance, if a package's delivery status changes or an address needs to be updated, the relevant entry can be quickly located using the package ID and adjusted as needed. This adaptability is pivotal for managing deliveries and adjusting routes based on real-time conditions.</p>
<p><strong>Pseudocode for Using Hash Table with Nearest Neighbor Algorithm:</strong></p>
<pre>
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
</pre>

<h3>Scalability and Adaptability:</h3>
<p>The hash table is engineered to scale efficiently with the addition of more packages. As the load factor increases, the table resizes to maintain operational efficiency. Chaining as a collision resolution method ensures that even with a high number of entries, the system can swiftly retrieve and update package information, adapting to changes such as route modifications or urgent delivery needs.</p>
<h3>Conclusion:</h3>
<p>This setup makes the hash table a robust structure for storing package data and aligns perfectly with the operational demands of the Nearest Neighbor Algorithm. Quick access to detailed package information enables the algorithm to efficiently plan and adjust routes, ensuring timely deliveries under varying logistical constraints (Book Details - MIT Press, 2024). The integration of this data structure with the routing algorithm demonstrates a high level of competence in handling the complexities of real-world package delivery systems.</p>

<h2>C. Write an overview of your program in which you do the following:</h2>
<h4>1. Explain the algorithm’s logic using pseudocode.</h4>
<pre>
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
</pre>

<h4>2. Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.</h4>

<p><strong>Specs:</strong></p>
<ul>
  <li>Computer: ASUS Custom-Built PC</li>
  <li>Memory: 32 GB RAM</li>
  <li>Processor: Intel(R) Core(TM) i7-10700 CPU @ 2.90GHz, 2904 Mhz, 8 Core(s), 16 Logical Processor(s)</li>
  <li>Operating System: Microsoft Windows 11 Pro</li>
  <li>Programming Language: Python 3.13</li>
  <li>IDE: VS Code</li>
</ul>

<h4>3. Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.</h4>

<h3>Main.py</h3>

<p><strong>CSV Data Loading (get_csv_data function)</strong></p>
<p>Time Complexity: O(n) where n is the number of records in the CSV file. Each record is read sequentially.</p>
<p>Space Complexity: O(n) as the data is stored in a list, consuming space proportional to the number of records.</p>

<p><strong>Loading Packages into Hash Map (load_packages_file function)</strong></p>
<p>Time Complexity: O(n) for reading and inserting n package records into the hash map. Although the average time complexity for each insert is O(1), reading n records results in a linear time complexity.</p>
<p>Space Complexity: O(n) as each package object is stored in the hash map.</p>

<p><strong>Distance Calculations (distance_between function)</strong></p>
<p>Time Complexity: O(1) since the distance retrieval from a pre-loaded two-dimensional list is a direct access operation.</p>
<p>Space Complexity: O(1) as no additional space is required for performing this operation.</p>

<p><strong>Address Index Retrieval (get_address function)</strong></p>
<p>Time Complexity: O(n) where n is the number of addresses. The function performs a linear search through the address list.</p>
<p>Space Complexity: O(1) as the operation does not allocate additional space proportional to the input size.</p>

<p><strong>Package Delivery Simulation (deliver_packages function)</strong></p>
<p>Time Complexity: O(n^2) as it involves finding the nearest package for each undelivered package, which includes a nested operation of finding the minimum distance which itself iterates over the list of packages.</p>
<p>Space Complexity: O(n) due to storing the list of not_delivered packages.</p>

<h3>Truck and Package Management</h3>

<p><strong>Time Complexity:</strong> O(p) where p is the number of packages on a truck during the assignment of packages to trucks. Each assignment is O(1), and this is done for each package.</p>
<p><strong>Space Complexity:</strong> O(1) as the operation modifies existing objects without allocating new proportional space.</p>

<p><strong>User Interface Functions (main_user_interface, initiate_tracking_process, etc.)</strong></p>
<p><strong>Time Complexity:</strong> Varies; most operations are O(1), except for package status updates which are O(n) where n is the number of packages.</p>
<p><strong>Space Complexity:</strong> Generally O(1), except where package data is iteratively accessed or modified, still using existing data structures without new allocations.</p>

<h3>DeliveryParcel.py</h3>

<p><strong>Initialization and Status Updates</strong></p>
<p><strong>Time Complexity:</strong> O(1) for both initialization and status update methods as these involve direct assignments and condition checks.</p>
<p><strong>Space Complexity:</strong> O(1) as no additional space is used beyond what is necessary for storing instance variables.</p>

<h3>ResizableHashmap.py</h3>

<p><strong>Hash Table Operations (put, get, remove, _resize)</strong></p>
<p>Time Complexity:</p>
<p>put: Average O(1), worst O(n) when resizing is needed.</p>
<p>get: Average O(1), worst O(n) in case of many collisions.</p>
<p>remove: Average O(1), worst O(n) similar to get.</p>
<p>_resize: O(n) as it rehashes all elements to new buckets.</p>

<p><strong>Space Complexity:</strong> All operations are O(1) in space except for _resize, which temporarily requires additional space but this is managed within the method.</p>

<h3>DeliveryTruck.py</h3>

<p><strong>Initialization and String Representation</strong></p>
<p><strong>Time Complexity:</strong> O(1) for initialization; O(n) for string representation where n is the number of packages due to iterating over packages.</p>
<p><strong>Space Complexity:</strong> O(n) for both, as space depends on the number of packages handled.</p>

<h4>Overall Program Complexity</h4>
<p><strong>• Time Complexity:</strong> The most time-consuming operations involve package delivery simulation and user interface functions which handle package data iteratively. Hence, the overall time complexity could be considered O(n^2) due to the quadratic behavior in the delivery simulation.</p>
<p><strong>• Space Complexity:</strong> The program primarily stores data in structures proportional to the number of packages and addresses, resulting in an overall space complexity of O(n), where n is the sum of packages and address data points.</p>

<h4>4. Explain the capability of your solution to scale and adapt to a growing number of packages.</h4>

<h2>Scalability</h2>

<h3>Resizable Hash Map (ResizableDict):</h3>
<p>The ResizableDict is a central feature designed to handle a growing number of packages efficiently. As the number of packages increases, the hash map automatically increases its capacity to maintain a low load factor, which is crucial for keeping the average time complexity for operations like insertions, deletions, and retrievals at O(1). This dynamic resizing helps avoid performance degradation due to excessive collisions, which typically occur in hash tables as they fill up.</p>
<p>The resizing operation itself is O(n), as it involves rehashing all entries into a new, larger bucket array. However, because resizing happens progressively less frequently as the size grows (doubling the capacity each time), the average cost of insertions (including occasional resizing) remains amortized constant.</p>

<h4>Efficient Data Retrieval and Update:</h4>
<p>Using a hash map ensures that accessing and updating package information, such as status or location updates, is efficient. This allows the system to manage more packages without significantly impacting the response time for queries, which is essential in a real-time delivery tracking context.</p>

<h2>Adaptability</h2>

<h3>Modular Design:</h3>
<p>The program's modular design, with separate components for managing package data (DeliveryParcel), routing and delivery simulation (deliver_packages), and truck management (DeliveryTruck), facilitates adaptability. This modular architecture allows individual components to be modified or replaced as requirements evolve, without extensive reworking of the entire system.</p>

<h4>Dynamic Routing and Delivery Management:</h4>
<p>The delivery simulation (deliver_packages) adapts to the real-time status of deliveries, including changes in package priorities or delivery routes. The algorithm's ability to dynamically select the next nearest package for delivery means the routing logic can adapt on-the-fly to changes such as traffic conditions or priority updates.</p>

<h4>User Interaction and Real-time Updates:</h4>
<p>The user interface functions, which provide real-time updates on package status and facilitate user interactions, are designed to handle varying loads and can be easily extended to include more features such as predictive delivery times, alternative routing options, or customer notifications.</p>

<h3>General Considerations</h3>

<h4>Handling Increased Load:</h4>
<p>The system's current implementation should handle moderate increases in package volume effectively. However, for significant scale-ups, additional considerations like distributed computing resources, more sophisticated routing algorithms (e.g., using machine learning for predictive analysis), and enhanced data synchronization across multiple locations would be necessary to maintain performance.</p>

<h4>Potential Bottlenecks:</h4>
<p>While the hash map handles package data efficiently, the O(n^2) complexity of the package delivery simulation could become a bottleneck as the number of packages grows very large. Exploring more advanced algorithms that can provide near-optimal solutions with lower complexity, such as using approximate or heuristic methods like Genetic Algorithms, Simulated Annealing, or Ant Colony Optimization, could be beneficial.</p>
<p>Overall, the current design balances efficiency and adaptability well for a growing number of packages but would require further enhancements to handle large-scale operations typical of major logistics and courier companies.</p>

<h4>5. Discuss why the software design would be efficient and easy to maintain.</h4>

<h3>Software Efficiency</h3>
<h4>Use of a Resizable Hash Map:</h4>
<p>The implementation of a ResizableDict for managing package data significantly enhances efficiency. By dynamically resizing based on the load factor, it ensures that the hash table maintains a balance between space and time efficiency, keeping average access, insertion, and deletion times close to O(1). This is crucial for high-performance scenarios where quick data retrieval and update are essential.</p>

<h4>Optimized Data Access Patterns:</h4>
<p>The software design strategically utilizes data structures such as lists and hash maps to optimize access patterns. For example, packages are accessed via their unique IDs using the hash map, ensuring constant-time complexity on average for queries. This leads to fast response times even as the number of packages grows.</p>

<h4>Modular Function Design:</h4>
<p>Functions like get_csv_data, load_packages_file, and deliver_packages are clearly defined with specific roles, reducing dependencies between components of the software. This separation of concerns not only makes the system more efficient by isolating changes to individual modules but also enhances performance by allowing focused optimizations.</p>

<h4>Clear Separation of Concerns:</h4>
<p>The program structure is divided into distinct modules (ResizableHashmap.py, DeliveryParcel.py, DeliveryTruck.py, and Main.py), each handling a specific aspect of the application. This separation simplifies understanding the system as a whole, making it easier for developers to identify where changes should be made without unintended side effects on other parts of the system.</p>

<h4>Self-Documenting and Descriptive Code:</h4>
<p>The codebase includes extensive comments and documentation, particularly explaining the purpose of each function and class, the expected input and output, and the complexity of operations. This level of documentation facilitates easier onboarding of new developers and assists in maintaining the code, as the intended design and functionality are clearly communicated.</p>

<h4>Scalable and Extendable Architecture:</h4>
<p>The software's architecture is designed to be scalable, as seen with the use of a dynamic hash map and adaptable routing logic. New functionalities, such as adding different types of deliveries or support for new types of routing algorithms, can be integrated with minimal changes to the existing system. The object-oriented design allows for easy extension of classes and functionality.</p>

<h4>Testability:</h4>
<p>Each module and function is designed to be self-contained, which enhances testability. Unit tests can be easily written and executed for individual components without the need for complex setup or dependencies. This modularity in design supports continuous integration and deployment practices, ensuring that changes can be tested and deployed with confidence.</p>

<h4>Error Handling and Robustness:</h4>
<p>The program includes basic error handling and validation, particularly in user input and file reading operations, which contributes to the overall robustness of the application. Enhancing this aspect with more comprehensive error management and recovery strategies could further improve maintainability.</p>
<p>Overall, the software design of the Routing Program combines efficiency with maintainability through thoughtful architecture, data structure choices, and coding practices. This not only facilitates current operational requirements but also lays a foundation for future enhancements and scalability.</p>

<h4>6. Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).</h4>
<h3>Strengths</h3>
<h4>Dynamic Resizing:</h4>
<p>One of the key strengths of the ResizableDict is its ability to dynamically adjust its size based on the load factor. This ensures that the hash table remains efficient in terms of access, insertion, and deletion operations even as the number of elements grows. By maintaining a balance between the number of elements and the bucket size, it significantly reduces the likelihood of hash collisions, which can degrade performance.</p>

<h4>Efficient Access Times:</h4>
<p>The hash table provides average O(1) time complexity for access, insert, and delete operations under typical conditions. This efficiency is crucial for real-time applications where quick data retrieval and updates are essential. For example, in the package delivery system I've developed, the status of deliveries needs to be updated and queried frequently, making this characteristic extremely valuable.</p>

<h4>Scalability:</h4>
<p>As the hash table automatically resizes, it can handle growth in data smoothly without significant manual adjustments in the underlying data structure. This scalability is advantageous for applications that experience varying loads or need to scale up to accommodate more data over time.</p>

<h4>Space Efficiency:</h4>
<p>While resizing increases capacity, the hash table only uses space proportional to the number of entries it contains, ensuring that space is not wasted. This space efficiency is critical in environments where memory resources may be constrained.</p>

<h3>Weaknesses</h3>
<h4>Cost of Resizing:</h4>
<p>While resizing helps maintain operational efficiency, the resizing operation itself can be costly. It involves rehashing all existing elements into new buckets, which has a time complexity of O(n). During the resizing process, there can be a temporary performance hit, which might affect system responsiveness, especially if the hash table is very large.</p>

<h4>Worst-Case Time Complexity:</h4>
<p>In the worst case, where many elements hash to the same bucket (high collision scenario), the time complexity for access and update operations can degrade to O(n). While this scenario is less likely with a good hash function and proper load management, it is still a potential weakness that can impact performance under certain conditions.</p>

<h4>Complexity in Concurrency:</h4>
<p>Managing concurrency in a hash table can be challenging, especially during resizing operations. Synchronization mechanisms are necessary to ensure data consistency, which can complicate the implementation and may reduce performance in multi-threaded environments.</p>

<h4>Dependence on Hash Function:</h4>
<p>The performance of the hash table heavily depends on the quality of the hash function used. A poor hash function can lead to increased collisions, undermining the efficiency advantages of the hash table. Ensuring a uniform distribution of hash values is critical but can be challenging depending on the data characteristics.</p>

<h4>Handling of Large Data Values:</h4>
<p>If the data elements stored in the hash table are large, the resizing operation can become more resource-intensive, both in terms of time and memory usage. This can be a drawback in systems where data payloads are substantial.</p>
<p>In summary, the ResizableDict in my Routing Program offers significant strengths in terms of scalability, efficiency, and dynamic sizing, making it well-suited for the program’s needs. However, I am always mindful of its weaknesses, especially regarding performance under high collision conditions and during resizing, to optimize its use and ensure robust system performance.</p>

<h4>7. Justify the choice of a key for efficient delivery management from the following components:</h4>
<ul>
  <li>delivery address</li>
  <li>delivery deadline</li>
  <li>delivery city</li>
  <li>delivery zip code</li>
  <li>package ID</li>
  <li>package weight</li>
  <li>delivery status (i.e., at the hub, en route, or delivered), including the delivery time</li>
</ul>

<h3>Uniqueness:</h3>
<p>The package ID is unique to each package, which eliminates the possibility of key collisions within the data storage system. This uniqueness ensures that each query or update operation targets precisely the intended package without confusion or error.</p>

<h4>Efficiency in Access and Updates:</h4>
<p>Using package ID as the key allows for constant-time complexity (O(1) on average) for accessing, updating, or deleting package information in the hash map (ResizableDict). This is because hash tables provide extremely fast access to elements when the keys distribute uniformly, as they do with unique identifiers like package IDs.</p>

<h4>Integration with Other System Operations:</h4>
<p>Package ID serves as a straightforward reference that can be used across various components of the system, such as during the loading and unloading of packages onto trucks, during the tracking of packages, and when updating delivery status. This integration simplifies the system’s architecture by reducing the need for complex joins or searches across different attributes.</p>

<h4>Independence from Variable Data:</h4>
<p>Other potential keys such as delivery address, deadline, or status could change over the lifecycle of a delivery (e.g., a change in delivery address due to customer request or an update in status as it moves from "at the hub" to "delivered"). Using a mutable attribute as a key could complicate the management of data integrity and consistency. In contrast, package ID is immutable – once assigned, it does not change, which makes it ideal for stable and reliable indexing.</p>

<h4>Irrelevance of Other Attributes to Indexing Efficiency:</h4>
<p>Attributes like delivery address, city, zip code, and deadline are important for sorting and routing decisions but are not efficient for quick data retrieval as keys because they are not unique and can be shared by multiple packages, potentially leading to inefficiencies and the need for further filtering.</p>
<p>Package weight and delivery status, including time, are attributes subject to frequent updates and thus are unsuitable for use as primary keys. Their use as keys would lead to inefficiencies in rehashing or reindexing the data as these values change.</p>

<h4>Summary:</h4>
<p>Choosing package ID as the key for managing package data within the Routing Program offers significant advantages in terms of data access speed, system simplicity, and maintenance. It supports efficient operations across the system's lifecycle, from package intake through delivery. This choice aligns with the principles of effective database and hash map design by leveraging the inherent properties of uniqueness and immutability, which are critical for ensuring robust and efficient data handling in dynamic and complex delivery systems like the Routing Program (Art of Computer Programming, the: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada, n.d.).</p>

<h4>D. Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.</h4>
<p>Programming Pearls [2nd edition] 0201657880 - DOKUMEN.PUB. (n.d.). dokumen.pub. https://dokumen.pub/programming-pearls-2nd-edition-0201657880.html</p>
<p>Book Details - MIT Press. (2024, January 12). MIT Press. https://mitpress.mit.edu/9780262533058/introduction-to-algorithms/</p>
<p>Art of Computer Programming, The: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada. (n.d.). https://www.amazon.ca/Art-Computer-Programming-Sorting-Searching/dp/0201896850</p>


<h1>Second Part of Project - Explanation</h1>

Picture of Hashtable
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/5e0baee4-b3e6-4fc0-af2d-644160c77cb4)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/c8d37222-1ab5-4f8e-8f38-2fe04d803e9c)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/7cfa72b1-90a8-4a1c-ba0e-235c598c4b82)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/e55f3f3c-9e9f-4ecd-9cb4-26daca282002)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/2824634a-5b2e-4c66-a5da-47e91438a6b3)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/fa750a48-1684-4144-a88b-e7f19930bea9)

main.py
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/cf5b1dbe-15b1-477d-814f-6645fda29ab5)

Lookup function
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/148759a5-1a44-47bd-a84d-250afca615c4)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/558cc8cf-25f6-4093-9b35-05d0290c27c2)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/9b674ff1-0c53-484f-a0f9-0ef8bf8adc1d)

Interface
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/bd95bc71-72b3-4757-86ed-c10e2e4d6c41)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/44632925-11f2-4b53-8bef-8a0e004606b6)

Output
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/cc738cf5-2c83-4a11-be87-88bcf340f1d8)

First status check (9:15am)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/07b0d921-57eb-4c0c-8c1c-1fd4121b3d80)

Second status check (9:50am)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/dcd4a357-7cff-4fda-ab31-7a691e2bf8af)

Third status check (12:45)
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/8908d18c-2747-4542-b70c-67c54c26ff76)

Code execution
![image](https://github.com/MayCooper/Python-Nearest-Neighbor-Truck-Logistics-Program/assets/82129870/8d7ad3ec-060a-4aef-8857-80370c75a018)

<h2>F. Justify the package delivery algorithm used in the solution as written in the original program by doing the following:</h2>
<h3>F1) Describe two or more strengths of the algorithm used in the solution</h3>
<p>The package delivery algorithm implemented in the program exhibits several strengths that contribute to its overall effectiveness and efficiency in managing deliveries. Here are two main strengths:</p>
<p><strong>1. Efficient Package Retrieval and Update</strong><br>
The algorithm leverages a ResizableHashmap to store and manage package information, which supports efficient retrieval and update operations. This approach provides several advantages:</p>
<ul>
    <li><strong>Constant Average Time Complexity:</strong> The use of a hash map ensures that, on average, package retrieval and update operations are performed in constant time (O(1)). This is crucial for the delivery system where quick access to package details is necessary to update statuses or retrieve specific package information rapidly.</li>
    <li><strong>Scalability:</strong> The resizable nature of the hash map allows the data structure to grow according to the load factor threshold. This means the system can handle an increasing number of packages without a significant drop in performance, as the hash map resizes itself to maintain operational efficiency and reduce collisions.</li>
</ul>
<p><strong>2. Route Optimization for Deliveries</strong><br>
The delivery process employs a nearest-neighbor heuristic to determine the sequence in which packages should be delivered. This method has several strengths:</p>
<ul>
    <li><strong>Reduction of Travel Distance:</strong> By always selecting the nearest unvisited destination, the algorithm effectively minimizes the distance traveled between stops. This can lead to a reduction in total travel time and operational costs (such as fuel and vehicle maintenance).</li>
    <li><strong>Simplicity and Speed:</strong> The nearest-neighbor approach is relatively simple to implement and execute. Despite its simplicity, it is particularly effective in scenarios where packages are densely located within specific areas, enabling quick computation and re-routing as needed during the delivery process.</li>
</ul>
<p>These strengths collectively enhance the system's ability to handle package deliveries in a manner that is both timely and resource-efficient. The use of a dynamic hash map for storage and the application of a heuristic route optimization significantly contribute to the robustness of the delivery management system (The Algorithm Design Manual: Skiena, Steven S: 9781849967204: Books - Amazon.ca, n.d.).</p>

<h3>F2) Verify that the algorithm used in the solution meets all requirements in the scenario.</h3>
<p><strong>1. Total Mileage Under 140 Miles</strong><br>
The algorithm utilizes the nearest neighbor method to optimize delivery sequences. Consistently selecting the closest next destination for each delivery significantly reduces the distance traveled between stops. This strategy efficiently plans routes to keep total mileage under the 140-mile target.</p>
<p><strong>2. Handling of Delayed Packages</strong><br>
Packages affected by delays, such as those delayed on flights, are strategically assigned to trucks that depart after the new arrival times (e.g., 9:05 am). This ensures all packages, including delayed ones, are delivered on the same day.</p>
<p><strong>3. Specific Truck Requirements</strong><br>
The algorithm manages specific truck requirements by manually loading designated packages onto the correct trucks in accordance with special handling notes. For example, packages like 3, 18, 36, and 38, which are restricted to truck 2, are specifically assigned to that truck.</p>
<p><strong>4. Meeting Delivery Deadlines</strong><br>
For packages with strict deadlines (e.g., “10:30 am for Package 1”), the algorithm prioritizes these using the nearest neighbor strategy to efficiently plan routes that meet these times. Packages with tight schedules are manually assigned to trucks to ensure they meet their delivery windows.</p>
<p><strong>5. Address Correction</strong><br>
Special handling is incorporated for packages needing address corrections, such as package 9. Scheduled on truck 2, which departs post-10:20 am, it allows for delivery to the corrected address, facilitated by the update_status function within the Package class.</p>
<p><strong>6. Bundled Deliveries</strong><br>
The algorithm accommodates bundled delivery requirements by manually grouping specific packages that must be delivered together onto the same truck, ensuring compliance with joint delivery instructions.</p>
<p><strong>7. Real-time Interface Display</strong><br>
The delivery system features a real-time interface that allows users to actively display package delivery information. Users can input a specific time and select to view the status of a single package or all packages, with updates reflecting the real-time status of each delivery.</p>
<p><strong>8. Capacity and Uniqueness of Package IDs</strong><br>
Each truck is initialized with a specific list of package IDs, adhering to the maximum capacity of 16 packages. The algorithm ensures that each package has a unique ID, as demonstrated in the system, where each ID is linked with specific delivery details.</p>
<p><strong>9. Truck Speed and Operation</strong><br>
Trucks travel at a specified average speed of 18 miles per hour. The delivery timing calculations incorporate this speed directly into the travel time computation, optimizing routing efficiency.</p>
<p><strong>10. Collision-Free Operation</strong><br>
The software simulation inherently avoids any possibility of collisions by not modeling them, ensuring a smooth logistical operation.</p>
<p><strong>11. Truck and Driver Allocation</strong><br>
Three trucks are each assigned a specific set of packages and corresponding delivery schedule. The system ensures that each driver remains with the assigned truck throughout the service.</p>
<p><strong>12. Operational Times</strong><br>
Drivers start their routes no earlier than 8:00 a.m., with the trucks fully loaded. The scheduling of trucks adheres strictly to these operational times, ensuring timely departures.</p>
<p><strong>13. Instantaneous Loading and Delivery</strong><br>
The program assumes that loading and delivery times are instantaneous, focusing instead on optimizing travel and routing logistics.</p>
<p><strong>14. Special Notes and Address Corrections</strong><br>
Special conditions, such as the address correction for package #9 at 10:20 a.m., are dynamically managed within the delivery process to ensure accurate redirection.</p>
<p><strong>15. Symmetric Distance Table</strong><br>
The algorithm accounts for and utilizes symmetric distances as provided in the “Distance Table” ensuring that travel calculations remain consistent regardless of direction.</p>
<p><strong>16. Completion Requirement</strong><br>
The algorithm ensures that the delivery process continues until all 40 packages are delivered, effectively marking the operational day's end.</p>

<h3>F3) Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.</h3>
<p><strong>1. Dijkstra's Algorithm</strong><br>
Dijkstra's algorithm is a well-known graph search method used to find the shortest paths between nodes in a graph, which could represent various locations in a package delivery system. Here’s how it would meet the delivery system’s requirements:</p>
<ul>
    <li><strong>Route Optimization:</strong> Dijkstra's algorithm can determine the shortest path from a starting point (the hub) to all other delivery locations. This would ensure that each truck travels the shortest possible total distance, potentially keeping the total mileage under 140 miles.</li>
    <li><strong>Handling Delays and Deadlines:</strong> The algorithm can be adapted to start routing at different times, accommodating delayed packages by recalculating paths as new packages are ready for delivery. It would also prioritize routes based on delivery deadlines by adjusting weights in the graph.</li>
    <li><strong>Special Handling and Bundled Deliveries:</strong> By adjusting the weights for certain edges or nodes (representing delivery locations or packages), Dijkstra’s algorithm can account for specific truck requirements and bundled deliveries, ensuring certain packages are delivered together or on specific trucks.</li>
</ul>
<p><strong>2. Tabu Search Algorithm</strong><br>
Tabu search is an advanced metaheuristic algorithm that guides a local heuristic search procedure to explore the solution space beyond local optimality. It is particularly useful in solving routing problems such as those encountered in package delivery systems. Here’s how it would align with the requirements:</p>
<ul>
    <li><strong>Route Optimization:</strong> Tabu search can efficiently explore various permutations of delivery sequences to find an optimal route that minimizes travel distance and time, which is crucial for keeping the mileage under the specified target.</li>
    <li><strong>Dynamic Adaptability:</strong> The algorithm's ability to remember previous states (using a tabu list) prevents it from revisiting ineffective solutions and allows it to dynamically adapt to changes such as delayed packages or updated addresses, improving its responsiveness to real-time scenarios.</li>
    <li><strong>Complex Constraints Handling:</strong> Tabu search's flexible framework enables the integration of complex constraints, such as specific truck loading requirements and delivery deadlines. It can prioritize these constraints during the search process, ensuring compliance with all logistical and operational requirements.</li>
</ul>
<p>Both algorithms are strong and adaptable options for tackling complex routing challenges. They could greatly enhance efficiency and effectiveness compared to simpler methods like the nearest neighbor algorithm. This is especially true in situations that involve multiple constraints and require the flexibility to adjust routes dynamically (Genetic Algorithms in Search, Optimization and Machine Learning: Goldberg, David E.: 9780201157673: Amazon.com: Books, n.d.).</p>

<h3>F3A) Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.</h3>
<p>The original solution for the program uses the nearest neighbor algorithm, which is straightforward and focuses on short-term decisions—picking the closest next stop with each step. Let's look at how Dijkstra's Algorithm and Tabu Search, the two algorithms we've considered, differ from this approach in more practical terms:</p>
<p><strong>Dijkstra's Algorithm</strong></p>
<ul>
    <li><strong>Broader Perspective:</strong></li>
    <ul>
        <li><strong>Overall Path Planning:</strong> Unlike the nearest neighbor approach, which just looks at the immediate next step, Dijkstra's algorithm calculates the shortest paths from the starting point to all other points. This means it takes a more comprehensive view, ensuring that the path chosen is the shortest in terms of the total distance from the start, not just the next destination.</li>
        <li><strong>Guaranteed Optimal Routes:</strong> Dijkstra's method provides a thorough solution by considering cumulative distances, which guarantees that the path it selects is the optimal one based on the total travel distance. This broader and more strategic approach contrasts sharply with the nearest neighbor method, which can sometimes settle for less efficient routes.</li>
    </ul>
</ul>
<p><strong>Tabu Search</strong></p>
<ul>
    <li><strong>Smarter Searching:</strong></li>
    <ul>
        <li><strong>Explorative Search Techniques:</strong> Tabu Search goes beyond the linear pathfinding of the nearest neighbor method. It explores a wider range of potential routes by remembering recent choices and deliberately avoiding them if they weren’t beneficial. This prevents it from getting stuck in less optimal routing loops and encourages finding new and possibly better paths.</li>
        <li><strong>Adaptable to Changes:</strong> This algorithm is particularly adept at adapting to new information or changes during the route, such as delays or last-minute rerouting. It can adjust its strategy on the fly, which is a significant upgrade over the nearest neighbor approach that simply moves from one point to the next without re-evaluating past decisions.</li>
    </ul>
</ul>
<p><strong>In Essence:</strong><br>
Both Dijkstra's Algorithm and Tabu Search offer a more holistic and flexible approach compared to the nearest neighbor algorithm used in the original program. They’re designed to look at the bigger picture and adapt more dynamically to the complexities of real-world routing, making them potentially more effective for a complex delivery network.</p>

<h2>G. Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.</h2>
<p>If given the opportunity to revisit and enhance the package delivery system project, there are several modifications and improvements I would consider, apart from integrating Dijkstra's Algorithm or Tabu Search. These changes aim to address potential inefficiencies and limitations observed in the original implementation and incorporate advances in technology and algorithmic approaches:</p>
<h4>1. Advanced Optimization Algorithms:</h4>
<p><strong>Implementation of Genetic Algorithms or Simulated Annealing:</strong></p>
<ul>
    <li><strong>Genetic Algorithms (GA):</strong> These could be used for route optimization by generating a variety of possible delivery sequences and iteratively improving them through operations analogous to biological evolution, such as mutation and crossover. GAs are particularly effective in exploring a vast solution space and finding near-optimal solutions for complex problems like route optimization with many constraints.</li>
    <li><strong>Simulated Annealing (SA):</strong> This algorithm could be employed to escape local optima by allowing worse solutions in the early stages of the solution process. SA gradually 'cools' and stabilizes towards the best solution, making it powerful for achieving global optimization in routing and scheduling problems.</li>
</ul>
<h4>2. Improved Data Structures:</h4>
<p><strong>Use of Graph Databases or Advanced Spatial Data Structures:</strong></p>
<ul>
    <li><strong>Graph Databases:</strong> Switching to graph databases from traditional relational databases or simple data structures could improve the management and querying of interconnected data, like distances and routes between locations. This would streamline the process of finding efficient paths and handling dynamic changes in the delivery network.</li>
    <li><strong>Spatial Data Structures (e.g., k-d trees, R-trees):</strong> These could be employed to manage spatial information more efficiently, particularly for tasks like nearest neighbor searches which are fundamental in routing decisions. This would drastically reduce the computation time for these operations.</li>
</ul>
<h4>3. Real-time Traffic and Weather Integration:</h4>
<p><strong>Dynamic Routing Adjustments:</strong></p>
<ul>
    <li><strong>Integration of Real-time Traffic Data:</strong> Incorporating live traffic data would allow the system to dynamically reroute deliveries to avoid delays caused by traffic congestion, road closures, etc.</li>
    <li><strong>Weather Conditions Consideration:</strong> Adjusting delivery routes based on weather conditions could improve the reliability and speed of deliveries, particularly in adverse weather conditions that might slow down transportation.</li>
</ul>
<h4>4. User Interface Enhancements:</h4>
<p><strong>More Interactive and Informative UI:</strong></p>
<ul>
    <li><strong>Enhanced Tracking Features:</strong> Implement features that allow both the dispatchers and customers to track the real-time status of their deliveries more interactively, providing estimated arrival times and current location on a map.</li>
    <li><strong>Mobile Compatibility:</strong> Develop a mobile-friendly version of the system, enabling access from smartphones and tablets for both drivers and customers, enhancing accessibility and convenience.</li>
</ul>
<h4>5. Machine Learning for Predictive Analytics:</h4>
<p><strong>Predictive Modeling for Delivery Times and Load Optimization:</strong></p>
<ul>
    <li><strong>Machine Learning Models:</strong> Utilize machine learning to predict the best times for deliveries based on historical traffic patterns, customer availability, and other factors. This could optimize delivery schedules and improve customer satisfaction.</li>
    <li><strong>Load Optimization:</strong> Implement machine learning algorithms to optimize the loading of trucks based on package size, weight, and delivery location, ensuring the most efficient use of space and minimizing the number of trips needed.</li>
</ul>
<h4>6. Sustainability Focus:</h4>
<p><strong>Route Optimization for Reduced Carbon Footprint:</strong></p>
<ul>
    <li><strong>Eco-Friendly Routing:</strong> Implement algorithms that not only optimize for time and distance but also for the lowest carbon footprint, supporting environmental sustainability initiatives.</li>
</ul>
<p>These proposed enhancements to the package delivery system are intended to augment its operational efficiency and overall effectiveness, while also improving its scalability and reducing its environmental footprint. Additionally, these improvements aim to significantly boost customer satisfaction through the adoption of advanced technological solutions, ensuring a more dynamic, adaptable, and client-centric service offering.</p>

<h2>H. Verify that the data structure used in the solution meets all requirements in the scenario.</h2>
<p>In my implementation of the package delivery system, the ResizableHashmap plays a crucial role in managing package information efficiently. Here's how this data structure aligns with the system's operational needs:</p>
<p><strong>1. Constant-Time Access:</strong><br>
The ResizableHashmap provides constant-time complexity, O(1), for accessing package information using unique package IDs as keys. This capability is critical in a delivery system that requires swift retrieval and updates of package statuses, destinations, or any special instructions. Such rapid access ensures that package details can be updated or queried in real-time, facilitating immediate decision-making and updates.</p>
<p><strong>2. Efficient Insertion and Deletion:</strong><br>
The hash map excels in providing efficient insertion and deletion operations, which are fundamental for dynamically adding new packages to the system or removing those that have been delivered. These operations are designed to be efficient; however, in cases where multiple packages hash to the same index—a scenario known as chaining—the performance can degrade to O(n), where n is the number of packages at that index. This happens when the hash function maps multiple keys to the same slot, necessitating a traversal of a linked list at that index to find the correct package.</p>
<p><strong>3. Initialization and Capacity Handling:</strong><br>
The ResizableHashmap class includes an initialization method that accepts a capacity argument, typically set with a default value that represents the expected number of packages. The constructor populates the hash map with empty buckets, ready to store package information. This setup is essential for managing collisions efficiently through chaining, allowing each bucket to store multiple entries if their keys hash to the same index.</p>
<p><strong>4. Scalability:</strong><br>
One of the key strengths of the ResizableHashmap is its inherent scalability. It can accommodate an increasing number of package entries without a significant drop in performance, thanks to its ability to resize based on the load factor. As the system grows, whether due to an increase in daily package volume or a scaling of operational capacity, the hash map adjusts its size to maintain efficiency, ensuring consistent performance across varying loads.</p>
<p><strong>5. Dynamic Information Management:</strong><br>
The scenario demands up-to-date tracking and management of packages, including those with special handling notes or conditions that may change. The ResizableHashmap is particularly well-suited for this task, as it allows for quick modifications to package details whenever new information becomes available. Whether updating a delivery address post-dispatch or adjusting delivery priorities, the hash map supports these changes effectively, reflecting updates immediately across the system.</p>
<p>In summary, the ResizableHashmap in my delivery system implementation meets the requirements for efficient, scalable, and dynamic package management. It ensures that the system can handle both the day-to-day operations and exceptional circumstances efficiently, maintaining high performance and adaptability in a fast-paced logistical environment (Art of Computer Programming, the: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada, n.d.).</p>

<h3>H1. Identify two other data structures that could meet the same requirements in the scenario.</h3>
<p>In the context of the package delivery system, while the ResizableHashmap effectively manages package data, other data structures might also meet these requirements, potentially offering additional functionalities or efficiencies. Here are two viable alternatives:</p>
<p><strong>1. Balanced Binary Search Trees (e.g., AVL Trees or Red-Black Trees)</strong></p>
<ul>
    <li><strong>Order Maintenance:</strong> These trees inherently maintain data in a sorted order, facilitating operations like range searches or sorted outputs, which can be advantageous for systematic data processing.</li>
    <li><strong>Consistent Logarithmic Performance:</strong> They guarantee O(logn) time complexity for all major operations (insertion, deletion, lookup), providing predictable performance even as data scales.</li>
    <li><strong>Scalability:</strong> Their self-balancing nature allows them to efficiently manage growing data sizes, maintaining operational efficiency.</li>
    <li><strong>Considerations:</strong> Implementing AVL or Red-Black Trees requires mechanisms to ensure trees remain balanced, which can add complexity to the implementation.</li>
</ul>
<p><strong>2. Skip Lists</strong></p>
<ul>
    <li><strong>Efficient Search:</strong> By using multiple layers of linked lists, skip lists provide tree-like search efficiency (O(logn)), which enhances accessibility and update speeds.</li>
    <li><strong>Simplicity and Flexibility:</strong> They combine the simplicity of linked lists with improved efficiency through a probabilistic layering strategy, making them easier to implement than tree structures.</li>
    <li><strong>Dynamic Updates:</strong> Designed for easy modification, skip lists are ideal for environments with frequent data updates, like dynamic package tracking.</li>
    <li><strong>Considerations:</strong> The probabilistic nature of skip lists may lead to less predictable performance than strictly balanced trees, but they generally offer sufficient reliability for most applications.</li>
</ul>
<p>Both balanced binary search trees and skip lists present robust alternatives to hash maps, supporting efficient data operations while accommodating scalability and dynamic updates essential for logistics applications. The choice between these structures would hinge on specific system priorities, such as the need for ordered data or implementation simplicity (Problem Solving With Algorithms and Data Structures Using Python — Problem Solving With Algorithms and Data Structures, n.d.).</p>

<h3>H1A. Describe how each data structure identified in H1 is different from the data structure used in the solution.</h3>
<p>In the package delivery system, the ResizableHashmap is utilized primarily for its average constant-time complexity for access, insertion, and deletion. However, the alternatives—Balanced Binary Search Trees and Skip Lists—offer distinct features and benefits.</p>
<p><strong>Balanced Binary Search Trees:</strong> (like AVL Trees or Red-Black Trees) store data in an inherently ordered manner, unlike the hash map which does not maintain any inherent order among keys. This makes them ideal for operations that benefit from sorted data, such as range queries. They guarantee O(logn) time complexity for all major operations due to their self-balancing nature, which keeps tree heights minimal. However, this comes at the cost of more complex maintenance operations, such as rotations and rebalancing, which are necessary to preserve their structured properties.</p>
<p><strong>Skip Lists:</strong> employ a probabilistic layered linked list approach that achieves average-case logarithmic search times, similar to balanced trees but with a simpler implementation. Skip Lists are particularly adept at handling frequent updates efficiently since they do not require rehashing or dealing with collisions as hash maps do. Their structure allows for quick adjustments of pointers, facilitating easier and faster modifications.</p>
<p>Both alternatives provide robust guarantees on performance and offer advantages in scenarios requiring ordered data access or frequent updates. They contrast with hash maps primarily in their approach to data organization, performance consistency, and maintenance complexity. These differences make them potentially more suitable for applications where predictable performance and ease of updates are prioritized (Book Details - MIT Press, 2024).</p>

<h2>I. SOURCES</h2>
<p>The Algorithm Design Manual: Skiena, Steven S: 9781849967204: Books - Amazon.ca. (n.d.). https://www.amazon.ca/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202</p>
<p>Genetic Algorithms in Search, Optimization and Machine Learning: Goldberg, David E.: 9780201157673: Amazon.com: Books. (n.d.). https://www.amazon.com/exec/obidos/ASIN/0201157675/acmorg-20</p>
<p>Art of Computer Programming, The: Sorting and Searching, Volume 3: Knuth, Donald: 9780201896855: Programming Languages: Amazon Canada. (n.d.). https://www.amazon.ca/Art-Computer-Programming-Sorting-Searching/dp/0201896850</p>
<p>Book Details - MIT Press. (2024, January 12). MIT Press. https://mitpress.mit.edu/9780262533058/introduction-to-algorithms/</p>
<p>Problem Solving with Algorithms and Data Structures using Python — Problem Solving with Algorithms and Data Structures. (n.d.). https://runestone.academy/ns/books/published/pythonds/index.html</p>
