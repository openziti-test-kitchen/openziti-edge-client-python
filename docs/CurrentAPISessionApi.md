# openziti_edge_client.CurrentAPISessionApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_current_api_session_certificate**](CurrentAPISessionApi.md#create_current_api_session_certificate) | **POST** /current-api-session/certificates | Creates an ephemeral certificate for the current API Session
[**current_api_session_delete**](CurrentAPISessionApi.md#current_api_session_delete) | **DELETE** /current-api-session | Logout
[**delete_current_api_session_certificate**](CurrentAPISessionApi.md#delete_current_api_session_certificate) | **DELETE** /current-api-session/certificates/{id} | Delete an ephemeral certificate
[**detail_current_api_session_certificate**](CurrentAPISessionApi.md#detail_current_api_session_certificate) | **GET** /current-api-session/certificates/{id} | Retrieves an ephemeral certificate
[**detail_current_identity_authenticator**](CurrentAPISessionApi.md#detail_current_identity_authenticator) | **GET** /current-identity/authenticators/{id} | Retrieve an authenticator for the current identity
[**extend_current_identity_authenticator**](CurrentAPISessionApi.md#extend_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend | Allows the current identity to recieve a new certificate associated with a certificate based authenticator
[**extend_verify_current_identity_authenticator**](CurrentAPISessionApi.md#extend_verify_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend-verify | Allows the current identity to validate reciept of a new client certificate
[**get_current_api_session**](CurrentAPISessionApi.md#get_current_api_session) | **GET** /current-api-session | Return the current API session
[**list_current_api_session_certificates**](CurrentAPISessionApi.md#list_current_api_session_certificates) | **GET** /current-api-session/certificates | List the ephemeral certificates available for the current API Session
[**list_current_identity_authenticators**](CurrentAPISessionApi.md#list_current_identity_authenticators) | **GET** /current-identity/authenticators | List authenticators for the current identity
[**list_service_updates**](CurrentAPISessionApi.md#list_service_updates) | **GET** /current-api-session/service-updates | Returns data indicating whether a client should updates it service list
[**patch_current_identity_authenticator**](CurrentAPISessionApi.md#patch_current_identity_authenticator) | **PATCH** /current-identity/authenticators/{id} | Update the supplied fields on an authenticator of this identity
[**update_current_identity_authenticator**](CurrentAPISessionApi.md#update_current_identity_authenticator) | **PUT** /current-identity/authenticators/{id} | Update all fields on an authenticator of this identity


# **create_current_api_session_certificate**
> CreateCurrentApiSessionCertificateEnvelope create_current_api_session_certificate(session_certificate)

Creates an ephemeral certificate for the current API Session

Creates an ephemeral certificate for the current API Session. This endpoint expects a PEM encoded CSRs to be provided for fulfillment as a property of a JSON payload. It is up to the client to manage the private key backing the CSR request.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.current_api_session_certificate_create import CurrentApiSessionCertificateCreate
from openziti_edge_client.model.create_current_api_session_certificate_envelope import CreateCurrentApiSessionCertificateEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    session_certificate = CurrentApiSessionCertificateCreate(
        csr="csr_example",
    ) # CurrentApiSessionCertificateCreate | The payload describing the CSR used to create a session certificate

    # example passing only required values which don't have defaults set
    try:
        # Creates an ephemeral certificate for the current API Session
        api_response = api_instance.create_current_api_session_certificate(session_certificate)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->create_current_api_session_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_certificate** | [**CurrentApiSessionCertificateCreate**](CurrentApiSessionCertificateCreate.md)| The payload describing the CSR used to create a session certificate |

### Return type

[**CreateCurrentApiSessionCertificateEnvelope**](CreateCurrentApiSessionCertificateEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A response of a create API Session certificate |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_api_session_delete**
> Empty current_api_session_delete()

Logout

Terminates the current API session

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_response = api_instance.current_api_session_delete()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->current_api_session_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_current_api_session_certificate**
> Empty delete_current_api_session_certificate(id)

Delete an ephemeral certificate

Delete an ephemeral certificateby id 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete an ephemeral certificate
        api_response = api_instance.delete_current_api_session_certificate(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->delete_current_api_session_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**Empty**](Empty.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request was successful and the resource has been removed |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_current_api_session_certificate**
> DetailCurrentApiSessionCertificateEnvelope detail_current_api_session_certificate(id)

Retrieves an ephemeral certificate

Retrieves a single ephemeral certificate by id

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.detail_current_api_session_certificate_envelope import DetailCurrentApiSessionCertificateEnvelope
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves an ephemeral certificate
        api_response = api_instance.detail_current_api_session_certificate(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->detail_current_api_session_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailCurrentApiSessionCertificateEnvelope**](DetailCurrentApiSessionCertificateEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing a single API Session certificate |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_current_identity_authenticator**
> DetailAuthenticatorEnvelope detail_current_identity_authenticator(id)

Retrieve an authenticator for the current identity

Retrieves a single authenticator by id. Will only show authenticators assigned to the API session's identity.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.detail_authenticator_envelope import DetailAuthenticatorEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an authenticator for the current identity
        api_response = api_instance.detail_current_identity_authenticator(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->detail_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailAuthenticatorEnvelope**](DetailAuthenticatorEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A singular authenticator resource |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_current_identity_authenticator**
> IdentityExtendEnrollmentEnvelope extend_current_identity_authenticator(id, extend)

Allows the current identity to recieve a new certificate associated with a certificate based authenticator

This endpoint only functions for certificates issued by the controller. 3rd party certificates are not handled. Allows an identity to extend its certificate's expiration date by using its current and valid client certificate to submit a CSR. This CSR may be passed in using a new private key, thus allowing private key rotation. The response from this endpoint is a new client certificate which the client must  be verified via the /authenticators/{id}/extend-verify endpoint. After verification is completion any new connections must be made with new certificate. Prior to verification the old client certificate remains active.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
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
        print("Exception when calling CurrentAPISessionApi->extend_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **extend** | [**IdentityExtendEnrollmentRequest**](IdentityExtendEnrollmentRequest.md)|  |

### Return type

[**IdentityExtendEnrollmentEnvelope**](IdentityExtendEnrollmentEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containg the identity&#39;s new certificate |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_verify_current_identity_authenticator**
> Empty extend_verify_current_identity_authenticator(id, extend)

Allows the current identity to validate reciept of a new client certificate

After submitting a CSR for a new client certificate the resulting public certificate must be re-submitted to this endpoint to verify receipt. After receipt, the new client certificate must be used for new authentication requests.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
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
        print("Exception when calling CurrentAPISessionApi->extend_verify_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **extend** | [**IdentityExtendValidateEnrollmentRequest**](IdentityExtendValidateEnrollmentRequest.md)|  |

### Return type

[**Empty**](Empty.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_api_session**
> CurrentApiSessionDetailEnvelope get_current_api_session()

Return the current API session

Retrieves the API session that was used to issue the current request

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.current_api_session_detail_envelope import CurrentApiSessionDetailEnvelope
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the current API session
        api_response = api_instance.get_current_api_session()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->get_current_api_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentApiSessionDetailEnvelope**](CurrentApiSessionDetailEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, default


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API session associated with the session used to issue the request |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_api_session_certificates**
> ListCurrentApiSessionCertificatesEnvelope list_current_api_session_certificates()

List the ephemeral certificates available for the current API Session

Retrieves a list of certificate resources for the current API session; supports filtering, sorting, and pagination

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_current_api_session_certificates_envelope import ListCurrentApiSessionCertificatesEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the ephemeral certificates available for the current API Session
        api_response = api_instance.list_current_api_session_certificates(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->list_current_api_session_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListCurrentApiSessionCertificatesEnvelope**](ListCurrentApiSessionCertificatesEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of the current API Session&#39;s certificate |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_identity_authenticators**
> ListAuthenticatorsEnvelope list_current_identity_authenticators()

List authenticators for the current identity

Retrieves a list of authenticators assigned to the current API session's identity; supports filtering, sorting, and pagination.

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.list_authenticators_envelope import ListAuthenticatorsEnvelope
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List authenticators for the current identity
        api_response = api_instance.list_current_identity_authenticators(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->list_current_identity_authenticators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListAuthenticatorsEnvelope**](ListAuthenticatorsEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of authenticators |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_updates**
> ListCurrentApiSessionServiceUpdatesEnvelope list_service_updates()

Returns data indicating whether a client should updates it service list

Retrieves data indicating the last time data relevant to this API Session was altered that would necessitate service refreshes. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_current_api_session_service_updates_envelope import ListCurrentApiSessionServiceUpdatesEnvelope
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns data indicating whether a client should updates it service list
        api_response = api_instance.list_service_updates()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->list_service_updates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCurrentApiSessionServiceUpdatesEnvelope**](ListCurrentApiSessionServiceUpdatesEnvelope.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data indicating necessary service updates |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_current_identity_authenticator**
> Empty patch_current_identity_authenticator(id, authenticator)

Update the supplied fields on an authenticator of this identity

Update the supplied fields on an authenticator by id. Will only update authenticators assigned to the API session's identity. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.empty import Empty
from openziti_edge_client.model.authenticator_patch_with_current import AuthenticatorPatchWithCurrent
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    id = "id_example" # str | The id of the requested resource
    authenticator = AuthenticatorPatchWithCurrent(None) # AuthenticatorPatchWithCurrent | An authenticator patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on an authenticator of this identity
        api_response = api_instance.patch_current_identity_authenticator(id, authenticator)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->patch_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **authenticator** | [**AuthenticatorPatchWithCurrent**](AuthenticatorPatchWithCurrent.md)| An authenticator patch object |

### Return type

[**Empty**](Empty.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The patch request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_identity_authenticator**
> Empty update_current_identity_authenticator(id, authenticator)

Update all fields on an authenticator of this identity

Update all fields on an authenticator by id.  Will only update authenticators assigned to the API session's identity. 

### Example

* OAuth Authentication (oauth2):
* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import current_api_session_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.authenticator_update_with_current import AuthenticatorUpdateWithCurrent
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

# Configure OAuth2 access token for authorization: oauth2
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_api_session_api.CurrentAPISessionApi(api_client)
    id = "id_example" # str | The id of the requested resource
    authenticator = AuthenticatorUpdateWithCurrent(None) # AuthenticatorUpdateWithCurrent | An authenticator put object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on an authenticator of this identity
        api_response = api_instance.update_current_identity_authenticator(id, authenticator)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling CurrentAPISessionApi->update_current_identity_authenticator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **authenticator** | [**AuthenticatorUpdateWithCurrent**](AuthenticatorUpdateWithCurrent.md)| An authenticator put object |

### Return type

[**Empty**](Empty.md)

### Authorization

[oauth2](../README.md#oauth2), [ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The update request was successful and the resource has been altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

