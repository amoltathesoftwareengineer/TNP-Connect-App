
import os


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-only-change-this-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///tnp_connect.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
