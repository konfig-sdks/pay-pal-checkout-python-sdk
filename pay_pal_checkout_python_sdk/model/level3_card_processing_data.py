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


class Level3CardProcessingData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The level 3 card processing data collections, If your merchant account has been configured for Level 3 processing this field will be passed to the processor on your behalf. Please contact your PayPal Technical Account Manager to define level 3 data for your business.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def shipping_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def duty_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def discount_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def shipping_address() -> typing.Type['AddressPortable']:
                return AddressPortable
            
            
            class ships_from_postal_code(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 60
                    min_length = 1
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9_'.-]*$',
                    }]
            
            
            class line_items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['LineItem']:
                        return LineItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LineItem'], typing.List['LineItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'line_items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LineItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "shipping_amount": shipping_amount,
                "duty_amount": duty_amount,
                "discount_amount": discount_amount,
                "shipping_address": shipping_address,
                "ships_from_postal_code": ships_from_postal_code,
                "line_items": line_items,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duty_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_address"]) -> 'AddressPortable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ships_from_postal_code"]) -> MetaOapg.properties.ships_from_postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_items"]) -> MetaOapg.properties.line_items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shipping_amount", "duty_amount", "discount_amount", "shipping_address", "ships_from_postal_code", "line_items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duty_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_address"]) -> typing.Union['AddressPortable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ships_from_postal_code"]) -> typing.Union[MetaOapg.properties.ships_from_postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_items"]) -> typing.Union[MetaOapg.properties.line_items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shipping_amount", "duty_amount", "discount_amount", "shipping_address", "ships_from_postal_code", "line_items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shipping_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        duty_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        discount_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        shipping_address: typing.Union['AddressPortable', schemas.Unset] = schemas.unset,
        ships_from_postal_code: typing.Union[MetaOapg.properties.ships_from_postal_code, str, schemas.Unset] = schemas.unset,
        line_items: typing.Union[MetaOapg.properties.line_items, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Level3CardProcessingData':
        return super().__new__(
            cls,
            *args,
            shipping_amount=shipping_amount,
            duty_amount=duty_amount,
            discount_amount=discount_amount,
            shipping_address=shipping_address,
            ships_from_postal_code=ships_from_postal_code,
            line_items=line_items,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.address_portable import AddressPortable
from pay_pal_checkout_python_sdk.model.line_item import LineItem
from pay_pal_checkout_python_sdk.model.money import Money
