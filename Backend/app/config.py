import os 
import dotenv import load_load_env
db_url = os.getenv("DATABASE_URL")
print(f"Connected to database at: {db_url}")