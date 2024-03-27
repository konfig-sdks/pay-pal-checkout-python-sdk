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

from pay_pal_checkout_python_sdk.pydantic.account_id import AccountId
from pay_pal_checkout_python_sdk.pydantic.email import Email

class PayeeBase(BaseModel):
    email_address: typing.Optional[Email] = Field(None, alias='email_address')

    merchant_id: typing.Optional[AccountId] = Field(None, alias='merchant_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
