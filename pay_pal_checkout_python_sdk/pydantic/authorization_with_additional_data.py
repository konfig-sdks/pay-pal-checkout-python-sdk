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

from pay_pal_checkout_python_sdk.pydantic.authorization import Authorization
from pay_pal_checkout_python_sdk.pydantic.processor_response import ProcessorResponse

AuthorizationWithAdditionalData = typing.Union[Authorization,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
AuthorizationWithAdditionalData = object
