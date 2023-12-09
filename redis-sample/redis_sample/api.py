


import json
import fastapi
import uvicorn
import redis
import redis.exceptions
import pymongo



app: fastapi.FastAPI = fastapi.FastAPI()
redis_client: redis.Redis = redis.Redis(host='localhost', port=6379, decode_responses=True)


@app.get('/')
async def index():
    return {'message': 'Hello, World!'}

@app.get('/{id}')
async def get_item(id: int):
    if type(id) == str:
        id = int(id)

    try:
        if (data := redis_client.get(id)):
            # print("data from redis")
            return json.loads(data)
    except redis.exceptions.ConnectionError as ex:
        pass
        # print(ex)

    # print("data from mongo")
    connection_string: str = "mongodb://admin:password123@localhost:27017"
    mongo_client = pymongo.MongoClient(connection_string)
    db = mongo_client["redis-sample"]
    collection = db["data"]

    cursor = collection.find_one({"product.id": id}, {"_id": 0})

    # print(cursor)

    if not cursor:
        raise fastapi.exceptions.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    # redis_client.set(id, json.dumps(cursor))

    return cursor


if __name__ == '__main__':
    uvicorn.run(app="api:app", host='0.0.0.0', port=3000, reload=True)