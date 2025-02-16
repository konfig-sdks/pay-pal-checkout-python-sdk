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

from pay_pal_checkout_python_sdk.type.date_no_time import DateNoTime
from pay_pal_checkout_python_sdk.type.date_time import DateTime
from pay_pal_checkout_python_sdk.type.shipment_carrier import ShipmentCarrier
from pay_pal_checkout_python_sdk.type.shipment_tracking_number_type import ShipmentTrackingNumberType
from pay_pal_checkout_python_sdk.type.shipment_tracking_status import ShipmentTrackingStatus

class RequiredShipmentTracker(TypedDict):
    # The PayPal transaction ID.
    transaction_id: str

    status: ShipmentTrackingStatus

class OptionalShipmentTracker(TypedDict, total=False):
    # The tracking number for the shipment. This property supports Unicode.
    tracking_number: str

    tracking_number_type: ShipmentTrackingNumberType

    shipment_date: DateNoTime

    carrier: ShipmentCarrier

    # The name of the carrier for the shipment. Provide this value only if the carrier parameter is OTHER. This property supports Unicode.
    carrier_name_other: str

    # The postage payment ID. This property supports Unicode.
    postage_payment_id: str

    # If true, sends an email notification to the buyer of the PayPal transaction. The email contains the tracking information that was uploaded through the API.
    notify_buyer: bool

    # The quantity of items shipped.
    quantity: int

    # Indicates whether the carrier validated the tracking number.
    tracking_number_validated: bool

    last_updated_time: DateTime

    # To denote whether the shipment is sent forward to the receiver or returned back.
    shipment_direction: str

    # To denote which party uploaded the shipment tracking info.
    shipment_uploader: str

class ShipmentTracker(RequiredShipmentTracker, OptionalShipmentTracker):
    pass
