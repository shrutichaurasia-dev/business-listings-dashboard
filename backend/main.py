import random
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI() 

cities = ["Lucknow", "Delhi", "Mumbai", "Pune", "Bangalore"]

categories = ["Restaurant", "Hospital", "School", "Gym", "Cafe"]

sources = ["Google", "Justdial", "Sulekha"]

businesses = []

for i in range(500):

    business = {
        "name": f"Business {i+1}",
        "category": random.choice(categories),
        "city": random.choice(cities),
        "source": random.choice(sources)
    }

    businesses.append(business)

conn = sqlite3.connect("business.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS listing_master (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    city TEXT,
    source TEXT
)
""")

conn.commit()

cursor.execute("DELETE FROM listing_master")
conn.commit()

for business in businesses:

    cursor.execute("""
    INSERT INTO listing_master (name, category, city, source)
    VALUES (?, ?, ?, ?)
    """, (
        business["name"],
        business["category"],
        business["city"],
        business["source"]
    ))

conn.commit()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}
    
@app.get("/city-count")
def city_count():
    cursor = conn.cursor()

    cursor.execute("""
    SELECT city, COUNT(*)
    FROM listing_master
    GROUP BY city
    """)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "city": row[0],
            "count": row[1]
        })

    return result

@app.get("/category-count")
def category_count():
    
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, COUNT(*)
    FROM listing_master
    GROUP BY category
    """)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "category": row[0],
            "count": row[1]
        })

    return result

@app.get("/source-count")
def source_count():
    
    cursor = conn.cursor()

    cursor.execute("""
    SELECT source, COUNT(*)
    FROM listing_master
    GROUP BY source
    """)

    data = cursor.fetchall()

    result = []

    for row in data:
        result.append({
            "source": row[0],
            "count": row[1]
        })

    return result