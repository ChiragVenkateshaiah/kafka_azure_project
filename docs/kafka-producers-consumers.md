# Kafka Producers and Consumers - Usage Guide

## Overview

This document explains how to produce and consume messages using Apache Kafka via  command-line tools. These commands are useful for:
- Verifying Kafka Cluster health
- Testing topics
- Debugging producers and consumers
- Learning Kafka message flow

Kafka is installed and managed via systemd on an Ubuntu VM.

## Prerequisites
Ensure the following services are running:
```bash
sudo systemctl status zookeeper
sudo systemcctl status kafka
```
Both services must be in active(running) state

## Kafka CLI Location
`/opt/kafka/bin`

## Topic Management
### List Existing Topics
```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### Create a Topic
```bash
kafka-topics.sh\
    --bootstrap-server localhost:9092 \
    --create \
    --topic demo-topic \
    --partitions 3 \
    --replication-factor 1
```
### Describe a Topic
```bash
kafka-topics.sh \
    --bootstrap-server localhost:9092 \
    --describe \
    --topic demo-topic
```

## Producing Messages
### start a Console Producer
```bash
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic demo-topic
```
After running the command:
- Types messages in the terminal
- Press Enter to send
- Each line is sent as a separate Kafka message
- CTRL + C to stop the producer

## Consuming Messages
### Start a Console Consumer (Latest Messages)
```bash
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic demo-topic
```
This consumer:
- Reads only new messages
- Does not read exisiting data

### Consume From Beginnning
```bash
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic demo-topic \
    --from-beginning
```
This is useful for:
- Debugging
- Replaying events
- Verifying message retention

## Consumer with Consumer Group
```bash
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic demo-topic \
    --group demo-consumer-group
```
Kafka will:
- Track offsets for the group
- Resume from last committed offset

## Viewing Consumer Group
### List Consumer Groups
```bash
kafka-consumer.groups.sh \
    --bootstrap-sever localhost:9092 \
    --list
```
### Describe a Consumer Group
```bash
kafka-consumer-group.sh \
    --bootstap-server localhost:9092 \
    --describe \
    --group demo-consumer-group
```
This shows:
- Partition assignments
- Current offsets
- Lag per partition