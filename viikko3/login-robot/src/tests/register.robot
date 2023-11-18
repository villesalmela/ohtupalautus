*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    seppo    seppo123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    kalle123
    Output Should Contain    Username already taken

Register With Too Short Username And Valid Password
    Input Credentials    kk    kalle123
    Output Should Contain    Bad username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    kalle123    kalle123
    Output Should Contain    Bad username

Register With Valid Username And Too Short Password
    Input Credentials    seppo    pp
    Output Should Contain    Bad password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    seppo    ppppppppp
    Output Should Contain    Bad password

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command