*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Yes Command
    Input  y

Input No Command
    Input  n

Input Nothing
    Input  value=

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

Input Article
   [Arguments]  ${source_key}  ${source_author}  ${source_title}  ${source_journal}  ${source_year}
    Input  article
    Input  ${source_key}
    Input  ${source_author}
    Input  ${source_title}
    Input  ${source_journal}
    Input  ${source_year}
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Yes Command
