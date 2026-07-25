import os 
from dotenv import load_dotenv
load_dotenv()
# dotenv.load_dotenv()
db_url = os.getenv("DATABASE_URL")
print(f"Connected to database at: {db_url}")