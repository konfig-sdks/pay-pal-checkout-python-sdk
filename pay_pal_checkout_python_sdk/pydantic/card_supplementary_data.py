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

from pay_pal_checkout_python_sdk.pydantic.level2_card_processing_data import Level2CardProcessingData
from pay_pal_checkout_python_sdk.pydantic.level3_card_processing_data import Level3CardProcessingData

class CardSupplementaryData(BaseModel):
    level_2: typing.Optional[Level2CardProcessingData] = Field(None, alias='level_2')

    level_3: typing.Optional[Level3CardProcessingData] = Field(None, alias='level_3')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
