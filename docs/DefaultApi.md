# pykanbanflow.DefaultApi

All URIs are relative to *https://kanbanflow.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_tasks**](DefaultApi.md#get_all_tasks) | **GET** /tasks | Return all tasks on a board
[**get_board**](DefaultApi.md#get_board) | **GET** /board | Returns the structure of the board belonging to the token.
[**get_task_by_id**](DefaultApi.md#get_task_by_id) | **GET** /tasks/{taskId} | Returns a single task by ID

# **get_all_tasks**
> list[TasksByColumn] get_all_tasks()

Return all tasks on a board

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
    # Return all tasks on a board
    api_response = api_instance.get_all_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TasksByColumn]**](TasksByColumn.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_task_by_id**
> Task get_task_by_id(task_id, include_position=include_position)

Returns a single task by ID

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
task_id = 'task_id_example' # str | The ID of the task to return
include_position = true # bool | Include the task's position in the column/swimlane it is in (optional)

try:
    # Returns a single task by ID
    api_response = api_instance.get_task_by_id(task_id, include_position=include_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The ID of the task to return | 
 **include_position** | **bool**| Include the task&#x27;s position in the column/swimlane it is in | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

