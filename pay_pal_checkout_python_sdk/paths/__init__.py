# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_pal_checkout_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_CHECKOUT_ORDERS = "/v2/checkout/orders"
    V2_CHECKOUT_ORDERS_ID = "/v2/checkout/orders/{id}"
    V2_CHECKOUT_ORDERS_ID_CONFIRMPAYMENTSOURCE = "/v2/checkout/orders/{id}/confirm-payment-source"
    V2_CHECKOUT_ORDERS_ID_AUTHORIZE = "/v2/checkout/orders/{id}/authorize"
    V2_CHECKOUT_ORDERS_ID_CAPTURE = "/v2/checkout/orders/{id}/capture"
    V2_CHECKOUT_ORDERS_ID_TRACK = "/v2/checkout/orders/{id}/track"
    V2_CHECKOUT_ORDERS_ID_TRACKERS_TRACKER_ID = "/v2/checkout/orders/{id}/trackers/{tracker_id}"
