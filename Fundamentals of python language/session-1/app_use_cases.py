#task-3:  app_use_cases.py

use_cases = [
    {
        "app": "Instagram",
        "python_use": "Backend web services (using Django at scale) and ML recommendation algorithms for Reels and feed posts."
    },
    {
        "app": "Spotify",
        "python_use": "Data analytics, backend microservices, and personalized recommendation systems like Discover Weekly."
    },
    {
        "app": "Uber / Zomato",
        "python_use": "Predictive analytics and machine learning models for dynamic surge pricing, estimated arrival times (ETA), and route optimization."
    }
]


print("--- Real-Life App Use Cases of Python ---")
for entry in use_cases:
    print(f"App: {entry['app']}")
    print(f"Python Application: {entry['python_use']}\n")