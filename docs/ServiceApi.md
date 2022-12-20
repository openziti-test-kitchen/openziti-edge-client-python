# openziti_edge_client.ServiceApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service**](ServiceApi.md#delete_service) | **DELETE** /services/{id} | Delete a service
[**detail_service**](ServiceApi.md#detail_service) | **GET** /services/{id} | Retrieves a single service
[**list_service_terminators**](ServiceApi.md#list_service_terminators) | **GET** /services/{id}/terminators | List of terminators assigned to a service
[**list_services**](ServiceApi.md#list_services) | **GET** /services | List services
[**patch_service**](ServiceApi.md#patch_service) | **PATCH** /services/{id} | Update the supplied fields on a service
[**update_service**](ServiceApi.md#update_service) | **PUT** /services/{id} | Update all fields on a service


# **delete_service**
> Empty delete_service(id)

Delete a service

Delete a service by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
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

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_api.ServiceApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Delete a service
        api_response = api_instance.delete_service(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request was successful and the resource has been removed |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_service**
> DetailServiceEnvelope detail_service(id)

Retrieves a single service

Retrieves a single service by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.detail_service_envelope import DetailServiceEnvelope
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
    api_instance = service_api.ServiceApi(api_client)
    id = "id_example" # str | The id of the requested resource

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a single service
        api_response = api_instance.detail_service(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->detail_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |

### Return type

[**DetailServiceEnvelope**](DetailServiceEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single service |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |
**404** | The requested resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_terminators**
> ListClientTerminatorsEnvelope list_service_terminators(id)

List of terminators assigned to a service

Retrieves a list of terminator resources that are assigned specific service; supports filtering, sorting, and pagination. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_client_terminators_envelope import ListClientTerminatorsEnvelope
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
    api_instance = service_api.ServiceApi(api_client)
    id = "id_example" # str | The id of the requested resource
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List of terminators assigned to a service
        api_response = api_instance.list_service_terminators(id)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->list_service_terminators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of terminators assigned to a service
        api_response = api_instance.list_service_terminators(id, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->list_service_terminators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**ListClientTerminatorsEnvelope**](ListClientTerminatorsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of terminators |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services**
> ListServicesEnvelope list_services()

List services

Retrieves a list of config resources; supports filtering, sorting, and pagination. Requires admin access. 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_services_envelope import ListServicesEnvelope
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
    api_instance = service_api.ServiceApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    filter = "filter_example" # str |  (optional)
    role_filter = [
        "roleFilter_example",
    ] # [str] |  (optional)
    role_semantic = "roleSemantic_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List services
        api_response = api_instance.list_services(limit=limit, offset=offset, filter=filter, role_filter=role_filter, role_semantic=role_semantic)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->list_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **filter** | **str**|  | [optional]
 **role_filter** | **[str]**|  | [optional]
 **role_semantic** | **str**|  | [optional]

### Return type

[**ListServicesEnvelope**](ListServicesEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of services |  -  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service**
> Empty patch_service(id, service)

Update the supplied fields on a service

Update the supplied fields on a service. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.service_patch import ServicePatch
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

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_api.ServiceApi(api_client)
    id = "id_example" # str | The id of the requested resource
    service = ServicePatch(
        configs=[
            "configs_example",
        ],
        encryption_required=True,
        name="name_example",
        role_attributes=[
            "role_attributes_example",
        ],
        tags=Tags(None),
        terminator_strategy="terminator_strategy_example",
    ) # ServicePatch | A service patch object

    # example passing only required values which don't have defaults set
    try:
        # Update the supplied fields on a service
        api_response = api_instance.patch_service(id, service)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->patch_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **service** | [**ServicePatch**](ServicePatch.md)| A service patch object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

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

# **update_service**
> Empty update_service(id, service)

Update all fields on a service

Update all fields on a service by id. Requires admin access.

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import service_api
from openziti_edge_client.model.service_update import ServiceUpdate
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

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_api.ServiceApi(api_client)
    id = "id_example" # str | The id of the requested resource
    service = ServiceUpdate(
        configs=[
            "configs_example",
        ],
        encryption_required=True,
        name="name_example",
        role_attributes=[
            "role_attributes_example",
        ],
        tags=Tags(None),
        terminator_strategy="terminator_strategy_example",
    ) # ServiceUpdate | A service update object

    # example passing only required values which don't have defaults set
    try:
        # Update all fields on a service
        api_response = api_instance.update_service(id, service)
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource |
 **service** | [**ServiceUpdate**](ServiceUpdate.md)| A service update object |

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession)

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

