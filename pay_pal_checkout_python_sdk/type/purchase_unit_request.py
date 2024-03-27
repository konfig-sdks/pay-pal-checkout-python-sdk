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

from pay_pal_checkout_python_sdk.type.amount_with_breakdown import AmountWithBreakdown
from pay_pal_checkout_python_sdk.type.item import Item
from pay_pal_checkout_python_sdk.type.payee import Payee
from pay_pal_checkout_python_sdk.type.payment_instruction import PaymentInstruction
from pay_pal_checkout_python_sdk.type.shipping_detail import ShippingDetail
from pay_pal_checkout_python_sdk.type.supplementary_data import SupplementaryData

class RequiredPurchaseUnitRequest(TypedDict):
    amount: AmountWithBreakdown

class OptionalPurchaseUnitRequest(TypedDict, total=False):
    # The purchase description. The maximum length of the character is dependent on the type of characters used. The character length is specified assuming a US ASCII character. Depending on type of character; (e.g. accented character, Japanese characters) the number of characters that that can be specified as input might not equal the permissible max length.
    description: str

    # The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must update the order through `PATCH`. If you omit this value and the order contains only one purchase unit, PayPal sets this value to `default`.
    reference_id: str

    payee: Payee

    payment_instruction: PaymentInstruction

    # The API caller-provided external ID. Used to reconcile client transactions with PayPal transactions. Appears in transaction and settlement reports but is not visible to the payer.
    custom_id: str

    # The API caller-provided external invoice number for this order. Appears in both the payer's transaction history and the emails that the payer receives.
    invoice_id: str

    # The soft descriptor is the dynamic text used to construct the statement descriptor that appears on a payer's card statement.<br><br>If an Order is paid using the \"PayPal Wallet\", the statement descriptor will appear in following format on the payer's card statement: <code><var>PAYPAL_prefix</var>+(space)+<var>merchant_descriptor</var>+(space)+ <var>soft_descriptor</var></code><blockquote><strong>Note:</strong> The merchant descriptor is the descriptor of the merchant’s payment receiving preferences which can be seen by logging into the merchant account https://www.sandbox.paypal.com/businessprofile/settings/info/edit</blockquote>The <code>PAYPAL</code> prefix uses 8 characters. Only the first 22 characters will be displayed in the statement. <br>For example, if:<ul><li>The PayPal prefix toggle is <code>PAYPAL *</code>.</li><li>The merchant descriptor in the profile is <code>Janes Gift</code>.</li><li>The soft descriptor is <code>800-123-1234</code>.</li></ul>Then, the statement descriptor on the card is <code>PAYPAL * Janes Gift 80</code>.
    soft_descriptor: str

    # An array of items that the customer purchases from the merchant.
    items: typing.List[Item]

    shipping: ShippingDetail

    supplementary_data: SupplementaryData

class PurchaseUnitRequest(RequiredPurchaseUnitRequest, OptionalPurchaseUnitRequest):
    pass
