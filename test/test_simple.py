# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from pay_pal_checkout_python_sdk import PayPalCheckout

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        paypalcheckout = PayPalCheckout(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(paypalcheckout)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
