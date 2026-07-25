from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import AsyncSessionLocal

app = FastAPI()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "Success", "message": "PostgreSQL is connected!"}
    except Exception as e:
        return {"status": "Failed", "error": str(e)}