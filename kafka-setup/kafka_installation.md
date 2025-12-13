# Apache Kafka Installation Guide (Ubuntu on Azure VM)

## 1. Overview
This document describes the step-by-step process to install Apache Kafka on an Ubuntu-based Azure Virtual Machine
The goal is to ensure a reproduction, production-aligned Kafka setup that can be reliably used for development, testing and leraning purposes.

Kafka is used in this project as the core distribution event-streaming platform for real-time data ingestion.

----

## 2. Prerequisites
Ensure the following prerequisites are completed before proceedings:
- Ubuntu 22.04 LTS Azure VM
- Java 17 installed and configured
Refer: [Java Installation Guide](/prerequisites/java_installation.md)
- Internet access from the VM

## 3. Kafka Version Selection
For this project, the following Kafka version is used:
- Apache Kafka: 3.6.x <!-- This ensure compatibility>
- Scala Version: 2.13

## 4. Download Apache Kafka
```bash
sudo wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz
```

## 5. Extract and Install Kafka
Extract the archive and move Kafka to a standard installation directory
```bash
tar -xvzf kafka_2.13-3.6.1.tgz
sudo mv kafka_2.13-3.6.1 /opt/kafka # Common industry-standard location for third-party software
```

## 6. Set Ownership and Permissions
Kafka should run under a dedicated Kafka user for security and isolation

```bash
sudo chown -R kafka:kafka /opt/kafka # This prevents running Kafka services as root, which is not recommended in production environments
```

## 7. Verify Kafka Installation
Switch to the Kafka user and verify the installation:
```bash
su - kafka
cd /opt/kafka
bin/kafka-topics.sh --version
```
