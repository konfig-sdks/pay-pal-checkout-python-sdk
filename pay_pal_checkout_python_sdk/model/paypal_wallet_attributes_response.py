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


class PaypalWalletAttributesResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Additional attributes associated with the use of a PayPal Wallet.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def vault() -> typing.Type['PaypalWalletVaultResponse']:
                return PaypalWalletVaultResponse
            
            
            class cobranded_cards(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 25
                    min_items = 0
                    
                    @staticmethod
                    def items() -> typing.Type['CobrandedCard']:
                        return CobrandedCard
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CobrandedCard'], typing.List['CobrandedCard']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cobranded_cards':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CobrandedCard':
                    return super().__getitem__(i)
            __annotations__ = {
                "vault": vault,
                "cobranded_cards": cobranded_cards,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vault"]) -> 'PaypalWalletVaultResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cobranded_cards"]) -> MetaOapg.properties.cobranded_cards: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vault", "cobranded_cards", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vault"]) -> typing.Union['PaypalWalletVaultResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cobranded_cards"]) -> typing.Union[MetaOapg.properties.cobranded_cards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vault", "cobranded_cards", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vault: typing.Union['PaypalWalletVaultResponse', schemas.Unset] = schemas.unset,
        cobranded_cards: typing.Union[MetaOapg.properties.cobranded_cards, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaypalWalletAttributesResponse':
        return super().__new__(
            cls,
            *args,
            vault=vault,
            cobranded_cards=cobranded_cards,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.cobranded_card import CobrandedCard
from pay_pal_checkout_python_sdk.model.paypal_wallet_vault_response import PaypalWalletVaultResponse
