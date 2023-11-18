*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Library  ../ChromeLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${BROWSER}    chrome

*** Keywords ***
Open And Configure Browser
    ${browser_options}    Get Chrome Options
    Open Browser  browser=${BROWSER}  options=${browser_options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Register Page Should Be Open
    Title Should Be  Register

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Welcome Page Should Be Open
    Title Should Be    Welcome to Ohtu Application!

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Register Page
    Go To    ${REGISTER_URL}

Go To Starting Page
    Go To    ${HOME_URL}
