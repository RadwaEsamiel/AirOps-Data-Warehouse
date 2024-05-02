# AirOps-Data-Warehouse
Airline Data Warehouse Project - README
Project Overview
This project involves the design and implementation of a data warehouse for an airline company to support analytical processing and business insights. The data warehouse is structured using a star schema design, providing a scalable and efficient framework for storing and analyzing data related to flight operations, reservations, flight revenue, customer interactions, and frequent flyer programs.

Business Processes Covered
The data warehouse supports various business processes crucial to airline operations. These processes include:

Flight Activity: Detailed information about flight segments, including departure and arrival times, trip duration, and operational metrics.
Reservations: Data related to passenger reservations, booking channels, fare types, and revenue.
Flight Revenue: Information on flight-based revenue, unearned revenue, remaining seats by class, and cancelled reservations.
Frequent Flyer Program: Points accumulation, tier levels, and points transactions related to the frequent flyer program.
Customer Interaction: Records of customer inquiries, complaints, feedback, and other interactions.
Passenger Tier Changes: Data tracking changes in passenger tiers, including upgrades and other tier-related events.
Data Warehouse Structure
The data warehouse is built using a star schema design, with fact tables at the center and dimension tables providing context. The primary tables in the data warehouse include:

Fact Tables: Flight Activity Trip, Reservations, Flight Revenue, Frequent Flyer Points, Customer Interaction, Passenger Tier Data (Factless), and Segment Level Flight Activity.
Dimension Tables: Passenger, Date, Time, Passenger Profile, Communication Channel, Interaction Type, and more.
The structure supports a variety of queries for business analysis and allows for flexible expansion as business needs evolve.

Technologies Used
The data warehouse is implemented using Oracle Database, which offers robust features for data warehousing and business intelligence. Oracle's support for partitioning, indexing, and query optimization helps ensure high performance and scalability. Additionally, the data warehouse integrates with various ETL processes and OLAP tools for analytical processing.

Key Queries for Business Insights
The following queries were executed to gain insights from the data warehouse:

Fully Booked Flights: Identifies flights that are fully booked 30 days before takeoff, showing airplane models, destination airports, and revenue generated.
Revenue from Flights Back Home: Calculates revenue from flights heading back to passengers' home airports, useful for understanding travel patterns.
Information Related to Flight Segment: Displays information about one flight segment, including frequent flyer status, base fare, and class of service flown.
Average Duration of Overnight Stays by Frequent Flyer Status: Calculates the average duration of overnight stays for passengers, grouped by frequent flyer status.
Proportion of Frequent Flyers That Upgrade with Specific Status: Determines the proportion of frequent flyers who upgrade and have gold, platinum, or titanium status.


