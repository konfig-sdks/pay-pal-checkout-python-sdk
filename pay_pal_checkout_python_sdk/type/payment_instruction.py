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

from pay_pal_checkout_python_sdk.type.disbursement_mode import DisbursementMode
from pay_pal_checkout_python_sdk.type.platform_fee import PlatformFee

class RequiredPaymentInstruction(TypedDict):
    pass

class OptionalPaymentInstruction(TypedDict, total=False):
    # An array of various fees, commissions, tips, or donations. This field is only applicable to merchants that been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability.
    platform_fees: typing.List[PlatformFee]

    disbursement_mode: DisbursementMode

    # This field is only enabled for selected merchants/partners to use and provides the ability to trigger a specific pricing rate/plan for a payment transaction. The list of eligible 'payee_pricing_tier_id' would be provided to you by your Account Manager. Specifying values other than the one provided to you by your account manager would result in an error.
    payee_pricing_tier_id: str

    # FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for eligible integrations) to be used when amount is settled/received into the payee account.
    payee_receivable_fx_rate_id: str

class PaymentInstruction(RequiredPaymentInstruction, OptionalPaymentInstruction):
    pass
