# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import pay_pal_checkout_python_sdk
from pay_pal_checkout_python_sdk.paths.v2_checkout_orders_id_capture import post
from pay_pal_checkout_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2CheckoutOrdersIdCapture(ApiTestMixin, unittest.TestCase):
    """
    V2CheckoutOrdersIdCapture unit test stubs
        Capture payment for order
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
