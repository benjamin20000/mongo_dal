import os


USERNAME = os.getenv("MONGODB_USER", "benny")
DB_PASSWORD = os.getenv("MONGODB_PASSWORD", 1234)
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_NAME = os.getenv("MONGODB_DATABASE", "enemy_soldiers")