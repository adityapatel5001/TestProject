import requests
import os
import sys

url = os.environ.get(
    "HEALTH_CHECK_URL",
    "http://localhost:8000/health"
)

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("Health check passed: The application is healthy.")
        sys.exit(0)

    else:
        print(
            f"Health check failed: "
            f"Received status code {response.status_code}."
        )
        sys.exit(1)

except requests.exceptions.RequestException as e:
    print(f"Health check failed: {e}")
    sys.exit(1)