import redis

class RedisHelper:
    
    @staticmethod
    def convert_redis_to_json(_redis: redis, _dict):
        return [eval(x.decode('utf-8')) for x in _redis.hgetall(_dict).values()]
