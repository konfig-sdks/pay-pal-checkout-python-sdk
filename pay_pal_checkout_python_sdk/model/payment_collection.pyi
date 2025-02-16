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


class PaymentCollection(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The collection of payments, or transactions, for a purchase unit in an order. For example, authorized payments, captured payments, and refunds.
    """


    class MetaOapg:
        
        class properties:
            
            
            class authorizations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AuthorizationWithAdditionalData']:
                        return AuthorizationWithAdditionalData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AuthorizationWithAdditionalData'], typing.List['AuthorizationWithAdditionalData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'authorizations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AuthorizationWithAdditionalData':
                    return super().__getitem__(i)
            
            
            class captures(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Capture']:
                        return Capture
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Capture'], typing.List['Capture']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'captures':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Capture':
                    return super().__getitem__(i)
            
            
            class refunds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Refund']:
                        return Refund
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Refund'], typing.List['Refund']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refunds':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Refund':
                    return super().__getitem__(i)
            __annotations__ = {
                "authorizations": authorizations,
                "captures": captures,
                "refunds": refunds,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorizations"]) -> MetaOapg.properties.authorizations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["captures"]) -> MetaOapg.properties.captures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refunds"]) -> MetaOapg.properties.refunds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authorizations", "captures", "refunds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorizations"]) -> typing.Union[MetaOapg.properties.authorizations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["captures"]) -> typing.Union[MetaOapg.properties.captures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refunds"]) -> typing.Union[MetaOapg.properties.refunds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authorizations", "captures", "refunds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        authorizations: typing.Union[MetaOapg.properties.authorizations, list, tuple, schemas.Unset] = schemas.unset,
        captures: typing.Union[MetaOapg.properties.captures, list, tuple, schemas.Unset] = schemas.unset,
        refunds: typing.Union[MetaOapg.properties.refunds, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentCollection':
        return super().__new__(
            cls,
            *args,
            authorizations=authorizations,
            captures=captures,
            refunds=refunds,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.authorization_with_additional_data import AuthorizationWithAdditionalData
from pay_pal_checkout_python_sdk.model.capture import Capture
from pay_pal_checkout_python_sdk.model.refund import Refund
