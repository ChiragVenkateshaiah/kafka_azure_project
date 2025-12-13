# ZooKeeper Service Configuration (Kafka Dependency)

## 1. Overview
This document describes the configuration and management of Apache ZooKeeper as a systemd service on an Ubuntu-based Azure Virtual Machine.

ZooKeeper is used by Apache Kafka to:
- Maintain cluster metadata
- Coordinate brokers
- Manage leader elections and topic state


## 2. Prerequisites
Ensure the following steps are completed before configuring ZooKeeper:
- Apache Kafka installed
Refer: kafka_installation.md
- Java 17 installed and configured
Refer: /prerequisites/java_installation.md
- Dedicated Kafka user created
- Kafka binaries available at /opt/kafka

## 3. ZooKeeper Data Directory Setup
ZooKeeper requires a persistent data directory to store:
- Snapshots
- Transaction logs

### 3.1 Create ZooKeeper data directory
```bash
sudo mkdir -p /var/lib/zookeeper # Standard Linux location for service state data
sudo chown -R kafka:kafka /var/lib/zookeeper # change ownership to kafka user
```
## 4. ZooKeeper Configuration File
Kafka ships with a default ZooKeeper configuration file

### 4.1 Update zookeper.properties
```bash
sudo nano /opt/kafka/config/zookeeper.properties
```
**add the properties**
```ini
dataDir=/var/lib/zookeeper
clientPort=2181
maxClientCnxns=60
```
## 5. systemd Service Configuration
To ensure ZooKeeper starts automaticaly and runs reliably, configure it as a **systemd service**.

### 5.1 Create ZooKeeper service file
```bash
sudo nano /etc/systemd/system/zookeeper.service
```

