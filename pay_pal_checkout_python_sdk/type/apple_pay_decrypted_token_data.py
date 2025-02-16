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

from pay_pal_checkout_python_sdk.type.apple_pay_payment_data import ApplePayPaymentData
from pay_pal_checkout_python_sdk.type.card import Card
from pay_pal_checkout_python_sdk.type.money2 import Money2

class RequiredApplePayDecryptedTokenData(TypedDict):
    tokenized_card: Card

class OptionalApplePayDecryptedTokenData(TypedDict, total=False):
    transaction_amount: Money2

    # Apple Pay Hex-encoded device manufacturer identifier. The pattern is defined by an external party and supports Unicode.
    device_manufacturer_id: str

    # Indicates the type of payment data passed, in case of Non China the payment data is 3DSECURE and for China it is EMV.
    payment_data_type: str

    payment_data: ApplePayPaymentData

class ApplePayDecryptedTokenData(RequiredApplePayDecryptedTokenData, OptionalApplePayDecryptedTokenData):
    pass
