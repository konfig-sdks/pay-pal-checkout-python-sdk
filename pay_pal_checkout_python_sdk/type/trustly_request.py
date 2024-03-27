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

from pay_pal_checkout_python_sdk.type.country_code import CountryCode
from pay_pal_checkout_python_sdk.type.experience_context_base import ExperienceContextBase
from pay_pal_checkout_python_sdk.type.full_name import FullName

class RequiredTrustlyRequest(TypedDict):
    name: FullName

    country_code: CountryCode

class OptionalTrustlyRequest(TypedDict, total=False):
    experience_context: ExperienceContextBase

class TrustlyRequest(RequiredTrustlyRequest, OptionalTrustlyRequest):
    pass
