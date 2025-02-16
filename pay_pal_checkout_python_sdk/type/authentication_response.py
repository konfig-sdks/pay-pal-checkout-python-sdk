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

from pay_pal_checkout_python_sdk.type.liability_shift import LiabilityShift
from pay_pal_checkout_python_sdk.type.three_d_secure_authentication_response import ThreeDSecureAuthenticationResponse

class RequiredAuthenticationResponse(TypedDict):
    pass

class OptionalAuthenticationResponse(TypedDict, total=False):
    liability_shift: LiabilityShift

    three_d_secure: ThreeDSecureAuthenticationResponse

    authentication_flow: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    exemption_details: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class AuthenticationResponse(RequiredAuthenticationResponse, OptionalAuthenticationResponse):
    pass
