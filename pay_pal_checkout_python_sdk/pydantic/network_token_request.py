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

from pay_pal_checkout_python_sdk.pydantic.date_year_month import DateYearMonth
from pay_pal_checkout_python_sdk.pydantic.eci_flag import EciFlag

class NetworkTokenRequest(BaseModel):
    # Third party network token number.
    number: str = Field(alias='number')

    expiry: DateYearMonth = Field(alias='expiry')

    # An Encrypted one-time use value that's sent along with Network Token. This field is not required to be present for recurring transactions.
    cryptogram: typing.Optional[str] = Field(None, alias='cryptogram')

    eci_flag: typing.Optional[EciFlag] = Field(None, alias='eci_flag')

    # A TRID, or a Token Requestor ID, is an identifier used by merchants to request network tokens from card networks. A TRID is a precursor to obtaining a network token for a credit card primary account number (PAN), and will aid in enabling secure card on file (COF) payments and reducing fraud.
    token_requestor_id: typing.Optional[str] = Field(None, alias='token_requestor_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
