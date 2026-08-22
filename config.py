class Config:

    SECRET_KEY = "quizsecret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///quiz.db"

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = "your_email@gmail.com"
    MAIL_PASSWORD = "your_app_password"