*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Init

*** Test Cases ***
Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Register
    Register Should Fail With Message    Username too short

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Register
    Register Should Succeed

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation    kalle
    Submit Register
    Register Should Fail With Message    Password must contain letters and something else

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password    kalle123
    Set Password Confirmation    kalle124
    Submit Register
    Register Should Fail With Message    Passwords do not match

Login After Successful Registration
    Set Username  seppo
    Set Password  seppo123
    Set Password Confirmation    seppo123
    Submit Register
    Register Should Succeed
    Go To Login Page
    Set Username  seppo
    Set Password  seppo123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  juhani
    Set Password    juhani123
    Set Password Confirmation    juhani124
    Submit Register
    Register Should Fail With Message    Passwords do not match
    Go To Login Page
    Set Username    juhani
    Set Password    juhani123
    Submit Credentials
    Login Should Fail With Message    Invalid username or password



*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Register
    Click Button    Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Init
    Dummy
    Go To Register Page