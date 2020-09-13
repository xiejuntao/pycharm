import redis

r = redis.StrictRedis(host='localhost',port=6379,db=0,decode_responses=True)
r.set('a','岁月长')
print(r.get('a'))