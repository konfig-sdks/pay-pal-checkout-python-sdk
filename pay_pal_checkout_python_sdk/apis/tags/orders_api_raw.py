# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id_track.post import AddTrackingInformationRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id_authorize.post import AuthorizePaymentOrderRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id_capture.post import CapturePaymentRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id_confirm_payment_source.post import ConfirmPaymentSourceRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders.post import CreateOrderRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id.get import ShowDetailsRaw
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id.patch import UpdateOrderStatusRaw


class OrdersApiRaw(
    AddTrackingInformationRaw,
    AuthorizePaymentOrderRaw,
    CapturePaymentRaw,
    ConfirmPaymentSourceRaw,
    CreateOrderRaw,
    ShowDetailsRaw,
    UpdateOrderStatusRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
