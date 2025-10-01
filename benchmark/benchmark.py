import csv
import time
import requests
import statistics

USE_HTTP = True
API_URL = "https://your-app.onrender.com/mediate"  # change to cloud URL

def benchmark(csv_file):
    latencies = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = time.time()
            if USE_HTTP:
                r = requests.post(API_URL, json={
                    "name": row["Restaurant Name"],
                    "location": row["Location"],
                    "cuisines": row["Cuisines"],
                    "avg_cost_for_two": float(row["Average Cost for two"]),
                    "rating": float(row["Aggregate rating"])
                })
                r.raise_for_status()
            else:
                # Local in-process mediation (optional)
                data = {
                    "name": row["Restaurant Name"][0] + "***" + row["Restaurant Name"][-1],
                    "location": row["Location"],
                    "cuisines": row["Cuisines"],
                    "avg_cost_for_two": float(row["Average Cost for two"]),
                    "rating": float(row["Aggregate rating"])
                }
            end = time.time()
            latencies.append((end - start) * 1000)
    print("Mean latency:", statistics.mean(latencies))
    print("p50 latency:", statistics.median(latencies))
    print("p90 latency:", statistics.quantiles(latencies, n=10)[8])
    print("p95 latency:", statistics.quantiles(latencies, n=20)[18])
    print("p99 latency:", statistics.quantiles(latencies, n=100)[98])

if __name__ == "__main__":
    benchmark("../data/zomato.csv")
