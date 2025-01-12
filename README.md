# Real-Time Stock Market Data Pipeline and Analytics Using Kafka and AWS

## Description

This project demonstrates a scalable and efficient **Real-Time Stock Market Data Pipeline** using **Apache Kafka** and **AWS Services**. The system simulates real-time stock market data, processes events, and provides analytics-ready datasets.

### Key Features:
- **Real-Time Data Streaming**: Stock market data simulation and event publishing to an **Apache Kafka** broker hosted on an **AWS EC2 instance**.
- **Data Ingestion and Storage**: Streamed events are stored in **Amazon S3**, ensuring durability and accessibility.
- **Automated Schema Inference**: Leveraged **AWS Glue Crawler** to build a **Glue Data Catalog** for schema automation and seamless data exploration.
- **SQL-Based Analytics**: Used **Amazon Athena** for querying and analyzing stock market data, enabling real-time insights.

This end-to-end data pipeline integrates event streaming, storage, and analytics to demonstrate the power of real-time data engineering and processing.

## Architecture
![Project Architecture](Architecture.jpg)

## Technology Used

### Programming Language:
- Python

### Amazon Web Services (AWS):
1. **S3**: Data storage.
2. **Athena**: SQL-based analytics.
3. **Glue Crawler**: Automated schema inference.
4. **Glue Catalog**: Unified metadata management.
5. **EC2**: Kafka broker hosting.
6. **Apache Kafka**: Real-time event streaming.

---

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/akhilrathod09/Real-Time-Stock-Market-Data-Pipeline-and-Analytics-Using-Kafka-and-AWS.git
