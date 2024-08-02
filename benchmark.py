import time
from snowflake import Snowflake

def benchmark(duration_seconds=1):
    snowflake = Snowflake(datacenter_id=1, worker_id=1)
    start_time = time.time()
    count = 0
    
    while time.time() - start_time < duration_seconds:
        snowflake.generate_id()
        count += 1
        
    rate = count / duration_seconds
    print(f"Generated {count} IDs in {duration_seconds} seconds")
    print(f"Rate: {rate:.2f} IDs/second")

if __name__ == '__main__':
    benchmark()