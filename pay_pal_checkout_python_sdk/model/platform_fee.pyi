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


class PlatformFee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The platform or partner fee, commission, or brokerage fee that is associated with the transaction. Not a separate or isolated transaction leg from the external perspective. The platform fee is limited in scope and is always associated with the original payment for the purchase unit.
    """


    class MetaOapg:
        required = {
            "amount",
        }
        
        class properties:
        
            @staticmethod
            def amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def payee() -> typing.Type['PayeeBase']:
                return PayeeBase
            __annotations__ = {
                "amount": amount,
                "payee": payee,
            }
    
    amount: 'Money'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee"]) -> 'PayeeBase': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "payee", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee"]) -> typing.Union['PayeeBase', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "payee", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: 'Money',
        payee: typing.Union['PayeeBase', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlatformFee':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            payee=payee,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.money import Money
from pay_pal_checkout_python_sdk.model.payee_base import PayeeBase
