import psutil
import time

def monitor_server_health(interval=5, threshold_cpu=80, threshold_memory=80, threshold_disk=90):
    """
    Monitors server health and performance metrics.

    Args:
        interval (int): Time in seconds between monitoring checks.
        threshold_cpu (int): CPU usage percentage threshold for alerts.
        threshold_memory (int): Memory usage percentage threshold for alerts.
        threshold_disk (int): Disk usage percentage threshold for alerts.
    """
    print("Starting server health monitoring...")
    print(f"Monitoring interval: {interval} seconds")
    print(f"CPU alert threshold: {threshold_cpu}%")
    print(f"Memory alert threshold: {threshold_memory}%")
    print(f"Disk alert threshold: {threshold_disk}%")
    try:
        while True:
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)

            # Get memory usage
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent

            # Get disk usage for the root partition
            disk_usage = psutil.disk_usage('/')
            disk_percent = disk_usage.percent

            print(f"\n--- Server Health Report ({time.strftime('%Y-%m-%d %H:%M:%S')}) ---")
            print(f"CPU Usage: {cpu_percent:.2f}%")
            print(f"Memory Usage: {memory_percent:.2f}%")
            print(f"Disk Usage ('/'): {disk_percent:.2f}%")

            # Check for alerts
            if cpu_percent > threshold_cpu:
                print(f"ALERT: High CPU usage detected: {cpu_percent:.2f}%")
            if memory_percent > threshold_memory:
                print(f"ALERT: High Memory usage detected: {memory_percent:.2f}%")
            if disk_percent > threshold_disk:
                print(f"ALERT: High Disk usage detected: {disk_percent:.2f}%")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user. Exiting safely...")

if __name__ == "__main__":
    # You can customize the monitoring interval and thresholds here
    monitor_server_health(interval=10, threshold_cpu=100, threshold_memory=100, threshold_disk=100)