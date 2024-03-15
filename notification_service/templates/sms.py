from enum import Enum

from pydantic import BaseModel
from pydantic import Field


class SMSTemplate(str, Enum):
    NEW_ORDER = 'NEW_ORDER'
    ORDER_CONFIRMED = 'ORDER_CONFIRMED'
    ORDER_CANCELLED = 'ORDER_CANCELLED'


class BSGRequestData(BaseModel):
    destination: str = 'phone'
    msisdn: str | None = None
    phones: str | None = None
    reference: str
    originator: str
    body: str
    two_way: int = Field(0, alias='2way')
