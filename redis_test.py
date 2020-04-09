import redis
conn = redis.Redis('localhost')

user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}
user1 = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}

conn.hmset("pythonDict", user)
conn.hmset("pythonDict1", user1)

print(conn.hgetall("pythonDict"))
print(conn.hgetall("pythonDict1"))
print(conn.hgetall())
