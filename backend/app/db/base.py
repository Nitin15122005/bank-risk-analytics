from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import all models after Base is defined so Alembic can discover them.
from app.models.branch import Branch  # noqa: E402,F401
from app.models.customer import Customer  # noqa: E402,F401
from app.models.loan import Loan  # noqa: E402,F401
from app.models.user import User  # noqa: E402,F401