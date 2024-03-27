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

from pay_pal_checkout_python_sdk.pydantic.network_transaction_reference import NetworkTransactionReference
from pay_pal_checkout_python_sdk.pydantic.payment_initiator import PaymentInitiator
from pay_pal_checkout_python_sdk.pydantic.stored_payment_source_payment_type import StoredPaymentSourcePaymentType
from pay_pal_checkout_python_sdk.pydantic.stored_payment_source_usage_type import StoredPaymentSourceUsageType

class CardStoredCredential(BaseModel):
    payment_initiator: PaymentInitiator = Field(alias='payment_initiator')

    payment_type: StoredPaymentSourcePaymentType = Field(alias='payment_type')

    usage: typing.Optional[StoredPaymentSourceUsageType] = Field(None, alias='usage')

    previous_network_transaction_reference: typing.Optional[NetworkTransactionReference] = Field(None, alias='previous_network_transaction_reference')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
