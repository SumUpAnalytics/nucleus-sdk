# swagger_client.UsersApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UsersApi.md#get_user) | **GET** /users/ | 
[**post_user**](UsersApi.md#post_user) | **POST** /users/ | 


# **get_user**
> GetUserKeyModel get_user(user_email, password)



Use this API to authenticate. If the password is correct, returns the user details, including the user's api key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_email = 'user_email_example' # str | Email of the user to authenticate. 
password = 'password_example' # str | Plaintext password of the user to authenticate. 

try:
    api_response = api_instance.get_user(user_email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| Email of the user to authenticate.  | 
 **password** | **str**| Plaintext password of the user to authenticate.  | 

### Return type

[**GetUserKeyModel**](GetUserKeyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user**
> UserRegisterModel post_user(user_email, password, x_api_key, first_name=first_name, last_name=last_name, phone=phone, company=company, title=title, country=country)



Use this API to register a new user. Email and password are required, all other fields optional.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_email = 'user_email_example' # str | Email of the user to register. 
password = 'password_example' # str | Password of the user to register. 
x_api_key = 'x_api_key_example' # str | API key for authentication.
first_name = 'first_name_example' # str | First name of the user to register.  (optional)
last_name = 'last_name_example' # str | Last name of the user to register.  (optional)
phone = 56 # int | Phone number (int) of the user to register.  (optional)
company = 'company_example' # str | Name of the Company of the user.  (optional)
title = 'title_example' # str | Job title.  (optional)
country = 'country_example' # str | Country of origin.  (optional)

try:
    api_response = api_instance.post_user(user_email, password, x_api_key, first_name=first_name, last_name=last_name, phone=phone, company=company, title=title, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**| Email of the user to register.  | 
 **password** | **str**| Password of the user to register.  | 
 **x_api_key** | **str**| API key for authentication. | 
 **first_name** | **str**| First name of the user to register.  | [optional] 
 **last_name** | **str**| Last name of the user to register.  | [optional] 
 **phone** | **int**| Phone number (int) of the user to register.  | [optional] 
 **company** | **str**| Name of the Company of the user.  | [optional] 
 **title** | **str**| Job title.  | [optional] 
 **country** | **str**| Country of origin.  | [optional] 

### Return type

[**UserRegisterModel**](UserRegisterModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

