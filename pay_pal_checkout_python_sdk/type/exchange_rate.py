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

from pay_pal_checkout_python_sdk.type.currency_code import CurrencyCode

class RequiredExchangeRate(TypedDict):
    pass

class OptionalExchangeRate(TypedDict, total=False):
    source_currency: CurrencyCode

    target_currency: CurrencyCode

    # The target currency amount. Equivalent to one unit of the source currency. Formatted as integer or decimal value with one to 15 digits to the right of the decimal point.
    value: str

class ExchangeRate(RequiredExchangeRate, OptionalExchangeRate):
    pass
