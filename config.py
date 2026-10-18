
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        if os.environ.get("FLASK_ENV") == "production":
            raise RuntimeError(
                "SECRET_KEY must be configured in production."
            )
        SECRET_KEY = "dev-only-change-this-secret-key"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///tnp_connect.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
