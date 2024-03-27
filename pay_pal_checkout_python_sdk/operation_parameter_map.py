operation_parameter_map = {
    '/v2/checkout/orders/{id}/track-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'transaction_id'
            },
            {
                'name': 'tracking_number'
            },
            {
                'name': 'tracking_number_type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'shipment_date'
            },
            {
                'name': 'carrier'
            },
            {
                'name': 'carrier_name_other'
            },
            {
                'name': 'postage_payment_id'
            },
            {
                'name': 'notify_buyer'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'tracking_number_validated'
            },
            {
                'name': 'last_updated_time'
            },
            {
                'name': 'shipment_direction'
            },
            {
                'name': 'shipment_uploader'
            },
            {
                'name': 'capture_id'
            },
            {
                'name': 'notify_payer'
            },
            {
                'name': 'items'
            },
            {
                'name': 'PayPal-Auth-Assertion'
            },
        ]
    },
    '/v2/checkout/orders/{id}/authorize-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'payment_source'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'Prefer'
            },
            {
                'name': 'PayPal-Client-Metadata-Id'
            },
            {
                'name': 'PayPal-Auth-Assertion'
            },
        ]
    },
    '/v2/checkout/orders/{id}/capture-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'payment_source'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'Prefer'
            },
            {
                'name': 'PayPal-Client-Metadata-Id'
            },
            {
                'name': 'PayPal-Auth-Assertion'
            },
        ]
    },
    '/v2/checkout/orders/{id}/confirm-payment-source-POST': {
        'parameters': [
            {
                'name': 'payment_source'
            },
            {
                'name': 'id'
            },
            {
                'name': 'processing_instruction'
            },
            {
                'name': 'application_context'
            },
            {
                'name': 'PayPal-Client-Metadata-Id'
            },
            {
                'name': 'Prefer'
            },
        ]
    },
    '/v2/checkout/orders-POST': {
        'parameters': [
            {
                'name': 'intent'
            },
            {
                'name': 'purchase_units'
            },
            {
                'name': 'payer'
            },
            {
                'name': 'payment_source'
            },
            {
                'name': 'application_context'
            },
            {
                'name': 'PayPal-Request-Id'
            },
            {
                'name': 'PayPal-Partner-Attribution-Id'
            },
            {
                'name': 'PayPal-Client-Metadata-Id'
            },
            {
                'name': 'Prefer'
            },
        ]
    },
    '/v2/checkout/orders/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v2/checkout/orders/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v2/checkout/orders/{id}/trackers/{tracker_id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tracker_id'
            },
        ]
    },
};