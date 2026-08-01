from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    RISK_ANALYST = "risk_analyst"


class EmploymentTypeEnum(str, Enum):
    UNEMPLOYED = "Unemployed"
    UNSKILLED = "Unskilled"
    SKILLED = "Skilled"
    HIGHLY_SKILLED = "Highly Skilled"


class HousingEnum(str, Enum):
    OWN = "own"
    RENT = "rent"
    FREE = "free"


class SavingAccountEnum(str, Enum):
    LITTLE = "little"
    MODERATE = "moderate"
    QUITE_RICH = "quite rich"
    RICH = "rich"


class CheckingAccountEnum(str, Enum):
    LITTLE = "little"
    MODERATE = "moderate"
    RICH = "rich"


class PurposeEnum(str, Enum):
    CAR = "car"
    RADIO_TV = "radio/TV"
    EDUCATION = "education"
    BUSINESS = "business"
    FURNITURE_EQUIPMENT = "furniture/equipment"
    DOMESTIC_APPLIANCES = "domestic appliances"
    REPAIRS = "repairs"
    VACATION_OTHERS = "vacation/others"


class LoanTypeEnum(str, Enum):
    PERSONAL = "Personal"
    HOME = "Home"
    VEHICLE = "Vehicle"
    EDUCATION = "Education"
    BUSINESS = "Business"
    GOLD = "Gold"
    OTHER = "Other"

class GenderEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"