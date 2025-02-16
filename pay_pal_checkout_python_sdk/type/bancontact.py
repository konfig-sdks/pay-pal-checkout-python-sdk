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

from pay_pal_checkout_python_sdk.type.bic import Bic
from pay_pal_checkout_python_sdk.type.country_code import CountryCode
from pay_pal_checkout_python_sdk.type.full_name import FullName
from pay_pal_checkout_python_sdk.type.iban_last_chars import IbanLastChars

class RequiredBancontact(TypedDict):
    pass

class OptionalBancontact(TypedDict, total=False):
    name: FullName

    country_code: CountryCode

    bic: Bic

    iban_last_chars: IbanLastChars

    # The last digits of the card used to fund the Bancontact payment.
    card_last_digits: str

    attributes: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Bancontact(RequiredBancontact, OptionalBancontact):
    pass
