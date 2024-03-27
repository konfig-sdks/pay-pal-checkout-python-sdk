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

from pay_pal_checkout_python_sdk.type.blik_one_click_response import BlikOneClickResponse
from pay_pal_checkout_python_sdk.type.country_code import CountryCode
from pay_pal_checkout_python_sdk.type.email_address import EmailAddress
from pay_pal_checkout_python_sdk.type.full_name import FullName

class RequiredBlik(TypedDict):
    pass

class OptionalBlik(TypedDict, total=False):
    name: FullName

    country_code: CountryCode

    email: EmailAddress

    one_click: BlikOneClickResponse

class Blik(RequiredBlik, OptionalBlik):
    pass
