# Kafka User Management Guide
Part of the Kafka Infrastructure Setup on Azure

## 1. Overview
This document explains how Kafka users are created, configured, and managed inside the Kafka Sever VM
for this project.

Kafka user accounts are essential for:
- Securing cluster access
- Tracking operational activity
- Assigning role-based permissions
- Managing daily monitoring tasks

In this setup, a dedicated Linux user is created for Kafka operations, ensuring isloation from the root
account and following production-grade best practices.

## 2. Creating a Dedicated Kafka User on Linux VM

Why create a separate user?
- Prevents running Kafka as root(a major security risk)
- Helps assign file permissions cleanly
- Useful for logging, auditing, and monitoring
- Keeps system users organized

## 3. Steps to Create and Configure Kafka User

### 3.1 Create a new system user
```bash
sudo useradd -m kafka
```

### 3.2 Set password for the user
```bash
sudo passwd kafka
```

### 3.3 Assign sudo privileges (optional, only if needed for admin task)
```bash
sudo usermod -aG sudo kafka
```
Note: For production clusters, it is recommended not to give sudo to Kafka user unless required for operations

## 4. Setting Directory Permission

### 4.1 Change Kafka installation folder ownership
```bash
sudo chown -R kafka:kafka /opt/kafka
```
### 4.2 Change Zookeeper folder ownership (if co-hosted)
```bash
sudo chown -R kafka:kafka /var/lib/zookeeper
sudo chown -R kafka:kafka /opt/zookeeper

# This ensures Kafka processes run as the correct user:
sudo -u kafka bin/kafka-server-start.sh config/server.properties

```
## 5. Enabling Kafka User for Daily Monitoring Tasks

### 5.1 Switch to Kafka user
```bash
sudo su - kafka
```

### 5.2 Verify Kafka server status
```bash
ps -ef | grep kafka
```

### 5.3 Monitor Kafka logs
```bash
tail -f /opt/kafka/logs/server.logs
```

## 6. Auditing Kafka User Actions

### 6.1 View Kafka user's command history
```bash
sudo cat /home/kafka/.bash_history
```

### 6.2 Check authentication logs
```bash
sudo cat /var/log/auth.log
```

## 7. For automation: Bash Script

```bash
scripts/kafka/create_kafka_user.sh
```
```bash
#!/bin/bash

# Create kafka user
sudo useradd -m kafka

# Set ownership permissions
sudo chown -R kafka:kafka /opt/kafka
sudo chown -R kafka:kafka /var/lib/zookeeper

echo "Kafka user created and permission set."

# make it executable:
chmod +x scripts/kafka/create_kafka_user.sh

```
