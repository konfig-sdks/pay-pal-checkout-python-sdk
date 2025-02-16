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

from pay_pal_checkout_python_sdk.type.email import Email
from pay_pal_checkout_python_sdk.type.vault_id import VaultId
from pay_pal_checkout_python_sdk.type.venmo_wallet_attributes import VenmoWalletAttributes
from pay_pal_checkout_python_sdk.type.venmo_wallet_experience_context import VenmoWalletExperienceContext

class RequiredVenmoWalletRequest(TypedDict):
    pass

class OptionalVenmoWalletRequest(TypedDict, total=False):
    vault_id: VaultId

    email_address: Email

    experience_context: VenmoWalletExperienceContext

    attributes: VenmoWalletAttributes

class VenmoWalletRequest(RequiredVenmoWalletRequest, OptionalVenmoWalletRequest):
    pass
