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

from pay_pal_checkout_python_sdk.type.address_portable2 import AddressPortable2
from pay_pal_checkout_python_sdk.type.billing_agreement_id import BillingAgreementId
from pay_pal_checkout_python_sdk.type.date_no_time import DateNoTime
from pay_pal_checkout_python_sdk.type.email import Email
from pay_pal_checkout_python_sdk.type.name2 import Name2
from pay_pal_checkout_python_sdk.type.paypal_wallet_attributes import PaypalWalletAttributes
from pay_pal_checkout_python_sdk.type.paypal_wallet_experience_context import PaypalWalletExperienceContext
from pay_pal_checkout_python_sdk.type.phone_with_type import PhoneWithType
from pay_pal_checkout_python_sdk.type.tax_info import TaxInfo
from pay_pal_checkout_python_sdk.type.vault_id import VaultId

class RequiredPaypalWallet(TypedDict):
    pass

class OptionalPaypalWallet(TypedDict, total=False):
    vault_id: VaultId

    email_address: Email

    name: Name2

    phone: PhoneWithType

    birth_date: DateNoTime

    tax_info: TaxInfo

    address: AddressPortable2

    attributes: PaypalWalletAttributes

    experience_context: PaypalWalletExperienceContext

    billing_agreement_id: BillingAgreementId

class PaypalWallet(RequiredPaypalWallet, OptionalPaypalWallet):
    pass
