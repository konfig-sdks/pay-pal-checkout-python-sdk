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


class CaptureStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The status of a captured payment.
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMPLETED": "COMPLETED",
                        "DECLINED": "DECLINED",
                        "PARTIALLY_REFUNDED": "PARTIALLY_REFUNDED",
                        "PENDING": "PENDING",
                        "REFUNDED": "REFUNDED",
                        "FAILED": "FAILED",
                    }
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
                
                @schemas.classproperty
                def DECLINED(cls):
                    return cls("DECLINED")
                
                @schemas.classproperty
                def PARTIALLY_REFUNDED(cls):
                    return cls("PARTIALLY_REFUNDED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def REFUNDED(cls):
                    return cls("REFUNDED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
        
            @staticmethod
            def status_details() -> typing.Type['CaptureStatusDetails']:
                return CaptureStatusDetails
            __annotations__ = {
                "status": status,
                "status_details": status_details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_details"]) -> 'CaptureStatusDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "status_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_details"]) -> typing.Union['CaptureStatusDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "status_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        status_details: typing.Union['CaptureStatusDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaptureStatus':
        return super().__new__(
            cls,
            *args,
            status=status,
            status_details=status_details,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.capture_status_details import CaptureStatusDetails
