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

from pay_pal_checkout_python_sdk.pydantic.account_id2 import AccountId2
from pay_pal_checkout_python_sdk.pydantic.address_portable2 import AddressPortable2
from pay_pal_checkout_python_sdk.pydantic.date_no_time import DateNoTime
from pay_pal_checkout_python_sdk.pydantic.email import Email
from pay_pal_checkout_python_sdk.pydantic.name2 import Name2
from pay_pal_checkout_python_sdk.pydantic.paypal_wallet_attributes_response import PaypalWalletAttributesResponse
from pay_pal_checkout_python_sdk.pydantic.phone2 import Phone2
from pay_pal_checkout_python_sdk.pydantic.phone_type2 import PhoneType2
from pay_pal_checkout_python_sdk.pydantic.tax_info import TaxInfo

class PaypalWalletResponse(BaseModel):
    email_address: typing.Optional[Email] = Field(None, alias='email_address')

    account_id: typing.Optional[AccountId2] = Field(None, alias='account_id')

    # The account status indicates whether the buyer has verified the financial details associated with their PayPal account.
    account_status: typing.Optional[Literal["VERIFIED", "UNVERIFIED"]] = Field(None, alias='account_status')

    name: typing.Optional[Name2] = Field(None, alias='name')

    phone_type: typing.Optional[PhoneType2] = Field(None, alias='phone_type')

    phone_number: typing.Optional[Phone2] = Field(None, alias='phone_number')

    birth_date: typing.Optional[DateNoTime] = Field(None, alias='birth_date')

    tax_info: typing.Optional[TaxInfo] = Field(None, alias='tax_info')

    address: typing.Optional[AddressPortable2] = Field(None, alias='address')

    attributes: typing.Optional[PaypalWalletAttributesResponse] = Field(None, alias='attributes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
