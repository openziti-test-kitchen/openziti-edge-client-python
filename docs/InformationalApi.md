# openziti_edge_client.InformationalApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detail_spec**](InformationalApi.md#detail_spec) | **GET** /specs/{id} | Return a single spec resource
[**detail_spec_body**](InformationalApi.md#detail_spec_body) | **GET** /specs/{id}/spec | Returns the spec&#39;s file
[**list_protocols**](InformationalApi.md#list_protocols) | **GET** /protocols | Return a list of the listening Edge protocols
[**list_root**](InformationalApi.md#list_root) | **GET** / | Returns version information
[**list_specs**](InformationalApi.md#list_specs) | **GET** /specs | Returns a list of API specs
[**list_version**](InformationalApi.md#list_version) | **GET** /version | Returns version information


# **detail_spec**
> DetailSpecEnvelope detail_spec(id)

Return a single spec resource

Returns single spec resource embedded within the controller for consumption/documentation/code geneartion

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.detail_spec_envelope import DetailSpecEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Return a single spec resource
        api_response = api_instance.detail_spec(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->detail_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailSpecEnvelope**](DetailSpecEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_spec_body**
> DetailSpecBodyEnvelope detail_spec_body(id)

Returns the spec's file

Return the body of the specification (i.e. Swagger, OpenAPI 2.0, 3.0, etc).

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.detail_spec_body_envelope import DetailSpecBodyEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Returns the spec's file
        api_response = api_instance.detail_spec_body(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->detail_spec_body: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailSpecBodyEnvelope**](DetailSpecBodyEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/yaml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the document that represents the specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_protocols**
> ListProtocolsEnvelope list_protocols()

Return a list of the listening Edge protocols

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.list_protocols_envelope import ListProtocolsEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return a list of the listening Edge protocols
        api_response = api_instance.list_protocols()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->list_protocols: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListProtocolsEnvelope**](ListProtocolsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of supported Edge protocols |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_root**
> ListVersionEnvelope list_root()

Returns version information

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.list_version_envelope import ListVersionEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns version information
        api_response = api_instance.list_root()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->list_root: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVersionEnvelope**](ListVersionEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information for the controller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_specs**
> ListSpecsEnvelope list_specs()

Returns a list of API specs

Returns a list of spec files embedded within the controller for consumption/documentation/code geneartion

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.list_specs_envelope import ListSpecsEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a list of API specs
        api_response = api_instance.list_specs()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->list_specs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSpecsEnvelope**](ListSpecsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of specifications |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version**
> ListVersionEnvelope list_version()

Returns version information

### Example


```python
import time
import openziti_edge_client
from openziti_edge_client.api import informational_api
from openziti_edge_client.model.list_version_envelope import ListVersionEnvelope
from pprint import pprint
# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = informational_api.InformationalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns version information
        api_response = api_instance.list_version()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling InformationalApi->list_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVersionEnvelope**](ListVersionEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information for the controller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

