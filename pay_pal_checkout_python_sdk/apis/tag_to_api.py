import typing_extensions

from pay_pal_checkout_python_sdk.apis.tags import TagValues
from pay_pal_checkout_python_sdk.apis.tags.orders_api import OrdersApi
from pay_pal_checkout_python_sdk.apis.tags.trackers_api import TrackersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ORDERS: OrdersApi,
        TagValues.TRACKERS: TrackersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ORDERS: OrdersApi,
        TagValues.TRACKERS: TrackersApi,
    }
)
