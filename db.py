import pymysql

conn = pymysql.connect(
    host='localhost',
    user='flask_user',
    password='flaskpass123',
    database='role_auth'
)

print("✅ Connection successful!")
