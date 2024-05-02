		AirOps Data Warehouse
   _____________________________________________________________________
 
1. Overview of the Project 
The goal of this project is to build a data warehouse for an airline to analyze its operations and improve customer satisfaction. We want to give executives a way to track flight activity, reservations, flight revenue, and segment-level details. By collecting both operational data and customer-centric information, the airline can see the full picture of its business. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/5466e645-fedb-489a-bde7-3f99f19e1096)

Business Processes Involved
Flight Activity
Reservations
Flight Revenue
Frequent Flyer Program
Customer Interaction
Passenger Tier Changes

2. Data Model Design 
The data warehouse employs a dimensional structure with a star schema design to support analytical processing and business insights. This design was chosen for several key advantages, including scalability, query performance, and ease of understanding. It also aligns with our goal to maintain a logical separation of data, while still ensuring strong connections between related information. Moreover, it provides the flexibility needed to allow for future expansion as business requirements evolve. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/187641c7-ad94-44c3-93a3-8d36883b11ad)

3. Data Model Components 
Our data warehouse design encompasses multiple fact tables, each serving a distinct role in capturing and analyzing key aspects of airline operations. Here's an overview of the fact tables and how they contribute to business insights. 


Flight Activity Trip 
The Flight Activity Trip fact table provides detailed information about flight trips (flight segments grouped into full trips) and related metrics. It includes data on origin and destination airports, booking channels, passenger profiles, and various financial elements like fare revenue, taxes, and fees. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/05121631-52b6-440b-a4eb-e7453dc3c636)

Reservations Fact 
The Reservations Fact table captures comprehensive reservation details, including passenger data, origin and destination airports, aircraft types, and class of service. It provides a detailed view of how reservations are made and the financial implications. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/ce6b2438-2f0a-45df-8f1e-5be91119aa62)

Flight Revenue Fact 
The Flight Revenue Fact table focuses on the revenue aspects of individual flights, it’s a daily periodic snapshot fact table, tracking flights info 90 days before takeoff, including unearned revenue and the number of remaining seats by class. It helps the airline track revenue generation and seat capacity utilization. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/bfdb8ecb-0290-46cd-9865-1086ae20c2ca)


Customer Interaction 
The Customer Interaction fact table captures various interactions between the airline and its customers, including inquiries, complaints, and feedback. This table is crucial for analyzing customer service quality and understanding passenger satisfaction. 

![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/665fb8e9-e25d-4d2f-b6da-8f6bcad8d35a)

Segment Level Flight Activity: 
The Segment Level Flight Activity Fact table provides granular insights into flight segments, capturing segment-specific information such as departure and arrival times, passenger data, and various financial metrics. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/e388cadb-5fce-4991-b88c-d53355dcd020)

Frequent Flyer Points 
The Frequent Flyer Points fact table tracks the activities of the airline's loyalty program. It helps monitor points accumulation, redemptions, and total points earned by frequent flyers.
Passenger Tier Data (Factless) 
The Passenger Tier Data factless fact table tracks changes in passenger tiers and related activities. This table is used to analyze passenger tier upgrades and other tier-related interactions. 
 ![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/6d7dae29-3286-4ca5-a841-c4516568754e)

Physical Model
Table Structure
In the Excel-based physical model, each sheet represents a table in the data warehouse. The structure includes:
•	Table Name: The name of the table as implemented in the database.
•	Columns: A list of columns with their data types, sizes, and constraints.
•	Primary Keys: The columns that form the primary key for each table.
•	Foreign Keys: The relationships between tables, showing which columns are used as foreign keys.
•	Indexes: A list of indexes, including primary, composite, and bitmap indexes.
![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/99e31152-5809-4eb7-af70-f149b68ea962)
![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/8f43eec3-b992-4b4f-bc26-11297d8613ab)
![image](https://github.com/RadwaEsamiel/AirOps-Data-Warehouse/assets/151566696/f0a77e60-c1ef-4ed5-8e2d-e4894bcb36a6)

Indexes and Their Usage
Indexes are a critical component of the physical model, as they improve query performance and data retrieval efficiency. Here's an overview of the possible indexes and how they are used in the data warehouse:

•	Primary Indexes: These are created on the primary keys of the tables, ensuring unique identification for each record and enabling fast lookups. For example, the Passenger Tier Data table has a composite primary index on the following columns: Passenger Key, Date Key, Time Key, Passenger Profile Key, and Tier Change Key.
•	Composite Indexes: Composite indexes are used to improve query performance for multi-column searches. For example, the Frequent Flyer Points table has a composite index on Passenger Key, Passenger Profile Key, Date Key, Time Key, and Points Activity Key.
•	Bitmap Indexes: Bitmap indexes are ideal for columns with low cardinality. They offer efficient filtering and can significantly improve the performance of complex queries. In our physical model, bitmap indexes are used on Frequent Flyer Status, Tier Name, and Day Time, as these columns have a limited set of unique values.

