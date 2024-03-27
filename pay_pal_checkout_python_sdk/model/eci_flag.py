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


class EciFlag(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Electronic Commerce Indicator (ECI). The ECI value is part of the 2 data elements that indicate the transaction was processed electronically. This should be passed on the authorization transaction to the Gateway/Processor.
    """


    class MetaOapg:
        max_length = 255
        min_length = 1
        regex=[{
            'pattern': r'^[0-9A-Z_]+$',
        }]
        enum_value_to_name = {
            "MASTERCARD_NON_3D_SECURE_TRANSACTION": "MASTERCARD_NON_3D_SECURE_TRANSACTION",
            "MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION": "MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION",
            "MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION": "MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION",
            "FULLY_AUTHENTICATED_TRANSACTION": "FULLY_AUTHENTICATED_TRANSACTION",
            "ATTEMPTED_AUTHENTICATION_TRANSACTION": "ATTEMPTED_AUTHENTICATION_TRANSACTION",
            "NON_3D_SECURE_TRANSACTION": "NON_3D_SECURE_TRANSACTION",
        }
    
    @schemas.classproperty
    def MASTERCARD_NON_3D_SECURE_TRANSACTION(cls):
        return cls("MASTERCARD_NON_3D_SECURE_TRANSACTION")
    
    @schemas.classproperty
    def MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION(cls):
        return cls("MASTERCARD_ATTEMPTED_AUTHENTICATION_TRANSACTION")
    
    @schemas.classproperty
    def MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION(cls):
        return cls("MASTERCARD_FULLY_AUTHENTICATED_TRANSACTION")
    
    @schemas.classproperty
    def FULLY_AUTHENTICATED_TRANSACTION(cls):
        return cls("FULLY_AUTHENTICATED_TRANSACTION")
    
    @schemas.classproperty
    def ATTEMPTED_AUTHENTICATION_TRANSACTION(cls):
        return cls("ATTEMPTED_AUTHENTICATION_TRANSACTION")
    
    @schemas.classproperty
    def NON_3D_SECURE_TRANSACTION(cls):
        return cls("NON_3D_SECURE_TRANSACTION")
