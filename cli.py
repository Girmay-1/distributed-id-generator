import argparse
from snowflake import Snowflake
from benchmark import benchmark

def main():
    parser = argparse.ArgumentParser(description="Snowflake ID Generator")
    parser.add_argument('--datacenter', type=int, default=1, help="Datacenter ID")
    parser.add_argument('--worker', type=int, default=1, help="Worker ID")
    parser.add_argument('--count', type=int, default=1, help="Number of IDs to generate")
    parser.add_argument('--benchmark', action='store_true', help="Run benchmark")
    
    args = parser.parse_args()
    
    if args.benchmark:
        benchmark()
    else:
        snowflake = Snowflake(datacenter_id=args.datacenter, worker_id=args.worker)
        for _ in range(args.count):
            print(snowflake.generate_id())

if __name__ == '__main__':
    main()
