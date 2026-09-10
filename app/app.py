from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/items/")
def create_item(item: dict):
    # Here you would typically save the item to your database or data store
    return {"item": item}








