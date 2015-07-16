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


