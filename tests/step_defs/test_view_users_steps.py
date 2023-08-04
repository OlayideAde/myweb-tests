import pytest
import unittest
import requests
import json
from service.api_service import API
from unittest.mock import MagicMock, patch
from pytest_bdd import scenario, given, when, then, parsers


@pytest.fixture(scope='session')
def context():
    return {}


@scenario('../features/view_users.feature', 'API admin user can get list of users')
def scenario_api():
    #    print("Tests finished")
    pass


@given("I am logged in as admin user")
def test_admin_user_is_logged_in():
    """Admin user is logged in"""


@when("I request API GET api/v1/users")
@patch('mywebtests.service.api_service.requests.get')
def test_request_users(self):
    mock_response = MagicMock()
    mock_response.return_value.ok = True
    mock_response.status_code = 200
    with open('./tests/resources/users.json') as users:
        mock_response.json.return_value = json.loads(users.read())

    # mock_api_call = mock_response
    # call service with mock
    api_service = API('api.myweb.com')
    response = api_service.request('GET', 'api/v1/users')
    # store response body and status code for next steps
    context['response_body'] = response.json.return_value
    context['status_code'] = response.status_code
    # assert request is ok
    self.assertIsNotNone(response)


@then("I get HTTP 200 status code")
def verify_status_code(self):
    self.assertEqual(context['status_code'], 200)


@then("I get JSON in response body")
def verify_response_body(self):
    with open('../resources/users.json') as users:
        self.assertEqual(context['response_body'], json.loads(users.read()))


@then("the HTTP response body contains a page with 4 users")
def verify_response_length():
    """"""""


@then(parsers.parse('1 of them is "{phrase}"'))
def verify_admin_is_in_user_list():
    """"""""


# @scenario('../features/view_users.feature', 'Frontend admin users can get list of users')

# def test_scenario_browser():
#    pass

# @given('I am logged in as admin user')

# @when('I visit the Users page')

# @then('4 users are listed')

# @And('1 of them is "Administrator" role')
