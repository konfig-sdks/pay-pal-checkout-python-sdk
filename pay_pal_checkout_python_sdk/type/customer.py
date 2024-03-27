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
from pay_pal_checkout_python_sdk.type.merchant_partner_customer_id import MerchantPartnerCustomerId
from pay_pal_checkout_python_sdk.type.phone_with_type import PhoneWithType

class RequiredCustomer(TypedDict):
    pass

class OptionalCustomer(TypedDict, total=False):
    id: MerchantPartnerCustomerId

    email_address: Email

    phone: PhoneWithType

class Customer(RequiredCustomer, OptionalCustomer):
    pass
