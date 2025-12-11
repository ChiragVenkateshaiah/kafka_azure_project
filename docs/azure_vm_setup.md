# Azure VM Setup Guide for Kafka Infrastructure

## 1. Overview
This document explains the step-by-step process of provisioning and configuring Azure Virtual Machines used for setting up the Kafka ecosystem in this project. The goal is to ensure the environment can be consistently recreated by any developer or DevOps Engineer

## 2. Architecture Overview
The infrastructure consists of:
- **Kafka Server VM**
- **Zookeeper VM** (if not using KRaft mode)
- **Application VM** (for producers/consumer, Flask API)

Each VM is deployed inside a Virtual Network with restricted network access.

## 3. VM Specifications

| Component | Value |
|----------|-------|
| Resource Group | `rg-kafkastreaming-southindia` |
| Region | `Central India` |
| VM Size | `Standard D2s v5 (2 vcpus, 8 GiB memory)` |
| OS | Linux (ubuntu 24.04) or latest |
| Authentication | username and password |
| Disk Type | Standard SSD (64GB) |
| Network | `dev-kafka-server-southindia-vnet` / `default` |
| Application Port | `5000` |

----

## 4. Networking Configuration

| Setting | Description |
|--------|-------------|
| VNet | `dev-kafka-server-southindia-vnet` |
| Subnet | `default` |
| Private IP | Assigned automatically |
| Public IP | Used for username (development only) |
| NSG Rules | Allow inbound ports: **22 (username)**, **5000 (Flask API)** |

**Production Note:**
The Flask API should run behind:
- Azure Application Gateway **or**
- NGINX reverse proxy

Avoid exposing port 5000 publicly in production environments.

---

## 5. Creating the VM (Azure Portal)

1. Navigate to **Azure Portal → Virtual Machines → Create**.
2. Choose **Ubuntu Server 22.04 LTS**.
3. Select a VM size: **Standard_B1ms** or **Standard_B2s**.
4. Under **Authentication**, choose *SSH key*.
5. Under **Networking**:
   - VNet: ``dev-kafka-server-southindia-vnet``
   - Subnet: `default`
   - Create an inbound rule for **TCP 5000**.
6. Keep defaults for disk and management settings.
7. Click **Review + Create**.

## 6. Connect to the VM

Use the PuTTY to connect VMs' servers
1. copy paste the IP addresses of the VMs from the portal
2. login via username and password given at the time of creating the VMs

## 7. Post-Deployement Configuration

Update system packages
```bash
sudo apt update
sudo apt install openjdk-11-jdk
tar -xzf kafka_2.13-3.6.0.tgz
cd kafka
```

# Azure VM Setup Guide for Flask API Infrastructure

## 1. Overview
This document explains the step-by-step process of provisioning and configuring Azure Virtual Machines used for setting up the Kafka ecosystem in this project. The goal is to ensure the environment can be consistently recreated by any developer or DevOps Engineer

## 2. Architecture Overview
The infrastructure consists of:
- **Flask API Server VM** - Runs the Flask application that produces data.
- **Kafka Server VM** - Receives data produced by the API (Optional reference).
- **Zookeeper VM** (if not using KRaft mode).
- **Virtual Network (VNet)** - Ensures secure internal communication.
- **Network Security Groups (NSG)** - Controls external access to API endpoints.
- **Application VM** (for producers/consumer, Flask API).

Each VM is deployed inside a Virtual Network with restricted network access.

## 3. VM Specifications

| Component | Value |
|----------|-------|
| Resource Group | `rg-kafkastreaming-southindia` |
| Region | `Central India` |
| VM Size | `Standard D2s v5 (2 vcpus, 8 GiB memory)` |
| OS | Linux (ubuntu 24.04) or latest |
| Authentication | username and password |
| Disk Type | Standard SSD (64GB) |
| Network | `dev-kafka-server-southindia-vnet` / `default` |

## 4. Networking Configuration

| Setting | Description |
|--------|-------------|
| VNet | `dev-kafka-server-southindia-vnet` |
| Subnet | `default` |
| Private IP | Assigned automatically |
| Public IP | Used for username (development only) |
| NSG Rules | Allow inbound ports: 22, 9092, 2181 |

**Production Note:**
Kafka should not expose ports to the internet. Restrict access to VNET-only.

---

## 5. Creating the VM (Azure Portal)

1. Navigate to **Azure Portal → Virtual Machines → Create**.
2. Select:
   - **Image:** Ubuntu Server 22.04 LTS or Latest 
   - **Size:**  Standard D2s v5 (2 vcpus, 8 GiB memory) 
3. Under **Administrator Account**, choose *username and password*.
4. Configure Networking:
   - Select `dev-kafka-server-southindia-vnet`
   - Subnet: `default`
   - NSG: create inbound rules for required ports
5. Attach OS disk and tags.
6. Click **Review + Create**.

## 6. Connect to the VM

Use the PuTTY to connect VMs' servers
1. copy paste the IP addresses of the VMs from the portal
2. login via username and password given at the time of creating the VMs

## 7. Post-Deployement Configuration

1. mkdir project <!-- creating a directory "project" inside the FastAPI VM -->
2. mkdir python <!-- createing another folder to specify that python code will be moved/created there -->
3. login to the server using WinSCP <!-- enter the required creds to login -->
4. copy the files using the WinSCP GUI <!-- this way is easier is what I feel -->
5. use the permission grant bash command `sudo chmod -R 777 <path>` <!-- use VM's terminal to grant this access -->
6. check the python code `sudo nano <name of the file>` <!-- make sure right targeting the right file -->
7. check all the modules updated `sudo apt update` <!-- This woudl make sure the modules updated -->
8. Install python `sudo apt install python3` <!-- This ensures that the python3 is installed, accessible system-wide, dependencies are present>
9. Install Flask web framework `sudo pip3 install Flask` <!-- This installs the Flask web framework -->
10. For best pratice install Flask/FastAPI on venv <!-- This virtual environment keeps the project isolated, safely, reproducible, cleaner workflow and no sudo needed for installation>
11. Install pandas `sudo pip3 install pandas` <!-- This installs pandas -->

## 8. Validation & Testing

1. verify Python Installation
```bash
python3 --version
pip3 --version
```
2. verify Flask installation
```bash
python3 -c "import flask; print(flask.__version__)"
```
3. start the Flask application
```bash
python3 file_name.py
```
4. test ingestion
```bash
curl <IP Address> /api/data # this shows the individual row reading at the output with status code 200 on the application session
```

Update system packages
```bash
sudo apt update
sudo apt install openjdk-11-jdk
tar -xzf kafka_2.13-3.6.0.tgz
cd kafka
