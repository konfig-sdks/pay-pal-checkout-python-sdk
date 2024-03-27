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

from pay_pal_checkout_python_sdk.type.activity_timestamps import ActivityTimestamps
from pay_pal_checkout_python_sdk.type.authorization_status import AuthorizationStatus
from pay_pal_checkout_python_sdk.type.date_time import DateTime
from pay_pal_checkout_python_sdk.type.link_description import LinkDescription
from pay_pal_checkout_python_sdk.type.money import Money
from pay_pal_checkout_python_sdk.type.network_transaction_reference import NetworkTransactionReference
from pay_pal_checkout_python_sdk.type.seller_protection import SellerProtection

Authorization = typing.Union[AuthorizationStatus,typing.Union[bool, date, datetime, dict, float, int, list, str, None],ActivityTimestamps]
Authorization = object
