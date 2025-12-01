*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Yes Command
    Input  y

Input No Command
    Input  n

Start Application
    Run Application

Input Source Credentials
   [Arguments]  ${source_key}  ${source_name}
    Input  ${source_key}
    Input  ${source_name}
    Input Yes Command
    Run Application
