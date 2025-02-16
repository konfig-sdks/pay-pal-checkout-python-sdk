# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from pay_pal_checkout_python_sdk.pydantic.address_portable import AddressPortable
from pay_pal_checkout_python_sdk.pydantic.card_attributes import CardAttributes
from pay_pal_checkout_python_sdk.pydantic.card_brand import CardBrand
from pay_pal_checkout_python_sdk.pydantic.card_type import CardType
from pay_pal_checkout_python_sdk.pydantic.date_year_month import DateYearMonth
from pay_pal_checkout_python_sdk.pydantic.instrument_id import InstrumentId

class Card(BaseModel):
    id: typing.Optional[InstrumentId] = Field(None, alias='id')

    # The card holder's name as it appears on the card.
    name: typing.Optional[str] = Field(None, alias='name')

    # The primary account number (PAN) for the payment card.
    number: typing.Optional[str] = Field(None, alias='number')

    expiry: typing.Optional[DateYearMonth] = Field(None, alias='expiry')

    # The three- or four-digit security code of the card. Also known as the CVV, CVC, CVN, CVE, or CID. This parameter cannot be present in the request when `payment_initiator=MERCHANT`.
    security_code: typing.Optional[str] = Field(None, alias='security_code')

    # The last digits of the payment card.
    last_digits: typing.Optional[str] = Field(None, alias='last_digits')

    card_type: typing.Optional[CardBrand] = Field(None, alias='card_type')

    type: typing.Optional[CardType] = Field(None, alias='type')

    brand: typing.Optional[CardBrand] = Field(None, alias='brand')

    billing_address: typing.Optional[AddressPortable] = Field(None, alias='billing_address')

    attributes: typing.Optional[CardAttributes] = Field(None, alias='attributes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
