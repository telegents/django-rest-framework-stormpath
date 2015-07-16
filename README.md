Django REST Framework Stormpath Auth Integration
================================================

# Overview

This package verifies Stormpath generated authTokens and creates a custom
Django user model populated with Stormpath accounts `customData` that can be
used for Django REST Framework resource authorization.

Can be used for creating microservices with Django REST framework with
centralized authentication hosted at Stormpath.

Users can authenticate against Stormpath to generate a JSON Web Token and pass
that token in the Authorization header for requests to Django REST Framework
instances utilizing this library for authentication.

# Usage

Add the method to the `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']` in `settings.py`

```
REST_FRAMEWORK = {
    # ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_stormpath.authentication.StormpathAuthentication',
    ),
}
```

Also, specify your Stormpath credentials in `settings.py`

```
STORMPATH_ID = '<apiKey>'
STORMPATH_SECRET = '<apiSecret>'
STORMPATH_APPLICATION = 'https://api.stormpath.com/v1/applications/<appId>'
``` 

Now, simply pass your Stormpath generated JSON Web Token in requests

`curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/<resource>`

Currently, you have to manually check the request.user.customData.  Hey, it's alpha.

# Requirements
* Python
* Django
* Django REST Framework

# Installation

`pip install djangorestframework-stormpath`

# TODO

* Documentation
* Django REST Framework Authorization library
* General improvements


