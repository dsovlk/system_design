```mermaid
graph TB
    subgraph DC1["Datacenter 1"]
        subgraph "Load Balancer 1"
            LB1[Load Balancer]
        end

        subgraph "Application Layer 1"
            API1[API Server]
            Cache1[Cache Layer]
        end

        subgraph "Storage Layer 1"
            Master1[(Master Node)]
            Replica1_1[(Replica Node 1)]
            Replica1_2[(Replica Node 2)]
        end
    end

    subgraph DC2["Datacenter 2"]
        subgraph "Load Balancer 2"
            LB2[Load Balancer]
        end

        subgraph "Application Layer 2"
            API2[API Server]
            Cache2[Cache Layer]
        end

        subgraph "Storage Layer 2"
            Master2[(Master Node)]
            Replica2_1[(Replica Node 1)]
            Replica2_2[(Replica Node 2)]
        end
    end

    subgraph "Client Layer"
        Client[Client Application]
    end

    subgraph "Global Load Balancer"
        GLB[Global Load Balancer]
    end

    subgraph "Monitoring"
        Monitor[Global Monitoring System]
    end

    %% Client to Global Load Balancer
    Client --> GLB

    %% Global Load Balancer to Datacenter Load Balancers
    GLB --> LB1
    GLB --> LB2

    %% Datacenter 1 connections
    LB1 --> API1
    API1 --> Cache1
    API1 --> Master1
    API1 --> Replica1_1
    API1 --> Replica1_2

    %% Datacenter 2 connections
    LB2 --> API2
    API2 --> Cache2
    API2 --> Master2
    API2 --> Replica2_1
    API2 --> Replica2_2

    %% Cross-datacenter replication
    Master1 --- Master2
    Replica1_1 --- Replica2_1
    Replica1_2 --- Replica2_2

    %% Monitoring connections
    Monitor --> API1
    Monitor --> API2
    Monitor --> Cache1
    Monitor --> Cache2
    Monitor --> Master1
    Monitor --> Master2
    Monitor --> Replica1_1
    Monitor --> Replica1_2
    Monitor --> Replica2_1
    Monitor --> Replica2_2

    %% Styling
    classDef primary fill:#f9f,stroke:#333,stroke-width:2px,color:#000
    classDef secondary fill:#bbf,stroke:#333,stroke-width:2px,color:#000
    classDef storage fill:#bfb,stroke:#333,stroke-width:2px,color:#000
    classDef monitoring fill:#fbb,stroke:#333,stroke-width:2px,color:#000

    class Client,GLB primary
    class API1,API2,Cache1,Cache2 secondary
    class Master1,Master2,Replica1_1,Replica1_2,Replica2_1,Replica2_2 storage
    class Monitor monitoring
```

# Multi-Datacenter Key-Value Store System Design

This diagram illustrates a distributed key-value store system with multiple datacenters and cross-datacenter replication.

## Components

1. **Client Layer**
   - Client applications that interact with the system

2. **Global Load Balancer**
   - Routes requests to appropriate datacenter
   - Handles geographic load balancing
   - Provides disaster recovery capabilities

3. **Datacenter Components**
   Each datacenter contains:
   - **Load Balancer**: Distributes requests within the datacenter
   - **Application Layer**:
     - API Server: Handles client requests and business logic
     - Cache Layer: Improves read performance with in-memory caching
   - **Storage Layer**:
     - Master Node: Handles write operations and data consistency
     - Replica Nodes: Provide read scalability and data redundancy

4. **Cross-Datacenter Replication**
   - Synchronous replication between master nodes
   - Asynchronous replication between replica nodes
   - Ensures data consistency across datacenters

5. **Global Monitoring System**
   - Tracks system health and performance across all datacenters
   - Monitors replication status and latency
   - Provides global system visibility

## Key Features

- **Multi-Datacenter Architecture**: Ensures high availability and disaster recovery
- **Cross-Datacenter Replication**: Maintains data consistency across regions
- **Geographic Distribution**: Reduces latency for global users
- **High Availability**: Multiple replicas within and across datacenters
- **Scalability**: Horizontal scaling through multiple nodes and datacenters
- **Consistency**: Master-replica architecture with cross-datacenter replication
- **Performance**: Local caching and geographic load balancing
- **Monitoring**: Comprehensive global system monitoring 