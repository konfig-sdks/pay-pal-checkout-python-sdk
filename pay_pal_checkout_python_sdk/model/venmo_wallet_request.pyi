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


class VenmoWalletRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information needed to pay using Venmo.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def vault_id() -> typing.Type['VaultId']:
                return VaultId
        
            @staticmethod
            def email_address() -> typing.Type['Email']:
                return Email
        
            @staticmethod
            def experience_context() -> typing.Type['VenmoWalletExperienceContext']:
                return VenmoWalletExperienceContext
        
            @staticmethod
            def attributes() -> typing.Type['VenmoWalletAttributes']:
                return VenmoWalletAttributes
            __annotations__ = {
                "vault_id": vault_id,
                "email_address": email_address,
                "experience_context": experience_context,
                "attributes": attributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vault_id"]) -> 'VaultId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> 'Email': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["experience_context"]) -> 'VenmoWalletExperienceContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'VenmoWalletAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vault_id", "email_address", "experience_context", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vault_id"]) -> typing.Union['VaultId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> typing.Union['Email', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["experience_context"]) -> typing.Union['VenmoWalletExperienceContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union['VenmoWalletAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vault_id", "email_address", "experience_context", "attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vault_id: typing.Union['VaultId', schemas.Unset] = schemas.unset,
        email_address: typing.Union['Email', schemas.Unset] = schemas.unset,
        experience_context: typing.Union['VenmoWalletExperienceContext', schemas.Unset] = schemas.unset,
        attributes: typing.Union['VenmoWalletAttributes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VenmoWalletRequest':
        return super().__new__(
            cls,
            *args,
            vault_id=vault_id,
            email_address=email_address,
            experience_context=experience_context,
            attributes=attributes,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_checkout_python_sdk.model.email import Email
from pay_pal_checkout_python_sdk.model.vault_id import VaultId
from pay_pal_checkout_python_sdk.model.venmo_wallet_attributes import VenmoWalletAttributes
from pay_pal_checkout_python_sdk.model.venmo_wallet_experience_context import VenmoWalletExperienceContext
