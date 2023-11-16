*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jonne  kalle123
    Output Should Contain  User with username jonne already exists 

Register With Too Short Username And Valid Password
    Input Credentials  ka  kakaka123
    Output Should Contain  Username not valid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  VEIKKO  veikko123
    Output Should Contain  Username not valid

Register With Valid Username And Too Short Password
    Input Credentials  veikko  veiko1
    Output Should Contain  Password not valid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  veikko  veikkonen
    Output Should Contain  Password not valid

*** Keywords ***
Create User And Input New Command
    Create User  jonne  jonne123
    Input New Command