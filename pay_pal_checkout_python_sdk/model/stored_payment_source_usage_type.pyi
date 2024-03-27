# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_checkout_python_sdk import schemas  # noqa: F401


class StoredPaymentSourceUsageType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Indicates if this is a `first` or `subsequent` payment using a stored payment source (also referred to as stored credential or card on file).
    """
    
    @schemas.classproperty
    def FIRST(cls):
        return cls("FIRST")
    
    @schemas.classproperty
    def SUBSEQUENT(cls):
        return cls("SUBSEQUENT")
    
    @schemas.classproperty
    def DERIVED(cls):
        return cls("DERIVED")
