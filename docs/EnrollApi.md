# openziti_edge_client.EnrollApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enroll**](EnrollApi.md#enroll) | **POST** /enroll | Enroll an identity via one-time-token
[**enroll_ca**](EnrollApi.md#enroll_ca) | **POST** /enroll/ca | Enroll an identity with a pre-exchanged certificate
[**enroll_er_ott**](EnrollApi.md#enroll_er_ott) | **POST** /enroll/erott | Enroll an edge-router
[**enroll_ott**](EnrollApi.md#enroll_ott) | **POST** /enroll/ott | Enroll an identity via one-time-token
[**enroll_ott_ca**](EnrollApi.md#enroll_ott_ca) | **POST** /enroll/ottca | Enroll an identity via one-time-token with a pre-exchanged client certificate
[**ernoll_updb**](EnrollApi.md#ernoll_updb) | **POST** /enroll/updb | Enroll an identity via one-time-token
[**extend_current_identity_authenticator**](EnrollApi.md#extend_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend | Allows the current identity to recieve a new certificate associated with a certificate based authenticator
[**extend_router_enrollment**](EnrollApi.md#extend_router_enrollment) | **POST** /enroll/extend/router | Extend the life of a currently enrolled router&#39;s certificates
[**extend_verify_current_identity_authenticator**](EnrollApi.md#extend_verify_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend-verify | Allows the current identity to validate reciept of a new client certificate


# **enroll**
> Empty enroll()

Enroll an identity via one-time-token

present a OTT and CSR to receive a long-lived client certificate

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    token = "token_example" # str |  (optional)
    method = "method_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.enroll(token=token, method=method)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->enroll: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional]
 **method** | **str**|  | [optional]

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-pem-file, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ca**
> Empty enroll_ca()

Enroll an identity with a pre-exchanged certificate

For CA auto enrollment, an identity is not created beforehand. Instead one will be created during enrollment. The client will present a client certificate that is signed by a Certificate Authority that has been added and verified (See POST /cas and POST /cas/{id}/verify).  During this process no CSRs are requires as the client should already be in possession of a valid certificate. 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enroll an identity with a pre-exchanged certificate
        api_response = api_instance.enroll_ca()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->enroll_ca: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_er_ott**
> EnrollmentCertsEnvelope enroll_er_ott(token)

Enroll an edge-router

Enrolls an edge-router via a one-time-token to establish a certificate based identity. 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.enrollment_certs_envelope import EnrollmentCertsEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enroll an edge-router
        api_response = api_instance.enroll_er_ott(token)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->enroll_er_ott: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

[**EnrollmentCertsEnvelope**](EnrollmentCertsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing the edge routers signed certificates (server chain, server cert, CAs). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ott**
> str enroll_ott(token)

Enroll an identity via one-time-token

Enroll an identity via a one-time-token which is supplied via a query string parameter. This enrollment method expects a PEM encoded CSRs to be provided for fulfillment. It is up to the enrolling identity to manage the private key backing the CSR request. 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.enroll_ott(token)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->enroll_ott: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-x509-user-cert, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PEM encoded certificate signed by the internal Ziti CA |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ott_ca**
> Empty enroll_ott_ca(token)

Enroll an identity via one-time-token with a pre-exchanged client certificate

Enroll an identity via a one-time-token that also requires a pre-exchanged client certificate to match a Certificate Authority that has been added and verified (See POST /cas and POST /cas{id}/verify). The client must present a client certificate signed by CA associated with the enrollment. This enrollment is similar to CA auto enrollment except that is required the identity to be pre-created.  As the client certificate has been pre-exchanged there is no CSR input to this enrollment method. 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enroll an identity via one-time-token with a pre-exchanged client certificate
        api_response = api_instance.enroll_ott_ca(token)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->enroll_ott_ca: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ernoll_updb**
> Empty ernoll_updb(token)

Enroll an identity via one-time-token

Enrolls an identity via a one-time-token to establish an initial username and password combination 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    token = "token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.ernoll_updb(token)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->ernoll_updb: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  |

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_current_identity_authenticator**
> IdentityExtendEnrollmentEnvelope extend_current_identity_authenticator(id, extend)

Allows the current identity to recieve a new certificate associated with a certificate based authenticator

This endpoint only functions for certificates issued by the controller. 3rd party certificates are not handled. Allows an identity to extend its certificate's expiration date by using its current and valid client certificate to submit a CSR. This CSR may be passed in using a new private key, thus allowing private key rotation. The response from this endpoint is a new client certificate which the client must  be verified via the /authenticators/{id}/extend-verify endpoint. After verification is completion any new connections must be made with new certificate. Prior to verification the old client certificate remains active.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.identity_extend_enrollment_envelope import IdentityExtendEnrollmentEnvelope
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.identity_extend_enrollment_request import IdentityExtendEnrollmentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    id = "id_example" # str | The id of the requested resource
    extend = IdentityExtendEnrollmentRequest(
        client_cert_csr="client_cert_csr_example",
    ) # IdentityExtendEnrollmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Allows the current identity to recieve a new certificate associated with a certificate based authenticator
        api_response = api_instance.extend_current_identity_authenticator(id, extend)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->extend_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **extend** | [**IdentityExtendEnrollmentRequest**](IdentityExtendEnrollmentRequest.md)|  |

### Return type

[**IdentityExtendEnrollmentEnvelope**](IdentityExtendEnrollmentEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containg the identity&#39;s new certificate |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_router_enrollment**
> EnrollmentCertsEnvelope extend_router_enrollment(router_extend_enrollment_request)

Extend the life of a currently enrolled router's certificates

Allows a router to extend its certificates' expiration date by using its current and valid client certificate to submit a CSR. This CSR may be passed in using a new private key, thus allowing private key rotation or swapping.  After completion any new connections must be made with certificates returned from a 200 OK response. The previous client certificate is rendered invalid for use with the controller even if it has not expired.  This request must be made using the existing, valid, client certificate. 

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.router_extend_enrollment_request import RouterExtendEnrollmentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    router_extend_enrollment_request = RouterExtendEnrollmentRequest(
        cert_csr="cert_csr_example",
        server_cert_csr="server_cert_csr_example",
    ) # RouterExtendEnrollmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Extend the life of a currently enrolled router's certificates
        api_response = api_instance.extend_router_enrollment(router_extend_enrollment_request)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->extend_router_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_extend_enrollment_request** | [**RouterExtendEnrollmentRequest**](RouterExtendEnrollmentRequest.md)|  |

### Return type

[**EnrollmentCertsEnvelope**](EnrollmentCertsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containg the edge routers new signed certificates (server chain, server cert, CAs). |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_verify_current_identity_authenticator**
> Empty extend_verify_current_identity_authenticator(id, extend)

Allows the current identity to validate reciept of a new client certificate

After submitting a CSR for a new client certificate the resulting public certificate must be re-submitted to this endpoint to verify receipt. After receipt, the new client certificate must be used for new authentication requests.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import enroll_api
from openziti_edge_client.model.identity_extend_validate_enrollment_request import IdentityExtendValidateEnrollmentRequest
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.empty import Empty
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enroll_api.EnrollApi(api_client)
    id = "id_example" # str | The id of the requested resource
    extend = IdentityExtendValidateEnrollmentRequest(
        client_cert="client_cert_example",
    ) # IdentityExtendValidateEnrollmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Allows the current identity to validate reciept of a new client certificate
        api_response = api_instance.extend_verify_current_identity_authenticator(id, extend)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EnrollApi->extend_verify_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **extend** | [**IdentityExtendValidateEnrollmentRequest**](IdentityExtendValidateEnrollmentRequest.md)|  |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

