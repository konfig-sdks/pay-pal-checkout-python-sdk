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


class OrdersAuthorize400(BaseModel):
    details: typing.Optional[typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]] = Field(None, alias='details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
