# openziti_edge_client.ExternalJWTSignerApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_external_jwt_signers**](ExternalJWTSignerApi.md#list_external_jwt_signers) | **GET** /external-jwt-signers | List Client Authentication External JWT


# **list_external_jwt_signers**
> ListClientExternalJwtSignersEnvelope list_external_jwt_signers()

List Client Authentication External JWT

Retrieves a list of external JWT signers for authentication

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import external_jwt_signer_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_client_external_jwt_signers_envelope import ListClientExternalJwtSignersEnvelope
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

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = external_jwt_signer_api.ExternalJWTSignerApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Client Authentication External JWT
        api_response = api_instance.list_external_jwt_signers(limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ExternalJWTSignerApi->list_external_jwt_signers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListClientExternalJwtSignersEnvelope**](ListClientExternalJwtSignersEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of External JWT Signers |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

