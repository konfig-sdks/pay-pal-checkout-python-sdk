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


class PaypalWalletAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Additional attributes associated with the use of this PayPal Wallet.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def customer() -> typing.Type['PaypalWalletCustomer']:
                return PaypalWalletCustomer
        
            @staticmethod
            def vault() -> typing.Type['VaultPaypalWalletBase']:
                return VaultPaypalWalletBase
            __annotations__ = {
                "customer": customer,
                "vault": vault,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'PaypalWalletCustomer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vault"]) -> 'VaultPaypalWalletBase': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["customer", "vault", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['PaypalWalletCustomer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vault"]) -> typing.Union['VaultPaypalWalletBase', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["customer", "vault", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        customer: typing.Union['PaypalWalletCustomer', schemas.Unset] = schemas.unset,
        vault: typing.Union['VaultPaypalWalletBase', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaypalWalletAttributes':
        return super().__new__(
            cls,
            *args,
            customer=customer,
            vault=vault,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.paypal_wallet_customer import PaypalWalletCustomer
from pay_pal_checkout_python_sdk.model.vault_paypal_wallet_base import VaultPaypalWalletBase
