# Data Generator for Kafka

This module contains Python scripts that:
1. Read data from a CSV file.
2. Process/transform the data.
3. Produce messages to Kafka for testing the streaming pipeline.

## 📁 Directory Contents

- **generate_data.py** — Reads and processes CSV records.
- **produce_to_kafka.py** — Publishes processed records to Kafka.
- **sample_data.csv** — Example dataset used for local or VM testing.
- **README.md** — Documentation for running and deploying the data generator.
