from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)
from app.services.customer_service import CustomerService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
    dependencies=[Depends(get_current_user)],
)


@router.post(
    "/",
    response_model=CustomerResponse,
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):
    return CustomerService.create(db, customer)


@router.get(
    "/",
    response_model=list[CustomerResponse],
)
def get_customers(
    db: Session = Depends(get_db),
):
    return CustomerService.get_all(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: str,
    db: Session = Depends(get_db),
):
    return CustomerService.get_one(db, customer_id)


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer(
    customer_id: str,
    customer: CustomerUpdate,
    db: Session = Depends(get_db),
):
    return CustomerService.update(
        db,
        customer_id,
        customer,
    )


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: str,
    db: Session = Depends(get_db),
):
    CustomerService.delete(db, customer_id)

    return {
        "message": "Customer deleted successfully",
    }