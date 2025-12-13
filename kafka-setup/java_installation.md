# Java Installation Guide for Apache Kafka on Azure VM

## 1. Overview
Apache Kafka runs on the Java Virtual Machine (JVM) because Kafka is built using Java and Scala.
To deploy a reliable Kafka Cluster on an Azure Virtual Machine (JVM), installing the correct Java version in a production-grade manner is essential.

This guide documents:
- Why Kafka requires Java
- Recommended Java versions for Kafka 3.x/4.x
- Step-by-step installation of OpenJDK 17 on Linux
- Setting up JAVA_HOME for Kafka services

## 2. Why Java is Required for Kafka
Kafka cannot run without Java:
- Kafka Broker runs as a JVM application
- Java provides high-performance features
- Kafka ecosystem tools require Java

## 3. Recommended Java version (Production Standard)
Kafka supports multiple Java versions, but the recommeneded production version is:
- OpenJDK 17(LTS) - Best choice for Kafka 3.x and 4.x

## 4. Install Java (OpenJDK 17) on Ubuntu VM

### 4.1 Update system packages
```bash
sudo apt update && sudo apt upgrade -y
```

### 4.2 Install OpenJDK 17
```bash
sudo apt install openjdk-17-jdk -y
```

### 4.3 Verify installation
```bash
java -version
```

## 5. Configure JAVA_HOME (Required for Kafka)
