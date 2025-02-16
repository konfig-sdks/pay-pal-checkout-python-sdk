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

from pay_pal_checkout_python_sdk.pydantic.checkout_payment_intent import CheckoutPaymentIntent
from pay_pal_checkout_python_sdk.pydantic.order_application_context import OrderApplicationContext
from pay_pal_checkout_python_sdk.pydantic.payer import Payer
from pay_pal_checkout_python_sdk.pydantic.payment_source import PaymentSource
from pay_pal_checkout_python_sdk.pydantic.purchase_unit_request import PurchaseUnitRequest

class OrderRequest(BaseModel):
    intent: CheckoutPaymentIntent = Field(alias='intent')

    # An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee.
    purchase_units: typing.List[PurchaseUnitRequest] = Field(alias='purchase_units')

    payer: typing.Optional[Payer] = Field(None, alias='payer')

    payment_source: typing.Optional[PaymentSource] = Field(None, alias='payment_source')

    application_context: typing.Optional[OrderApplicationContext] = Field(None, alias='application_context')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
