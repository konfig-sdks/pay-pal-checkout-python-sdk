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

from pay_pal_checkout_python_sdk.pydantic.country_code import CountryCode
from pay_pal_checkout_python_sdk.pydantic.email_address import EmailAddress
from pay_pal_checkout_python_sdk.pydantic.experience_context_base import ExperienceContextBase
from pay_pal_checkout_python_sdk.pydantic.full_name import FullName

class P24Request(BaseModel):
    name: FullName = Field(alias='name')

    email: EmailAddress = Field(alias='email')

    country_code: CountryCode = Field(alias='country_code')

    experience_context: typing.Optional[ExperienceContextBase] = Field(None, alias='experience_context')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
