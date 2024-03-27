<div align="left">

[![Visit Paypal](./header.png)](https://www.paypal.com&#x2F;)

# Paypal<a id="paypal"></a>

An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`paypalcheckout.orders.add_tracking_information`](#paypalcheckoutordersadd_tracking_information)
  * [`paypalcheckout.orders.authorize_payment_order`](#paypalcheckoutordersauthorize_payment_order)
  * [`paypalcheckout.orders.capture_payment`](#paypalcheckoutorderscapture_payment)
  * [`paypalcheckout.orders.confirm_payment_source`](#paypalcheckoutordersconfirm_payment_source)
  * [`paypalcheckout.orders.create_order`](#paypalcheckoutorderscreate_order)
  * [`paypalcheckout.orders.show_details`](#paypalcheckoutordersshow_details)
  * [`paypalcheckout.orders.update_order_status`](#paypalcheckoutordersupdate_order_status)
  * [`paypalcheckout.trackers.update_tracking_info`](#paypalcheckouttrackersupdate_tracking_info)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=PayPal&serviceName=Checkout&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from pay_pal_checkout_python_sdk import PayPalCheckout, ApiException

paypalcheckout = PayPalCheckout(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add tracking information for an Order.
    add_tracking_information_response = paypalcheckout.orders.add_tracking_information(
        id="8",
        transaction_id="Cu2LC4aWwWL9Y864DZtaGR",
        tracking_number="a",
        tracking_number_type="CARRIER_PROVIDED",
        status="CANCELLED",
        shipment_date="0480-08-03",
        carrier="DPD_RU",
        carrier_name_other="a",
        postage_payment_id="a",
        notify_buyer=False,
        quantity=1,
        tracking_number_validated=True,
        last_updated_time="0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
        shipment_direction="FORWARD",
        shipment_uploader="MERCHANT",
        capture_id="Cu2LC4aWwWL9Y864DZtaGR",
        notify_payer=False,
        items=[{}],
        pay_pal_auth_assertion="string_example",
    )
    print(add_tracking_information_response)
except ApiException as e:
    print("Exception when calling OrdersApi.add_tracking_information: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from pay_pal_checkout_python_sdk import PayPalCheckout, ApiException

paypalcheckout = PayPalCheckout(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Add tracking information for an Order.
        add_tracking_information_response = await paypalcheckout.orders.aadd_tracking_information(
            id="8",
            transaction_id="Cu2LC4aWwWL9Y864DZtaGR",
            tracking_number="a",
            tracking_number_type="CARRIER_PROVIDED",
            status="CANCELLED",
            shipment_date="0480-08-03",
            carrier="DPD_RU",
            carrier_name_other="a",
            postage_payment_id="a",
            notify_buyer=False,
            quantity=1,
            tracking_number_validated=True,
            last_updated_time="0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
            shipment_direction="FORWARD",
            shipment_uploader="MERCHANT",
            capture_id="Cu2LC4aWwWL9Y864DZtaGR",
            notify_payer=False,
            items=[{}],
            pay_pal_auth_assertion="string_example",
        )
        print(add_tracking_information_response)
    except ApiException as e:
        print("Exception when calling OrdersApi.add_tracking_information: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from pay_pal_checkout_python_sdk import PayPalCheckout, ApiException

paypalcheckout = PayPalCheckout(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add tracking information for an Order.
    add_tracking_information_response = paypalcheckout.orders.raw.add_tracking_information(
        id="8",
        transaction_id="Cu2LC4aWwWL9Y864DZtaGR",
        tracking_number="a",
        tracking_number_type="CARRIER_PROVIDED",
        status="CANCELLED",
        shipment_date="0480-08-03",
        carrier="DPD_RU",
        carrier_name_other="a",
        postage_payment_id="a",
        notify_buyer=False,
        quantity=1,
        tracking_number_validated=True,
        last_updated_time="0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
        shipment_direction="FORWARD",
        shipment_uploader="MERCHANT",
        capture_id="Cu2LC4aWwWL9Y864DZtaGR",
        notify_payer=False,
        items=[{}],
        pay_pal_auth_assertion="string_example",
    )
    pprint(add_tracking_information_response.body)
    pprint(add_tracking_information_response.headers)
    pprint(add_tracking_information_response.status)
    pprint(add_tracking_information_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OrdersApi.add_tracking_information: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `paypalcheckout.orders.add_tracking_information`<a id="paypalcheckoutordersadd_tracking_information"></a>

Adds tracking information for an Order.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_tracking_information_response = paypalcheckout.orders.add_tracking_information(
    id="8",
    transaction_id="Cu2LC4aWwWL9Y864DZtaGR",
    tracking_number="a",
    tracking_number_type="CARRIER_PROVIDED",
    status="CANCELLED",
    shipment_date="0480-08-03",
    carrier="DPD_RU",
    carrier_name_other="a",
    postage_payment_id="a",
    notify_buyer=False,
    quantity=1,
    tracking_number_validated=True,
    last_updated_time="0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
    shipment_direction="FORWARD",
    shipment_uploader="MERCHANT",
    capture_id="Cu2LC4aWwWL9Y864DZtaGR",
    notify_payer=False,
    items=[{}],
    pay_pal_auth_assertion="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### transaction_id: `str`<a id="transaction_id-str"></a>

The PayPal transaction ID.

##### tracking_number: `str`<a id="tracking_number-str"></a>

The tracking number for the shipment. This property supports Unicode.

##### tracking_number_type: [`ShipmentTrackingNumberType`](./pay_pal_checkout_python_sdk/type/shipment_tracking_number_type.py)<a id="tracking_number_type-shipmenttrackingnumbertypepay_pal_checkout_python_sdktypeshipment_tracking_number_typepy"></a>

##### status: [`ShipmentTrackingStatus`](./pay_pal_checkout_python_sdk/type/shipment_tracking_status.py)<a id="status-shipmenttrackingstatuspay_pal_checkout_python_sdktypeshipment_tracking_statuspy"></a>

##### shipment_date: [`DateNoTime`](./pay_pal_checkout_python_sdk/type/date_no_time.py)<a id="shipment_date-datenotimepay_pal_checkout_python_sdktypedate_no_timepy"></a>

##### carrier: [`ShipmentCarrier`](./pay_pal_checkout_python_sdk/type/shipment_carrier.py)<a id="carrier-shipmentcarrierpay_pal_checkout_python_sdktypeshipment_carrierpy"></a>

##### carrier_name_other: `str`<a id="carrier_name_other-str"></a>

The name of the carrier for the shipment. Provide this value only if the carrier parameter is OTHER. This property supports Unicode.

##### postage_payment_id: `str`<a id="postage_payment_id-str"></a>

The postage payment ID. This property supports Unicode.

##### notify_buyer: `bool`<a id="notify_buyer-bool"></a>

If true, sends an email notification to the buyer of the PayPal transaction. The email contains the tracking information that was uploaded through the API.

##### quantity: `int`<a id="quantity-int"></a>

The quantity of items shipped.

##### tracking_number_validated: `bool`<a id="tracking_number_validated-bool"></a>

Indicates whether the carrier validated the tracking number.

##### last_updated_time: [`DateTime`](./pay_pal_checkout_python_sdk/type/date_time.py)<a id="last_updated_time-datetimepay_pal_checkout_python_sdktypedate_timepy"></a>

##### shipment_direction: `str`<a id="shipment_direction-str"></a>

To denote whether the shipment is sent forward to the receiver or returned back.

##### shipment_uploader: `str`<a id="shipment_uploader-str"></a>

To denote which party uploaded the shipment tracking info.

##### capture_id: `str`<a id="capture_id-str"></a>

The PayPal capture ID.

##### notify_payer: `bool`<a id="notify_payer-bool"></a>

If true, sends an email notification to the payer of the PayPal transaction. The email contains the tracking information that was uploaded through the API.

##### items: List[`TrackerItem`]<a id="items-listtrackeritem"></a>

An array of details of items in the shipment.

##### pay_pal_auth_assertion: `str`<a id="pay_pal_auth_assertion-str"></a>

An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see <a href=\"/api/rest/requests/#paypal-auth-assertion\">PayPal-Auth-Assertion</a>.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrderTrackerRequest`](./pay_pal_checkout_python_sdk/type/order_tracker_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./pay_pal_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}/track` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.authorize_payment_order`<a id="paypalcheckoutordersauthorize_payment_order"></a>

Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="/api/rest/reference/orders/v2/errors/#authorize-order">Orders v2 errors</a>.</blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authorize_payment_order_response = paypalcheckout.orders.authorize_payment_order(
    id="8",
    payment_source={},
    pay_pal_request_id="a",
    prefer="return=minimal",
    pay_pal_client_metadata_id="a",
    pay_pal_auth_assertion="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### payment_source: [`PaymentSource`](./pay_pal_checkout_python_sdk/type/payment_source.py)<a id="payment_source-paymentsourcepay_pal_checkout_python_sdktypepayment_sourcepy"></a>


##### pay_pal_request_id: `str`<a id="pay_pal_request_id-str"></a>

The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager.

##### prefer: `str`<a id="prefer-str"></a>

The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>

##### pay_pal_client_metadata_id: `str`<a id="pay_pal_client_metadata_id-str"></a>

##### pay_pal_auth_assertion: `str`<a id="pay_pal_auth_assertion-str"></a>

An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see <a href=\"/api/rest/requests/#paypal-auth-assertion\">PayPal-Auth-Assertion</a>.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrderAuthorizeRequest`](./pay_pal_checkout_python_sdk/type/order_authorize_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrderAuthorizeResponse`](./pay_pal_checkout_python_sdk/pydantic/order_authorize_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}/authorize` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.capture_payment`<a id="paypalcheckoutorderscapture_payment"></a>

Captures payment for an order. To successfully capture payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="/api/rest/reference/orders/v2/errors/#capture-order">Orders v2 errors</a>.</blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
capture_payment_response = paypalcheckout.orders.capture_payment(
    id="8",
    payment_source={},
    pay_pal_request_id="a",
    prefer="return=minimal",
    pay_pal_client_metadata_id="a",
    pay_pal_auth_assertion="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### payment_source: [`PaymentSource`](./pay_pal_checkout_python_sdk/type/payment_source.py)<a id="payment_source-paymentsourcepay_pal_checkout_python_sdktypepayment_sourcepy"></a>


##### pay_pal_request_id: `str`<a id="pay_pal_request_id-str"></a>

The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager.

##### prefer: `str`<a id="prefer-str"></a>

The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>

##### pay_pal_client_metadata_id: `str`<a id="pay_pal_client_metadata_id-str"></a>

##### pay_pal_auth_assertion: `str`<a id="pay_pal_auth_assertion-str"></a>

An API-caller-provided JSON Web Token (JWT) assertion that identifies the merchant. For details, see <a href=\"/api/rest/requests/#paypal-auth-assertion\">PayPal-Auth-Assertion</a>.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrderCaptureRequest`](./pay_pal_checkout_python_sdk/type/order_capture_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./pay_pal_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}/capture` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.confirm_payment_source`<a id="paypalcheckoutordersconfirm_payment_source"></a>

Payer confirms their intent to pay for the the Order with the given payment source.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
confirm_payment_source_response = paypalcheckout.orders.confirm_payment_source(
    body=None,
    payment_source={},
    id="8",
    processing_instruction="NO_INSTRUCTION",
    application_context={},
    pay_pal_client_metadata_id="a",
    prefer="return=minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_source: [`PaymentSource`](./pay_pal_checkout_python_sdk/type/payment_source.py)<a id="payment_source-paymentsourcepay_pal_checkout_python_sdktypepayment_sourcepy"></a>


##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### processing_instruction: [`ProcessingInstruction`](./pay_pal_checkout_python_sdk/type/processing_instruction.py)<a id="processing_instruction-processinginstructionpay_pal_checkout_python_sdktypeprocessing_instructionpy"></a>

##### application_context: [`OrderConfirmApplicationContext`](./pay_pal_checkout_python_sdk/type/order_confirm_application_context.py)<a id="application_context-orderconfirmapplicationcontextpay_pal_checkout_python_sdktypeorder_confirm_application_contextpy"></a>


##### pay_pal_client_metadata_id: `str`<a id="pay_pal_client_metadata_id-str"></a>

##### prefer: `str`<a id="prefer-str"></a>

The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConfirmOrderRequest`](./pay_pal_checkout_python_sdk/type/confirm_order_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./pay_pal_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}/confirm-payment-source` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.create_order`<a id="paypalcheckoutorderscreate_order"></a>

Creates an order. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see <a href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="/api/rest/reference/orders/v2/errors/#create-order">Orders v2 errors</a>.</blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_order_response = paypalcheckout.orders.create_order(
    intent="CAPTURE",
    purchase_units=[
        {
            "amount": {},
        }
    ],
    payer={},
    payment_source={},
    application_context={
        "landing_page": "NO_PREFERENCE",
        "shipping_preference": "GET_FROM_FILE",
        "user_action": "CONTINUE",
    },
    pay_pal_request_id="a",
    pay_pal_partner_attribution_id="a",
    pay_pal_client_metadata_id="a",
    prefer="return=minimal",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### intent: [`CheckoutPaymentIntent`](./pay_pal_checkout_python_sdk/type/checkout_payment_intent.py)<a id="intent-checkoutpaymentintentpay_pal_checkout_python_sdktypecheckout_payment_intentpy"></a>

##### purchase_units: List[`PurchaseUnitRequest`]<a id="purchase_units-listpurchaseunitrequest"></a>

An array of purchase units. Each purchase unit establishes a contract between a payer and the payee. Each purchase unit represents either a full or partial order that the payer intends to purchase from the payee.

##### payer: [`Payer`](./pay_pal_checkout_python_sdk/type/payer.py)<a id="payer-payerpay_pal_checkout_python_sdktypepayerpy"></a>


##### payment_source: [`PaymentSource`](./pay_pal_checkout_python_sdk/type/payment_source.py)<a id="payment_source-paymentsourcepay_pal_checkout_python_sdktypepayment_sourcepy"></a>


##### application_context: [`OrderApplicationContext`](./pay_pal_checkout_python_sdk/type/order_application_context.py)<a id="application_context-orderapplicationcontextpay_pal_checkout_python_sdktypeorder_application_contextpy"></a>


##### pay_pal_request_id: `str`<a id="pay_pal_request_id-str"></a>

The server stores keys for 6 hours. The API callers can request the times to up to 72 hours by speaking to their Account Manager.

##### pay_pal_partner_attribution_id: `str`<a id="pay_pal_partner_attribution_id-str"></a>

##### pay_pal_client_metadata_id: `str`<a id="pay_pal_client_metadata_id-str"></a>

##### prefer: `str`<a id="prefer-str"></a>

The preferred server response upon successful completion of the request. Value is:<ul><li><code>return=minimal</code>. The server returns a minimal response to optimize communication between the API caller and the server. A minimal response includes the <code>id</code>, <code>status</code> and HATEOAS links.</li><li><code>return=representation</code>. The server returns a complete resource representation, including the current state of the resource.</li></ul>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrderRequest`](./pay_pal_checkout_python_sdk/type/order_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./pay_pal_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.show_details`<a id="paypalcheckoutordersshow_details"></a>

Shows details for an order, by ID.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="/api/rest/reference/orders/v2/errors/#get-order">Orders v2 errors</a>.</blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_response = paypalcheckout.orders.show_details(
    id="8",
    fields="qhxqgltwliclfmprgfzkrj",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### fields: `str`<a id="fields-str"></a>

A comma-separated list of fields that should be returned for the order. Valid filter field is `payment_source`.

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./pay_pal_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.orders.update_order_status`<a id="paypalcheckoutordersupdate_order_status"></a>

Updates an order with a `CREATED` or `APPROVED` status. You cannot update an order with the `COMPLETED` status.<br/><br/>To make an update, you must provide a `reference_id`. If you omit this value with an order that contains only one purchase unit, PayPal sets the value to `default` which enables you to use the path: <code>\"/purchase_units/@reference_id=='default'/{attribute-or-object}\"</code>. Merchants and partners can add Level 2 and 3 data to payments to reduce risk and payment processing costs. For more information about processing payments, see <a href="https://developer.paypal.com/docs/checkout/advanced/processing/">checkout</a> or <a href="https://developer.paypal.com/docs/multiparty/checkout/advanced/processing/">multiparty checkout</a>.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href=\"/api/rest/reference/orders/v2/errors/#patch-order\">Orders v2 errors</a>.</blockquote>Patchable attributes or objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody><tr><td><code>intent</code></td><td>replace</td><td></td></tr><tr><td><code>payer</code></td><td>replace, add</td><td>Using replace op for <code>payer</code> will replace the whole <code>payer</code> object with the value sent in request.</td></tr><tr><td><code>purchase_units</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].custom_id</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].description</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].payee.email</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].shipping.name</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.address</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].shipping.type</code></td><td>replace, add</td><td></td></tr><tr><td><code>purchase_units[].soft_descriptor</code></td><td>replace, remove</td><td></td></tr><tr><td><code>purchase_units[].amount</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].items</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].invoice_id</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction</code></td><td>replace</td><td></td></tr><tr><td><code>purchase_units[].payment_instruction.disbursement_mode</code></td><td>replace</td><td>By default, <code>disbursement_mode</code> is <code>INSTANT</code>.</td></tr><tr><td><code>purchase_units[].payment_instruction.platform_fees</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.airline</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>purchase_units[].supplementary_data.card</code></td><td>replace, add, remove</td><td></td></tr><tr><td><code>application_context.client_configuration</code></td><td>replace, add</td><td></td></tr></tbody></table>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalcheckout.orders.update_order_status(
    body=[
        {
            "op": "add",
        }
    ],
    id="8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### requestBody: [`PatchRequest`](./pay_pal_checkout_python_sdk/type/patch_request.py)<a id="requestbody-patchrequestpay_pal_checkout_python_sdktypepatch_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalcheckout.trackers.update_tracking_info`<a id="paypalcheckouttrackersupdate_tracking_info"></a>

Updates or cancels the tracking information for a PayPal order, by ID. Updatable attributes or objects:<br/><br/><table><thead><th>Attribute</th><th>Op</th><th>Notes</th></thead><tbody></tr><tr><td><code>items</code></td><td>replace</td><td>Using replace op for <code>items</code> will replace the entire <code>items</code> object with the value sent in request.</td></tr><tr><td><code>notify_payer</code></td><td>replace, add</td><td></td></tr><tr><td><code>status</code></td><td>replace</td><td>Only patching status to CANCELLED is currently supported.</td></tr></tbody></table>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalcheckout.trackers.update_tracking_info(
    body=[
        {
            "op": "replace",
            "path": "/purchase_units/@reference_id=='PUHF'/shipping/address",
            "value": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "Building 17",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US",
            },
        }
    ],
    id="8",
    tracker_id="8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the order that the tracking information is associated with.

##### tracker_id: `str`<a id="tracker_id-str"></a>

The order tracking ID.

##### requestBody: [`PatchRequest`](./pay_pal_checkout_python_sdk/type/patch_request.py)<a id="requestbody-patchrequestpay_pal_checkout_python_sdktypepatch_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout/orders/{id}/trackers/{tracker_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
