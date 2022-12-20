# openziti_edge_client.PostureChecksApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posture_response**](PostureChecksApi.md#create_posture_response) | **POST** /posture-response | Submit a posture response to a posture query
[**create_posture_response_bulk**](PostureChecksApi.md#create_posture_response_bulk) | **POST** /posture-response-bulk | Submit multiple posture responses


# **create_posture_response**
> PostureResponseEnvelope create_posture_response(posture_response)

Submit a posture response to a posture query

Submits posture responses

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import posture_checks_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.posture_response_create import PostureResponseCreate
from openziti_edge_client.model.posture_response_envelope import PostureResponseEnvelope
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
    api_instance = posture_checks_api.PostureChecksApi(api_client)
    posture_response = PostureResponseCreate() # PostureResponseCreate | A Posture Response

    # example passing only required values which don't have defaults set
    try:
        # Submit a posture response to a posture query
        api_response = api_instance.create_posture_response(posture_response)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling PostureChecksApi->create_posture_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_response** | [**PostureResponseCreate**](PostureResponseCreate.md)| A Posture Response |

### Return type

[**PostureResponseEnvelope**](PostureResponseEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contains a list of services that have had their timers altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posture_response_bulk**
> PostureResponseEnvelope create_posture_response_bulk(posture_response)

Submit multiple posture responses

Submits posture responses

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import posture_checks_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.posture_response_create import PostureResponseCreate
from openziti_edge_client.model.posture_response_envelope import PostureResponseEnvelope
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
    api_instance = posture_checks_api.PostureChecksApi(api_client)
    posture_response = [
        PostureResponseCreate(),
    ] # [PostureResponseCreate] | A Posture Response

    # example passing only required values which don't have defaults set
    try:
        # Submit multiple posture responses
        api_response = api_instance.create_posture_response_bulk(posture_response)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling PostureChecksApi->create_posture_response_bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_response** | [**[PostureResponseCreate]**](PostureResponseCreate.md)| A Posture Response |

### Return type

[**PostureResponseEnvelope**](PostureResponseEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains a list of services that have had their timers altered |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

