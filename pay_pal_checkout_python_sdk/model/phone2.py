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


class Phone2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The phone number in its canonical international [E.164 numbering plan format](https://www.itu.int/rec/T-REC-E.164/en).
    """


    class MetaOapg:
        required = {
            "national_number",
        }
        
        class properties:
            
            
            class national_number(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 14
                    min_length = 1
                    regex=[{
                        'pattern': r'^[0-9]{1,14}?$',
                    }]
            __annotations__ = {
                "national_number": national_number,
            }
    
    national_number: MetaOapg.properties.national_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["national_number"]) -> MetaOapg.properties.national_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["national_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["national_number"]) -> MetaOapg.properties.national_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["national_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        national_number: typing.Union[MetaOapg.properties.national_number, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Phone2':
        return super().__new__(
            cls,
            *args,
            national_number=national_number,
            _configuration=_configuration,
            **kwargs,
        )
