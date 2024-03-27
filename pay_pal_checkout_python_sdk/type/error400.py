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

from pay_pal_checkout_python_sdk.type.error_details import ErrorDetails
from pay_pal_checkout_python_sdk.type.error_link_description import ErrorLinkDescription

class RequiredError400(TypedDict):
    pass

class OptionalError400(TypedDict, total=False):
    name: str

    message: str

    details: typing.List[ErrorDetails]

    # The PayPal internal ID. Used for correlation purposes.
    debug_id: str

    # An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    links: typing.List[ErrorLinkDescription]

class Error400(RequiredError400, OptionalError400):
    pass
