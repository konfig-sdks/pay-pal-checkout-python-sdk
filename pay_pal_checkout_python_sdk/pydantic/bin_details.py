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

from pay_pal_checkout_python_sdk.pydantic.bin_details_products import BinDetailsProducts
from pay_pal_checkout_python_sdk.pydantic.country_code import CountryCode

class BinDetails(BaseModel):
    # The Bank Identification Number (BIN) signifies the number that is being used to identify the granular level details (except the PII information) of the card.
    bin: typing.Optional[str] = Field(None, alias='bin')

    # The issuer of the card instrument.
    issuing_bank: typing.Optional[str] = Field(None, alias='issuing_bank')

    bin_country_code: typing.Optional[CountryCode] = Field(None, alias='bin_country_code')

    products: typing.Optional[BinDetailsProducts] = Field(None, alias='products')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
