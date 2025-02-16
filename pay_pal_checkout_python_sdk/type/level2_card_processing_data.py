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

from pay_pal_checkout_python_sdk.type.money import Money

class RequiredLevel2CardProcessingData(TypedDict):
    pass

class OptionalLevel2CardProcessingData(TypedDict, total=False):
    # Use this field to pass a purchase identification value of up to 12 ASCII characters for AIB and 17 ASCII characters for all other processors.
    invoice_id: str

    tax_total: Money

class Level2CardProcessingData(RequiredLevel2CardProcessingData, OptionalLevel2CardProcessingData):
    pass
