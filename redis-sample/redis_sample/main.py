


import redis


client: redis.Redis = redis.Redis(host='localhost', port=6379, decode_responses=True)



client.set('foo', 'bar')



client.get('foo')