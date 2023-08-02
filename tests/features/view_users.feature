Feature: View Users
    As an admin user
    I want to access Users page
    So I can view a list of all users

    Scenario: API admin user can get list of users
        Given I am logged in as admin user
        When I request API GET api/v1/users
        Then I get HTTP "200" status code
        And I get JSON in response body
        And the HTTP response body contains a page with 4 users
        And 1 of them is "Administrator" role


    Scenario: Frontend admin users can get list of users
        Given I am logged in as admin user
        When I visit the Users page
        Then 4 users are listed
        And 1 of them is "Administrator" role