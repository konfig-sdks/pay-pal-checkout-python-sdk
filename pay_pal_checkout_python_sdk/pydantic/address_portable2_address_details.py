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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class AddressPortable2AddressDetails(BaseModel):
    # The street number.
    street_number: typing.Optional[str] = Field(None, alias='street_number')

    # The street name. Just `Drury` in `Drury Lane`.
    street_name: typing.Optional[str] = Field(None, alias='street_name')

    # The street type. For example, avenue, boulevard, road, or expressway.
    street_type: typing.Optional[str] = Field(None, alias='street_type')

    # The delivery service. Post office box, bag number, or post office name.
    delivery_service: typing.Optional[str] = Field(None, alias='delivery_service')

    # A named locations that represents the premise. Usually a building name or number or collection of buildings with a common name or number. For example, <code>Craven House</code>.
    building_name: typing.Optional[str] = Field(None, alias='building_name')

    # The first-order entity below a named building or location that represents the sub-premise. Usually a single building within a collection of buildings with a common name. Can be a flat, story, floor, room, or apartment.
    sub_building: typing.Optional[str] = Field(None, alias='sub_building')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
