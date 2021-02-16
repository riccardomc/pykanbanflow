# pykanbanflow.DefaultApi

All URIs are relative to *https://kanbanflow.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_board**](DefaultApi.md#get_board) | **GET** /board | Returns the structure of the board belonging to the token.

# **get_board**
> Board get_board()

Returns the structure of the board belonging to the token.

### Example
```python
from __future__ import print_function
import time
import pykanbanflow
from pykanbanflow.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pykanbanflow.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pykanbanflow.DefaultApi(pykanbanflow.ApiClient(configuration))

try:
    # Returns the structure of the board belonging to the token.
    api_response = api_instance.get_board()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_board: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Board**](Board.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

