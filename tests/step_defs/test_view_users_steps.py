import pytest
import json
from unittest.mock import MagicMock, patch
from pytest_bdd import scenario, given, when, then, parsers
from services.api import API

#@pytest.fixture(scope='session')
#def step_context():
#    return {'response': None}


@scenario('../features/view_users.feature', 'API admin user can get list of users')

def scenario_api():
    print("Tests finished")
    pass

@given("I am logged in as admin user")
def admin_user_is_logged_in():
    """Admin user is logged in"""
    pass


@when("I request API GET api/v1/users")

@patch('mywebtests.services.api.requests.get')
def request_users(self, mock_requests):
    
    mock_response = MagicMock()
    mock_response.return_value.ok = True
    mock_response.status_code = 200
    with open('../resources/users.json') as users:
        mock_response.json.return_value = json.loads(users.read())
     
    mock_requests.get.return_value = mock_response
    
    api = API('api.myweb.com')
    response = api.request('GET', 'api/v1/users')
    self.assertIsNotNone(response)
    
@then("I get HTTP 200 status code")
@patch('myweb-tests.services.api.requests.get')
def verify_status_code(self, mock_requests):
    mock_response = MagicMock()
    mock_response.return_value.ok = True
    mock_response.status_code = 200
    with open('../resources/users.json') as users:
        mock_response.json.return_value = json.loads(users.read())
     
    mock_requests.get.return_value = mock_response
    
    api = API('api.myweb.com')
    response = api.request('GET', 'api/v1/users')
    self.assertIsNotNone(response)
    self.assertIsTrue(response.status_code, 200)
 

#@And("I get JSON in response body")
#def verify_response_body():
    """"""""
      

#@And("the HTTP response body contains a page with 4 users")
#def verify_response_length():
    """"""""

#@And(parsers.parse('1 of them is "{Administrator}"'))
#def verify_admin_is_in_user_list():
    """"""""


#@scenario('../features/view_users.feature', 'Frontend admin users can get list of users')

#def test_scenario_browser():
#    pass

#@given('I am logged in as admin user') 
        
#@when('I visit the Users page') 

#@then('4 users are listed') 

#@And('1 of them is "Administrator" role') 