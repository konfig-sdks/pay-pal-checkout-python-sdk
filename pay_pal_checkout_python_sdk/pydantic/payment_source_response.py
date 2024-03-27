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

from pay_pal_checkout_python_sdk.pydantic.bancontact import Bancontact
from pay_pal_checkout_python_sdk.pydantic.blik import Blik
from pay_pal_checkout_python_sdk.pydantic.card_response import CardResponse
from pay_pal_checkout_python_sdk.pydantic.eps import Eps
from pay_pal_checkout_python_sdk.pydantic.giropay import Giropay
from pay_pal_checkout_python_sdk.pydantic.ideal import Ideal
from pay_pal_checkout_python_sdk.pydantic.mybank import Mybank
from pay_pal_checkout_python_sdk.pydantic.p24 import P24
from pay_pal_checkout_python_sdk.pydantic.paypal_wallet_response import PaypalWalletResponse
from pay_pal_checkout_python_sdk.pydantic.sofort import Sofort
from pay_pal_checkout_python_sdk.pydantic.trustly import Trustly
from pay_pal_checkout_python_sdk.pydantic.venmo_wallet_response import VenmoWalletResponse

class PaymentSourceResponse(BaseModel):
    card: typing.Optional[CardResponse] = Field(None, alias='card')

    paypal: typing.Optional[PaypalWalletResponse] = Field(None, alias='paypal')

    bancontact: typing.Optional[Bancontact] = Field(None, alias='bancontact')

    blik: typing.Optional[Blik] = Field(None, alias='blik')

    eps: typing.Optional[Eps] = Field(None, alias='eps')

    giropay: typing.Optional[Giropay] = Field(None, alias='giropay')

    ideal: typing.Optional[Ideal] = Field(None, alias='ideal')

    mybank: typing.Optional[Mybank] = Field(None, alias='mybank')

    p24: typing.Optional[P24] = Field(None, alias='p24')

    sofort: typing.Optional[Sofort] = Field(None, alias='sofort')

    trustly: typing.Optional[Trustly] = Field(None, alias='trustly')

    venmo: typing.Optional[VenmoWalletResponse] = Field(None, alias='venmo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
