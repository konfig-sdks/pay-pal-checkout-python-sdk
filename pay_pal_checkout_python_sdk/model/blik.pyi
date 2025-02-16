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


class Blik(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information used to pay using BLIK.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['FullName']:
                return FullName
        
            @staticmethod
            def country_code() -> typing.Type['CountryCode']:
                return CountryCode
        
            @staticmethod
            def email() -> typing.Type['EmailAddress']:
                return EmailAddress
        
            @staticmethod
            def one_click() -> typing.Type['BlikOneClickResponse']:
                return BlikOneClickResponse
            __annotations__ = {
                "name": name,
                "country_code": country_code,
                "email": email,
                "one_click": one_click,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'FullName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> 'CountryCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> 'EmailAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["one_click"]) -> 'BlikOneClickResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "country_code", "email", "one_click", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['FullName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> typing.Union['CountryCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union['EmailAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["one_click"]) -> typing.Union['BlikOneClickResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "country_code", "email", "one_click", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union['FullName', schemas.Unset] = schemas.unset,
        country_code: typing.Union['CountryCode', schemas.Unset] = schemas.unset,
        email: typing.Union['EmailAddress', schemas.Unset] = schemas.unset,
        one_click: typing.Union['BlikOneClickResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Blik':
        return super().__new__(
            cls,
            *args,
            name=name,
            country_code=country_code,
            email=email,
            one_click=one_click,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.blik_one_click_response import BlikOneClickResponse
from pay_pal_checkout_python_sdk.model.country_code import CountryCode
from pay_pal_checkout_python_sdk.model.email_address import EmailAddress
from pay_pal_checkout_python_sdk.model.full_name import FullName
