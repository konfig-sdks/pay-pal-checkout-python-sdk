# coding: utf-8

"""
    Orders

    An order represents a payment between two or more parties. Use the Orders API to create, update, retrieve, authorize, and capture orders.

    The version of the OpenAPI document: 2.13
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from pay_pal_checkout_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from pay_pal_checkout_python_sdk.api_response import AsyncGeneratorResponse
from pay_pal_checkout_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_checkout_python_sdk import schemas  # noqa: F401

from pay_pal_checkout_python_sdk.model.order import Order as OrderSchema
from pay_pal_checkout_python_sdk.model.orders_create_order401_response import OrdersCreateOrder401Response as OrdersCreateOrder401ResponseSchema
from pay_pal_checkout_python_sdk.model.order_request import OrderRequest as OrderRequestSchema
from pay_pal_checkout_python_sdk.model.checkout_payment_intent import CheckoutPaymentIntent as CheckoutPaymentIntentSchema
from pay_pal_checkout_python_sdk.model.order_application_context import OrderApplicationContext as OrderApplicationContextSchema
from pay_pal_checkout_python_sdk.model.orders_create_order422_response import OrdersCreateOrder422Response as OrdersCreateOrder422ResponseSchema
from pay_pal_checkout_python_sdk.model.payment_source import PaymentSource as PaymentSourceSchema
from pay_pal_checkout_python_sdk.model.purchase_unit_request import PurchaseUnitRequest as PurchaseUnitRequestSchema
from pay_pal_checkout_python_sdk.model.orders_create_order_response import OrdersCreateOrderResponse as OrdersCreateOrderResponseSchema
from pay_pal_checkout_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_checkout_python_sdk.model.payer import Payer as PayerSchema

from pay_pal_checkout_python_sdk.type.order_application_context import OrderApplicationContext
from pay_pal_checkout_python_sdk.type.payment_source import PaymentSource
from pay_pal_checkout_python_sdk.type.order import Order
from pay_pal_checkout_python_sdk.type.order_request import OrderRequest
from pay_pal_checkout_python_sdk.type.checkout_payment_intent import CheckoutPaymentIntent
from pay_pal_checkout_python_sdk.type.payer import Payer
from pay_pal_checkout_python_sdk.type.error_default import ErrorDefault
from pay_pal_checkout_python_sdk.type.orders_create_order422_response import OrdersCreateOrder422Response
from pay_pal_checkout_python_sdk.type.orders_create_order_response import OrdersCreateOrderResponse
from pay_pal_checkout_python_sdk.type.orders_create_order401_response import OrdersCreateOrder401Response
from pay_pal_checkout_python_sdk.type.purchase_unit_request import PurchaseUnitRequest

from ...api_client import Dictionary
from pay_pal_checkout_python_sdk.pydantic.payment_source import PaymentSource as PaymentSourcePydantic
from pay_pal_checkout_python_sdk.pydantic.order import Order as OrderPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_create_order422_response import OrdersCreateOrder422Response as OrdersCreateOrder422ResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.order_request import OrderRequest as OrderRequestPydantic
from pay_pal_checkout_python_sdk.pydantic.purchase_unit_request import PurchaseUnitRequest as PurchaseUnitRequestPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_create_order401_response import OrdersCreateOrder401Response as OrdersCreateOrder401ResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_create_order_response import OrdersCreateOrderResponse as OrdersCreateOrderResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.payer import Payer as PayerPydantic
from pay_pal_checkout_python_sdk.pydantic.checkout_payment_intent import CheckoutPaymentIntent as CheckoutPaymentIntentPydantic
from pay_pal_checkout_python_sdk.pydantic.order_application_context import OrderApplicationContext as OrderApplicationContextPydantic

from . import path

# Header params


class PayPalRequestIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 108
        min_length = 1


class PayPalPartnerAttributionIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 36
        min_length = 1


class PayPalClientMetadataIdSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 36
        min_length = 1


class PreferSchema(
    schemas.StrSchema
):


    class MetaOapg:
        max_length = 25
        min_length = 1
        regex=[{
            'pattern': r'^[a-zA-Z=]*$',
        }]
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'PayPal-Request-Id': typing.Union[PayPalRequestIdSchema, str, ],
        'PayPal-Partner-Attribution-Id': typing.Union[PayPalPartnerAttributionIdSchema, str, ],
        'PayPal-Client-Metadata-Id': typing.Union[PayPalClientMetadataIdSchema, str, ],
        'Prefer': typing.Union[PreferSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_pay_pal_request_id = api_client.HeaderParameter(
    name="PayPal-Request-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalRequestIdSchema,
)
request_header_pay_pal_partner_attribution_id = api_client.HeaderParameter(
    name="PayPal-Partner-Attribution-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalPartnerAttributionIdSchema,
)
request_header_pay_pal_client_metadata_id = api_client.HeaderParameter(
    name="PayPal-Client-Metadata-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalClientMetadataIdSchema,
)
request_header_prefer = api_client.HeaderParameter(
    name="Prefer",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PreferSchema,
)
# body param
SchemaForRequestBodyApplicationJson = OrderRequestSchema


request_body_order_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'Oauth2',
]
SchemaFor200ResponseBodyApplicationJson = OrderSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Order


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Order


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = OrderSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Order


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Order


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = OrdersCreateOrderResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OrdersCreateOrderResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrderResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = OrdersCreateOrder401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: OrdersCreateOrder401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = OrdersCreateOrder422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: OrdersCreateOrder422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: OrdersCreateOrder422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ErrorDefaultSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ErrorDefault


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ErrorDefault


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '201': _response_for_201,
    '400': _response_for_400,
    '401': _response_for_401,
    '422': _response_for_422,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_order_mapped_args(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if intent is not None:
            _body["intent"] = intent
        if payer is not None:
            _body["payer"] = payer
        if purchase_units is not None:
            _body["purchase_units"] = purchase_units
        if payment_source is not None:
            _body["payment_source"] = payment_source
        if application_context is not None:
            _body["application_context"] = application_context
        args.body = _body
        if pay_pal_request_id is not None:
            _header_params["PayPal-Request-Id"] = pay_pal_request_id
        if pay_pal_partner_attribution_id is not None:
            _header_params["PayPal-Partner-Attribution-Id"] = pay_pal_partner_attribution_id
        if pay_pal_client_metadata_id is not None:
            _header_params["PayPal-Client-Metadata-Id"] = pay_pal_client_metadata_id
        if prefer is not None:
            _header_params["Prefer"] = prefer
        args.header = _header_params
        return args

    async def _acreate_order_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create order
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_pay_pal_partner_attribution_id,
            request_header_pay_pal_client_metadata_id,
            request_header_prefer,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/checkout/orders',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_order_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_order_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create order
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_pay_pal_partner_attribution_id,
            request_header_pay_pal_client_metadata_id,
            request_header_prefer,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/checkout/orders',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_order_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateOrderRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_order(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_order_mapped_args(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
        )
        return await self._acreate_order_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create_order(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_order_mapped_args(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
        )
        return self._create_order_oapg(
            body=args.body,
            header_params=args.header,
        )

class CreateOrder(BaseApi):

    async def acreate_order(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrderPydantic:
        raw_response = await self.raw.acreate_order(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
            **kwargs,
        )
        if validate:
            return RootModel[OrderPydantic](raw_response.body).root
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)
    
    
    def create_order(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OrderPydantic:
        raw_response = self.raw.create_order(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
        )
        if validate:
            return RootModel[OrderPydantic](raw_response.body).root
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_order_mapped_args(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
        )
        return await self._acreate_order_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        intent: CheckoutPaymentIntent,
        purchase_units: typing.List[PurchaseUnitRequest],
        payer: typing.Optional[Payer] = None,
        payment_source: typing.Optional[PaymentSource] = None,
        application_context: typing.Optional[OrderApplicationContext] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        pay_pal_partner_attribution_id: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_order_mapped_args(
            intent=intent,
            purchase_units=purchase_units,
            payer=payer,
            payment_source=payment_source,
            application_context=application_context,
            pay_pal_request_id=pay_pal_request_id,
            pay_pal_partner_attribution_id=pay_pal_partner_attribution_id,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            prefer=prefer,
        )
        return self._create_order_oapg(
            body=args.body,
            header_params=args.header,
        )

