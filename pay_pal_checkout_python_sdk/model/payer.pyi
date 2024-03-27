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


class Payer(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The customer who approves and pays for the order. The customer is also known as the payer.
    """


    class MetaOapg:
        format = 'payer_v1'
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def name() -> typing.Type['Name']:
                        return Name
                
                    @staticmethod
                    def phone() -> typing.Type['PhoneWithType']:
                        return PhoneWithType
                
                    @staticmethod
                    def birth_date() -> typing.Type['DateNoTime']:
                        return DateNoTime
                
                    @staticmethod
                    def tax_info() -> typing.Type['TaxInfo']:
                        return TaxInfo
                
                    @staticmethod
                    def address() -> typing.Type['AddressPortable']:
                        return AddressPortable
                    __annotations__ = {
                        "name": name,
                        "phone": phone,
                        "birth_date": birth_date,
                        "tax_info": tax_info,
                        "address": address,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phone"]) -> 'PhoneWithType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["birth_date"]) -> 'DateNoTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tax_info"]) -> 'TaxInfo': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'AddressPortable': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "phone", "birth_date", "tax_info", "address", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['Name', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union['PhoneWithType', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["birth_date"]) -> typing.Union['DateNoTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tax_info"]) -> typing.Union['TaxInfo', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['AddressPortable', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "phone", "birth_date", "tax_info", "address", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                name: typing.Union['Name', schemas.Unset] = schemas.unset,
                phone: typing.Union['PhoneWithType', schemas.Unset] = schemas.unset,
                birth_date: typing.Union['DateNoTime', schemas.Unset] = schemas.unset,
                tax_info: typing.Union['TaxInfo', schemas.Unset] = schemas.unset,
                address: typing.Union['AddressPortable', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    name=name,
                    phone=phone,
                    birth_date=birth_date,
                    tax_info=tax_info,
                    address=address,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                PayerBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Payer':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.address_portable import AddressPortable
from pay_pal_checkout_python_sdk.model.date_no_time import DateNoTime
from pay_pal_checkout_python_sdk.model.name import Name
from pay_pal_checkout_python_sdk.model.payer_base import PayerBase
from pay_pal_checkout_python_sdk.model.phone_with_type import PhoneWithType
from pay_pal_checkout_python_sdk.model.tax_info import TaxInfo
