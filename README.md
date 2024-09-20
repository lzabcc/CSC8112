Project Overview

This project focuses on the collection, processing, prediction, and visualization of PM2.5 data within an IoT environment. It includes collecting data from sensors, publishing the data to an edge virtual machine via the EMQX server, cleaning and calculating daily average values, and then sending the cleaned data to a cloud virtual machine for visualization and future value prediction.

Key Achievements

Data Collection: Collected PM2.5 data from June 1, 2023, to August 31, 2023.

Data Processing: Performed data cleaning and preliminary processing at the edge level, including filtering out outliers and calculating the average PM2.5 value.

Machine Learning: Utilized the Prophet model for time series analysis to predict future PM2.5 concentration trends.

Visualization: Created charts using Matplotlib to display historical data and prediction results.

Implementation Details
The project was implemented through the following steps:

Design of Data Injection Component:

Pulled and ran the EMQX message broker server via Docker.
Wrote a publisher program that retrieves PM2.5 data from the Urban Observatory platform and sends it through the EMQX server.
Cleaned the data, retaining only PM2.5-related information.
Launched the publisher program to send data to the EMQX server.

Design of Data Preprocessing Operations:

Wrote a subscriber program on the edge virtual machine to receive PM2.5 data and print it to the console.
Cleaned the data and calculated the average PM2.5 value.
Wrote Dockerfile and docker-compose configuration files to build and run the data preprocessing service.
Pulled and ran the RabbitMQ message queue service.
Wrote a producer program to send data to the RabbitMQ server in the cloud.

Time Series Data Prediction and Visualization:

Wrote a consumer program to retrieve data from RabbitMQ.
Used charting tools to visualize the data stored in RabbitMQ.
Passed the data to the machine learning component for prediction.
Displayed the prediction results graphically.

Technologies Used

Docker: For containerized deployment of components. 

EMQX: Message queuing service supporting the MQTT protocol. 

RabbitMQ: Reliable and efficient data communication between cloud and edge. 

Python: Scripting language for data handling and machine learning. 

Prophet: Time series prediction model. 

Matplotlib: Library for data visualization. 

![PM25_data](https://github.com/user-attachments/assets/fc65ad72-6e69-42a4-916e-9e72726e7de6)
![prediction](https://github.com/user-attachments/assets/a02bb296-337e-4c29-8175-06e042a8e79c)

