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


class StoreInVaultInstruction(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Defines how and when the payment source gets vaulted.
    """


    class MetaOapg:
        max_length = 255
        min_length = 1
        regex=[{
            'pattern': r'^[0-9A-Z_]+$',
        }]
        enum_value_to_name = {
            "ON_SUCCESS": "ON_SUCCESS",
        }
    
    @schemas.classproperty
    def ON_SUCCESS(cls):
        return cls("ON_SUCCESS")
