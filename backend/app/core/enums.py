from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    RISK_ANALYST = "risk_analyst"