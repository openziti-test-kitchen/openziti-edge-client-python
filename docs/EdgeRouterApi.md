# openziti_edge_client.EdgeRouterApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_identity_edge_routers**](EdgeRouterApi.md#get_current_identity_edge_routers) | **GET** /current-identity/edge-routers | Return this list of Edge Routers the identity has access to


# **get_current_identity_edge_routers**
> ListCurrentIdentityEdgeRoutersEnvelope get_current_identity_edge_routers()

Return this list of Edge Routers the identity has access to

Lists the Edge Routers that the current identity has access to via policies. The data returned includes their address and online status 

### Example

* Api Key Authentication (ztSession):

```python
import time
import openziti_edge_client
from openziti_edge_client.api import edge_router_api
from openziti_edge_client.model.api_error_envelope import ApiErrorEnvelope
from openziti_edge_client.model.list_current_identity_edge_routers_envelope import ListCurrentIdentityEdgeRoutersEnvelope
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
    api_instance = edge_router_api.EdgeRouterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return this list of Edge Routers the identity has access to
        api_response = api_instance.get_current_identity_edge_routers()
        pprint(api_response)
    except openziti_edge_client.ApiException as e:
        print("Exception when calling EdgeRouterApi->get_current_identity_edge_routers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCurrentIdentityEdgeRoutersEnvelope**](ListCurrentIdentityEdgeRoutersEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of edge routers |  -  |
**401** | The currently supplied session does not have the correct access rights to request this resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

