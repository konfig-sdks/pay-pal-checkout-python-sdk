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


RequiredPatch = TypedDict("RequiredPatch", {
    # The operation.
    "op": str,
    })

OptionalPatch = TypedDict("OptionalPatch", {
    # The <a href=\"https://tools.ietf.org/html/rfc6901\">JSON Pointer</a> to the target document location at which to complete the operation.
    "path": str,

    # The value to apply. The <code>remove</code>, <code>copy</code>, and <code>move</code> operations do not require a value. Since <a href=\"https://www.rfc-editor.org/rfc/rfc69021\">JSON Patch</a> allows any type for <code>value</code>, the <code>type</code> property is not specified.
    "value": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    # The <a href=\"https://tools.ietf.org/html/rfc6901\">JSON Pointer</a> to the target document location from which to move the value. Required for the <code>move</code> operation.
    "from": str,
    }, total=False)

class Patch(RequiredPatch, OptionalPatch):
    pass
