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

from pay_pal_checkout_python_sdk.model.error500 import Error500 as Error500Schema
from pay_pal_checkout_python_sdk.model.order_capture_request import OrderCaptureRequest as OrderCaptureRequestSchema
from pay_pal_checkout_python_sdk.model.order import Order as OrderSchema
from pay_pal_checkout_python_sdk.model.orders_capture_payment403_response import OrdersCapturePayment403Response as OrdersCapturePayment403ResponseSchema
from pay_pal_checkout_python_sdk.model.orders_capture_payment422_response import OrdersCapturePayment422Response as OrdersCapturePayment422ResponseSchema
from pay_pal_checkout_python_sdk.model.payment_source import PaymentSource as PaymentSourceSchema
from pay_pal_checkout_python_sdk.model.orders_capture_payment_response import OrdersCapturePaymentResponse as OrdersCapturePaymentResponseSchema
from pay_pal_checkout_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_checkout_python_sdk.model.orders_capture_payment404_response import OrdersCapturePayment404Response as OrdersCapturePayment404ResponseSchema
from pay_pal_checkout_python_sdk.model.orders_capture_payment401_response import OrdersCapturePayment401Response as OrdersCapturePayment401ResponseSchema

from pay_pal_checkout_python_sdk.type.payment_source import PaymentSource
from pay_pal_checkout_python_sdk.type.order import Order
from pay_pal_checkout_python_sdk.type.orders_capture_payment403_response import OrdersCapturePayment403Response
from pay_pal_checkout_python_sdk.type.orders_capture_payment401_response import OrdersCapturePayment401Response
from pay_pal_checkout_python_sdk.type.order_capture_request import OrderCaptureRequest
from pay_pal_checkout_python_sdk.type.orders_capture_payment404_response import OrdersCapturePayment404Response
from pay_pal_checkout_python_sdk.type.error_default import ErrorDefault
from pay_pal_checkout_python_sdk.type.orders_capture_payment_response import OrdersCapturePaymentResponse
from pay_pal_checkout_python_sdk.type.orders_capture_payment422_response import OrdersCapturePayment422Response
from pay_pal_checkout_python_sdk.type.error500 import Error500

from ...api_client import Dictionary
from pay_pal_checkout_python_sdk.pydantic.payment_source import PaymentSource as PaymentSourcePydantic
from pay_pal_checkout_python_sdk.pydantic.order import Order as OrderPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_capture_payment401_response import OrdersCapturePayment401Response as OrdersCapturePayment401ResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_capture_payment403_response import OrdersCapturePayment403Response as OrdersCapturePayment403ResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.error500 import Error500 as Error500Pydantic
from pay_pal_checkout_python_sdk.pydantic.order_capture_request import OrderCaptureRequest as OrderCaptureRequestPydantic
from pay_pal_checkout_python_sdk.pydantic.orders_capture_payment_response import OrdersCapturePaymentResponse as OrdersCapturePaymentResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.orders_capture_payment422_response import OrdersCapturePayment422Response as OrdersCapturePayment422ResponsePydantic
from pay_pal_checkout_python_sdk.pydantic.orders_capture_payment404_response import OrdersCapturePayment404Response as OrdersCapturePayment404ResponsePydantic

# Header params


class PayPalRequestIdSchema(
    schemas.StrSchema
):
    pass


class PreferSchema(
    schemas.StrSchema
):
    pass


class PayPalClientMetadataIdSchema(
    schemas.StrSchema
):
    pass
PayPalAuthAssertionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'PayPal-Request-Id': typing.Union[PayPalRequestIdSchema, str, ],
        'Prefer': typing.Union[PreferSchema, str, ],
        'PayPal-Client-Metadata-Id': typing.Union[PayPalClientMetadataIdSchema, str, ],
        'PayPal-Auth-Assertion': typing.Union[PayPalAuthAssertionSchema, str, ],
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
request_header_prefer = api_client.HeaderParameter(
    name="Prefer",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PreferSchema,
)
request_header_pay_pal_client_metadata_id = api_client.HeaderParameter(
    name="PayPal-Client-Metadata-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalClientMetadataIdSchema,
)
request_header_pay_pal_auth_assertion = api_client.HeaderParameter(
    name="PayPal-Auth-Assertion",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalAuthAssertionSchema,
)
# Path params


class IdSchema(
    schemas.StrSchema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = OrderCaptureRequestSchema


request_body_order_capture_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
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
SchemaFor400ResponseBodyApplicationJson = OrdersCapturePaymentResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OrdersCapturePaymentResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OrdersCapturePaymentResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = OrdersCapturePayment401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: OrdersCapturePayment401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: OrdersCapturePayment401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = OrdersCapturePayment403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: OrdersCapturePayment403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: OrdersCapturePayment403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = OrdersCapturePayment404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: OrdersCapturePayment404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: OrdersCapturePayment404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = OrdersCapturePayment422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: OrdersCapturePayment422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: OrdersCapturePayment422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = Error500Schema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: Error500


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: Error500


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _capture_payment_mapped_args(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if payment_source is not None:
            _body["payment_source"] = payment_source
        args.body = _body
        if pay_pal_request_id is not None:
            _header_params["PayPal-Request-Id"] = pay_pal_request_id
        if prefer is not None:
            _header_params["Prefer"] = prefer
        if pay_pal_client_metadata_id is not None:
            _header_params["PayPal-Client-Metadata-Id"] = pay_pal_client_metadata_id
        if pay_pal_auth_assertion is not None:
            _header_params["PayPal-Auth-Assertion"] = pay_pal_auth_assertion
        if id is not None:
            _path_params["id"] = id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _acapture_payment_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Capture payment for order
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_prefer,
            request_header_pay_pal_client_metadata_id,
            request_header_pay_pal_auth_assertion,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/checkout/orders/{id}/capture',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_order_capture_request.serialize(body, content_type)
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


    def _capture_payment_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Capture payment for order
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_prefer,
            request_header_pay_pal_client_metadata_id,
            request_header_pay_pal_auth_assertion,
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
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/checkout/orders/{id}/capture',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_order_capture_request.serialize(body, content_type)
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


class CapturePaymentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acapture_payment(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._capture_payment_mapped_args(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return await self._acapture_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def capture_payment(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._capture_payment_mapped_args(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return self._capture_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class CapturePayment(BaseApi):

    async def acapture_payment(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OrderPydantic:
        raw_response = await self.raw.acapture_payment(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            **kwargs,
        )
        if validate:
            return RootModel[OrderPydantic](raw_response.body).root
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)
    
    
    def capture_payment(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OrderPydantic:
        raw_response = self.raw.capture_payment(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        if validate:
            return RootModel[OrderPydantic](raw_response.body).root
        return api_client.construct_model_instance(OrderPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._capture_payment_mapped_args(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return await self._acapture_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        id: str,
        payment_source: typing.Optional[PaymentSource] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_client_metadata_id: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._capture_payment_mapped_args(
            id=id,
            payment_source=payment_source,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_client_metadata_id=pay_pal_client_metadata_id,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return self._capture_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

