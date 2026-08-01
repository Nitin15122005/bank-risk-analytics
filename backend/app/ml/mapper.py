from datetime import date

import pandas as pd
from app.models.customer import Customer
from app.models.loan import Loan


class MLMapper:

    JOB_MAPPING = {  # noqa: RUF012
        "Unemployed": 0,
        "Unskilled": 1,
        "Skilled": 2,
        "Highly Skilled": 3,
    }

    @staticmethod
    def calculate_age(date_of_birth: date) -> int:
        today = date.today()

        age = (
            today.year
            - date_of_birth.year
            - (
                (today.month, today.day)
                < (date_of_birth.month, date_of_birth.day)
            )
        )

        return age

    @classmethod
    def to_dataframe(
        cls,
        customer: Customer,
        loan: Loan,
    ) -> pd.DataFrame:

        data = {
            "Age": [
                cls.calculate_age(
                    customer.date_of_birth,
                )
            ],

            "Sex": [
                customer.gender.value
                if hasattr(customer.gender, "value")
                else customer.gender
            ],

            "Job": [
                cls.JOB_MAPPING[
                    customer.employment_type.value
                    if hasattr(customer.employment_type, "value")
                    else customer.employment_type
                ]
            ],

            "Housing": [
                customer.housing.value
                if hasattr(customer.housing, "value")
                else customer.housing
            ],

            "Saving accounts": [
                customer.saving_account.value
                if hasattr(customer.saving_account, "value")
                else customer.saving_account
            ],

            "Checking account": [
                customer.checking_account.value
                if hasattr(customer.checking_account, "value")
                else customer.checking_account
            ],

            "Credit amount": [
                float(loan.loan_amount)
            ],

            "Duration": [
                loan.tenure_months
            ],

            "Purpose": [
                loan.purpose.value
                if hasattr(loan.purpose, "value")
                else loan.purpose
            ],
        }

        return pd.DataFrame(data)