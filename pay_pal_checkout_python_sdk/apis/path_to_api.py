import typing_extensions

from pay_pal_checkout_python_sdk.paths import PathValues
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders import V2CheckoutOrders
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id import V2CheckoutOrdersId
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id_confirm_payment_source import V2CheckoutOrdersIdConfirmPaymentSource
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id_authorize import V2CheckoutOrdersIdAuthorize
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id_capture import V2CheckoutOrdersIdCapture
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id_track import V2CheckoutOrdersIdTrack
from pay_pal_checkout_python_sdk.apis.paths.v2_checkout_orders_id_trackers_tracker_id import V2CheckoutOrdersIdTrackersTrackerId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_CHECKOUT_ORDERS: V2CheckoutOrders,
        PathValues.V2_CHECKOUT_ORDERS_ID: V2CheckoutOrdersId,
        PathValues.V2_CHECKOUT_ORDERS_ID_CONFIRMPAYMENTSOURCE: V2CheckoutOrdersIdConfirmPaymentSource,
        PathValues.V2_CHECKOUT_ORDERS_ID_AUTHORIZE: V2CheckoutOrdersIdAuthorize,
        PathValues.V2_CHECKOUT_ORDERS_ID_CAPTURE: V2CheckoutOrdersIdCapture,
        PathValues.V2_CHECKOUT_ORDERS_ID_TRACK: V2CheckoutOrdersIdTrack,
        PathValues.V2_CHECKOUT_ORDERS_ID_TRACKERS_TRACKER_ID: V2CheckoutOrdersIdTrackersTrackerId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_CHECKOUT_ORDERS: V2CheckoutOrders,
        PathValues.V2_CHECKOUT_ORDERS_ID: V2CheckoutOrdersId,
        PathValues.V2_CHECKOUT_ORDERS_ID_CONFIRMPAYMENTSOURCE: V2CheckoutOrdersIdConfirmPaymentSource,
        PathValues.V2_CHECKOUT_ORDERS_ID_AUTHORIZE: V2CheckoutOrdersIdAuthorize,
        PathValues.V2_CHECKOUT_ORDERS_ID_CAPTURE: V2CheckoutOrdersIdCapture,
        PathValues.V2_CHECKOUT_ORDERS_ID_TRACK: V2CheckoutOrdersIdTrack,
        PathValues.V2_CHECKOUT_ORDERS_ID_TRACKERS_TRACKER_ID: V2CheckoutOrdersIdTrackersTrackerId,
    }
)
