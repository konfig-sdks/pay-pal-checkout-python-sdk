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


class OrderApplicationContext(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Customizes the payer experience during the approval process for the payment with PayPal.<blockquote><strong>Note:</strong> Partners and Marketplaces might configure <code>brand_name</code> and <code>shipping_preference</code> during partner account setup, which overrides the request values.</blockquote>
    """


    class MetaOapg:
        
        class properties:
            
            
            class brand_name(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def locale() -> typing.Type['Language']:
                return Language
            
            
            class landing_page(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LOGIN(cls):
                    return cls("LOGIN")
                
                @schemas.classproperty
                def BILLING(cls):
                    return cls("BILLING")
                
                @schemas.classproperty
                def NO_PREFERENCE(cls):
                    return cls("NO_PREFERENCE")
            
            
            class shipping_preference(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GET_FROM_FILE(cls):
                    return cls("GET_FROM_FILE")
                
                @schemas.classproperty
                def NO_SHIPPING(cls):
                    return cls("NO_SHIPPING")
                
                @schemas.classproperty
                def SET_PROVIDED_ADDRESS(cls):
                    return cls("SET_PROVIDED_ADDRESS")
            
            
            class user_action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONTINUE(cls):
                    return cls("CONTINUE")
                
                @schemas.classproperty
                def PAY_NOW(cls):
                    return cls("PAY_NOW")
        
            @staticmethod
            def payment_method() -> typing.Type['PaymentMethod']:
                return PaymentMethod
            return_url = schemas.StrSchema
            cancel_url = schemas.StrSchema
        
            @staticmethod
            def stored_payment_source() -> typing.Type['StoredPaymentSource']:
                return StoredPaymentSource
            __annotations__ = {
                "brand_name": brand_name,
                "locale": locale,
                "landing_page": landing_page,
                "shipping_preference": shipping_preference,
                "user_action": user_action,
                "payment_method": payment_method,
                "return_url": return_url,
                "cancel_url": cancel_url,
                "stored_payment_source": stored_payment_source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand_name"]) -> MetaOapg.properties.brand_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> 'Language': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["landing_page"]) -> MetaOapg.properties.landing_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_preference"]) -> MetaOapg.properties.shipping_preference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_action"]) -> MetaOapg.properties.user_action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method"]) -> 'PaymentMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return_url"]) -> MetaOapg.properties.return_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancel_url"]) -> MetaOapg.properties.cancel_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stored_payment_source"]) -> 'StoredPaymentSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["brand_name", "locale", "landing_page", "shipping_preference", "user_action", "payment_method", "return_url", "cancel_url", "stored_payment_source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand_name"]) -> typing.Union[MetaOapg.properties.brand_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> typing.Union['Language', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["landing_page"]) -> typing.Union[MetaOapg.properties.landing_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_preference"]) -> typing.Union[MetaOapg.properties.shipping_preference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_action"]) -> typing.Union[MetaOapg.properties.user_action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method"]) -> typing.Union['PaymentMethod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return_url"]) -> typing.Union[MetaOapg.properties.return_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancel_url"]) -> typing.Union[MetaOapg.properties.cancel_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stored_payment_source"]) -> typing.Union['StoredPaymentSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["brand_name", "locale", "landing_page", "shipping_preference", "user_action", "payment_method", "return_url", "cancel_url", "stored_payment_source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        brand_name: typing.Union[MetaOapg.properties.brand_name, str, schemas.Unset] = schemas.unset,
        locale: typing.Union['Language', schemas.Unset] = schemas.unset,
        landing_page: typing.Union[MetaOapg.properties.landing_page, str, schemas.Unset] = schemas.unset,
        shipping_preference: typing.Union[MetaOapg.properties.shipping_preference, str, schemas.Unset] = schemas.unset,
        user_action: typing.Union[MetaOapg.properties.user_action, str, schemas.Unset] = schemas.unset,
        payment_method: typing.Union['PaymentMethod', schemas.Unset] = schemas.unset,
        return_url: typing.Union[MetaOapg.properties.return_url, str, schemas.Unset] = schemas.unset,
        cancel_url: typing.Union[MetaOapg.properties.cancel_url, str, schemas.Unset] = schemas.unset,
        stored_payment_source: typing.Union['StoredPaymentSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderApplicationContext':
        return super().__new__(
            cls,
            *args,
            brand_name=brand_name,
            locale=locale,
            landing_page=landing_page,
            shipping_preference=shipping_preference,
            user_action=user_action,
            payment_method=payment_method,
            return_url=return_url,
            cancel_url=cancel_url,
            stored_payment_source=stored_payment_source,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.language import Language
from pay_pal_checkout_python_sdk.model.payment_method import PaymentMethod
from pay_pal_checkout_python_sdk.model.stored_payment_source import StoredPaymentSource
