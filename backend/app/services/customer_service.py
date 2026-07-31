from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerService:

    @staticmethod
    def create(db: Session, data: CustomerCreate):

        total = len(CustomerRepository.get_all(db)) + 1

        customer = Customer(
            customer_id=f"CUS{total:06d}",
            **data.model_dump(),
        )

        return CustomerRepository.create(db, customer)

    @staticmethod
    def get_all(db: Session):
        return CustomerRepository.get_all(db)

    @staticmethod
    def get_one(db: Session, customer_id: str):

        customer = CustomerRepository.get_by_customer_id(
            db,
            customer_id,
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found",
            )

        return customer

    @staticmethod
    def update(
        db: Session,
        customer_id: str,
        data: CustomerUpdate,
    ):
        customer = CustomerService.get_one(db, customer_id)

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(customer, key, value)

        return CustomerRepository.update(db, customer)

    @staticmethod
    def delete(db: Session, customer_id: str):
        customer = CustomerService.get_one(db, customer_id)
        CustomerRepository.delete(db, customer)