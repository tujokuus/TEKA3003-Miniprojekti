*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Yes Command
    Input  y

Input No Command
    Input  n

Input Add New Source Command
    Input  a

Input Edit Source Command
    Input  b

Input Sort Sources Command
    Input  c

Input Quit Command
    Input  q

Start Application
    Run Application

Input Source Credentials
   [Arguments]  ${source_key}  ${source_name}
    Input  ${source_key}
    Input  ${source_name}
    Input Yes Command
