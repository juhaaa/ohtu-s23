*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  jonne
    Set Password  kalle123
    Set Password-confirmation  kalle123
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password-confirmation  kalle123
    Submit Credentials
    Registering Should Fail With Message  Username not valid

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  salasana
    Set Password-confirmation  salasana
    Submit Credentials
    Registering Should Fail With Message  Password not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  veikko
    Set Password  kalle123
    Set Password-confirmation  kalle456
    Submit Credentials
    Registering Should Fail With Message  Passwords do not match

Login After Succesfull Registration
    Set Username  jonnez
    Set Password  kalle123
    Set Password-confirmation  kalle123
    Submit Credentials
    Registering Should Succeed
    Continue after registering
    Logout
    Login Page Should Be Open
    Set Username  jonne
    Set Password  kalle123
    Submit Login Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  failure
    Set Password  kalle123
    Set Password-confirmation  kalle456
    Submit Credentials
    Registering Should Fail With Message  Passwords do not match
    Continue To Login
    Set Username  failure
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password-confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Continue after registering
    Click Link  Continue to main page

Continue To Login
    Click Link  Login

Logout
    Click Button  Logout

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
    