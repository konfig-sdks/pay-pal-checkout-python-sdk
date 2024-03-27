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

from pay_pal_checkout_python_sdk.pydantic.error_link_description import ErrorLinkDescription

class Error503(BaseModel):
    name: typing.Optional[Literal["SERVICE_UNAVAILABLE"]] = Field(None, alias='name')

    message: typing.Optional[Literal["Service Unavailable."]] = Field(None, alias='message')

    # The PayPal internal ID. Used for correlation purposes.
    debug_id: typing.Optional[str] = Field(None, alias='debug_id')

    # An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    links: typing.Optional[typing.List[ErrorLinkDescription]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
