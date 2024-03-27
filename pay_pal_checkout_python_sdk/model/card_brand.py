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


class CardBrand(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The card network or brand. Applies to credit, debit, gift, and payment cards.
    """


    class MetaOapg:
        max_length = 255
        min_length = 1
        regex=[{
            'pattern': r'^[A-Z_]+$',
        }]
        enum_value_to_name = {
            "VISA": "VISA",
            "MASTERCARD": "MASTERCARD",
            "DISCOVER": "DISCOVER",
            "AMEX": "AMEX",
            "SOLO": "SOLO",
            "JCB": "JCB",
            "STAR": "STAR",
            "DELTA": "DELTA",
            "SWITCH": "SWITCH",
            "MAESTRO": "MAESTRO",
            "CB_NATIONALE": "CB_NATIONALE",
            "CONFIGOGA": "CONFIGOGA",
            "CONFIDIS": "CONFIDIS",
            "ELECTRON": "ELECTRON",
            "CETELEM": "CETELEM",
            "CHINA_UNION_PAY": "CHINA_UNION_PAY",
        }
    
    @schemas.classproperty
    def VISA(cls):
        return cls("VISA")
    
    @schemas.classproperty
    def MASTERCARD(cls):
        return cls("MASTERCARD")
    
    @schemas.classproperty
    def DISCOVER(cls):
        return cls("DISCOVER")
    
    @schemas.classproperty
    def AMEX(cls):
        return cls("AMEX")
    
    @schemas.classproperty
    def SOLO(cls):
        return cls("SOLO")
    
    @schemas.classproperty
    def JCB(cls):
        return cls("JCB")
    
    @schemas.classproperty
    def STAR(cls):
        return cls("STAR")
    
    @schemas.classproperty
    def DELTA(cls):
        return cls("DELTA")
    
    @schemas.classproperty
    def SWITCH(cls):
        return cls("SWITCH")
    
    @schemas.classproperty
    def MAESTRO(cls):
        return cls("MAESTRO")
    
    @schemas.classproperty
    def CB_NATIONALE(cls):
        return cls("CB_NATIONALE")
    
    @schemas.classproperty
    def CONFIGOGA(cls):
        return cls("CONFIGOGA")
    
    @schemas.classproperty
    def CONFIDIS(cls):
        return cls("CONFIDIS")
    
    @schemas.classproperty
    def ELECTRON(cls):
        return cls("ELECTRON")
    
    @schemas.classproperty
    def CETELEM(cls):
        return cls("CETELEM")
    
    @schemas.classproperty
    def CHINA_UNION_PAY(cls):
        return cls("CHINA_UNION_PAY")
