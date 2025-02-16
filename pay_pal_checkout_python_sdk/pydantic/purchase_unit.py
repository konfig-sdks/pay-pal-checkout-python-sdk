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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from pay_pal_checkout_python_sdk.pydantic.amount_with_breakdown import AmountWithBreakdown
from pay_pal_checkout_python_sdk.pydantic.item import Item
from pay_pal_checkout_python_sdk.pydantic.payee import Payee
from pay_pal_checkout_python_sdk.pydantic.payment_collection import PaymentCollection
from pay_pal_checkout_python_sdk.pydantic.payment_instruction import PaymentInstruction
from pay_pal_checkout_python_sdk.pydantic.shipping_with_tracking_details import ShippingWithTrackingDetails
from pay_pal_checkout_python_sdk.pydantic.supplementary_data import SupplementaryData

class PurchaseUnit(BaseModel):
    # The purchase description.
    description: typing.Optional[str] = Field(None, alias='description')

    # The API caller-provided external ID for the purchase unit. Required for multiple purchase units when you must update the order through `PATCH`. If you omit this value and the order contains only one purchase unit, PayPal sets this value to `default`. <blockquote><strong>Note:</strong> If there are multiple purchase units, <code>reference_id</code> is required for each purchase unit.</blockquote>
    reference_id: typing.Optional[str] = Field(None, alias='reference_id')

    amount: typing.Optional[AmountWithBreakdown] = Field(None, alias='amount')

    payee: typing.Optional[Payee] = Field(None, alias='payee')

    payment_instruction: typing.Optional[PaymentInstruction] = Field(None, alias='payment_instruction')

    # The API caller-provided external ID. Used to reconcile API caller-initiated transactions with PayPal transactions. Appears in transaction and settlement reports.
    custom_id: typing.Optional[str] = Field(None, alias='custom_id')

    # The API caller-provided external invoice ID for this order.
    invoice_id: typing.Optional[str] = Field(None, alias='invoice_id')

    # The PayPal-generated ID for the purchase unit. This ID appears in both the payer's transaction history and the emails that the payer receives. In addition, this ID is available in transaction and settlement reports that merchants and API callers can use to reconcile transactions. This ID is only available when an order is saved by calling <code>v2/checkout/orders/id/save</code>.
    id: typing.Optional[str] = Field(None, alias='id')

    # The payment descriptor on account transactions on the customer's credit card statement, that PayPal sends to processors. The maximum length of the soft descriptor information that you can pass in the API field is 22 characters, in the following format:<code>22 - len(PAYPAL * (8)) - len(<var>Descriptor in Payment Receiving Preferences of Merchant account</var> + 1)</code>The PAYPAL prefix uses 8 characters.<br/><br/>The soft descriptor supports the following ASCII characters:<ul><li>Alphanumeric characters</li><li>Dashes</li><li>Asterisks</li><li>Periods (.)</li><li>Spaces</li></ul>For Wallet payments marketplace integrations:<ul><li>The merchant descriptor in the Payment Receiving Preferences must be the marketplace name.</li><li>You can't use the remaining space to show the customer service number.</li><li>The remaining spaces can be a combination of seller name and country.</li></ul><br/>For unbranded payments (Direct Card) marketplace integrations, use a combination of the seller name and phone number.
    soft_descriptor: typing.Optional[str] = Field(None, alias='soft_descriptor')

    # An array of items that the customer purchases from the merchant.
    items: typing.Optional[typing.List[Item]] = Field(None, alias='items')

    shipping: typing.Optional[ShippingWithTrackingDetails] = Field(None, alias='shipping')

    supplementary_data: typing.Optional[SupplementaryData] = Field(None, alias='supplementary_data')

    payments: typing.Optional[PaymentCollection] = Field(None, alias='payments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
