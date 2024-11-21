from fastapi import FastAPI
from routers import category, products

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My shop"}

# Подключаем маршруты из category
app.include_router(category.router)
# app.include_router(products.router)
