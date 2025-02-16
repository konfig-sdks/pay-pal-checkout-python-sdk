# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from pay_pal_checkout_python_sdk.type.apple_pay_decrypted_token_data import ApplePayDecryptedTokenData
from pay_pal_checkout_python_sdk.type.card_stored_credential import CardStoredCredential
from pay_pal_checkout_python_sdk.type.email_address import EmailAddress
from pay_pal_checkout_python_sdk.type.full_name import FullName
from pay_pal_checkout_python_sdk.type.phone import Phone
from pay_pal_checkout_python_sdk.type.vault_id import VaultId

class RequiredApplePayRequest(TypedDict):
    pass

class OptionalApplePayRequest(TypedDict, total=False):
    # ApplePay transaction identifier, this will be the unique identifier for this transaction provided by Apple. The pattern is defined by an external party and supports Unicode.
    id: str

    name: FullName

    email_address: EmailAddress

    phone_number: Phone

    decrypted_token: ApplePayDecryptedTokenData

    stored_credential: CardStoredCredential

    vault_id: VaultId

    attributes: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ApplePayRequest(RequiredApplePayRequest, OptionalApplePayRequest):
    pass
