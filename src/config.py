# Configuration Management

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///prod.db'