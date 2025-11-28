*** Settings ***
Library  ../tests/test_console.py
Library  ../tests/test_bibtex.py

*** Keywords ***
Input Yes Command
    Input  y

Input No Command
    Input  n

Start Application
    Run Application

Input Surce Credentials
   [Arguments]  ${source_key}  ${source_name}
    Input  ${source_key}
    Input  ${source_name}
    Run Application
