from fastapi import FastAPI

app = FastAPI()

@app.get("/{item_id}")
async def get_method(item_id: int):
    return {"item_id": item_id}

