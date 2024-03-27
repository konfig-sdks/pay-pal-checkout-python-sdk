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


class RequiredOrdersPatch400(TypedDict):
    pass

class OptionalOrdersPatch400(TypedDict, total=False):
    details: typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]

class OrdersPatch400(RequiredOrdersPatch400, OptionalOrdersPatch400):
    pass
