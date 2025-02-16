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


class PayeeBase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details for the merchant who receives the funds and fulfills the order. The merchant is also known as the payee.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def email_address() -> typing.Type['Email']:
                return Email
        
            @staticmethod
            def merchant_id() -> typing.Type['AccountId']:
                return AccountId
            __annotations__ = {
                "email_address": email_address,
                "merchant_id": merchant_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> 'Email': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_id"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_address", "merchant_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> typing.Union['Email', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_id"]) -> typing.Union['AccountId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_address", "merchant_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email_address: typing.Union['Email', schemas.Unset] = schemas.unset,
        merchant_id: typing.Union['AccountId', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayeeBase':
        return super().__new__(
            cls,
            *args,
            email_address=email_address,
            merchant_id=merchant_id,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.account_id import AccountId
from pay_pal_checkout_python_sdk.model.email import Email
