# Distributed Unique ID Generator

This project implements a distributed unique ID generator based on Twitter's Snowflake algorithm. It generates 64-bit numeric IDs that are unique across a distributed environment.

## Features

- 64-bit numeric IDs
- Distributed environment support
- No collisions
- Can generate at least 10,000 IDs per second

## How It Works

The ID is composed of:

- Timestamp (41 bits): Milliseconds since the epoch or custom epoch
- Datacenter ID (5 bits): Allows for 32 datacenters
- Worker ID (5 bits): Allows for 32 workers per datacenter
- Sequence number (12 bits): Allows for 4096 IDs per millisecond per worker

## Usage

```python
from snowflake import Snowflake

# Create a Snowflake instance with datacenter_id and worker_id
snowflake = Snowflake(datacenter_id=1, worker_id=1)

# Generate a unique ID
unique_id = snowflake.generate_id()
print(unique_id)
```

## Running Tests
To run the unit tests:

python -m unittest discover tests

## Benchmarking

To run the performance benchmark:

python benchmark.py


## Command-line Interface

Generate IDs:

python cli.py --datacenter 1 --worker 1 --count 5