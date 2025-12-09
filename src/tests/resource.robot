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

Input Add New Source By Doi Command
    Input  d

Input Add New Source By Acm.org Link Command
    Input  m

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

Input Source By Doi
    [Arguments]  ${source_doi}
    Input Add New Source By Doi Command
    Input  ${source_doi}

Input Source By Acm.org Link
    [Arguments]  ${source_link}
    Input Add New Source By Acm.org Link Command
    Input  ${source_link}

Input No Optionals
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Yes Command

Create Sources
    Input Add New Source Command
    Input Article  source_key=testiavain1  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Add New Source Command
    Input Article  source_key=testiavain2  source_author=Pertti Perttinen  source_title=Pertin kootut  source_journal=Epäluotettava lähde  source_year=2000
    Input Add New Source Command
    Input Article  source_key=testiavain3  source_author=Antti Anttinen  source_title=Kaikki parhaat lohkaisuni  source_journal=Legit lähde  source_year=200

Input Sort Sources According To Field Command
    [Arguments]  ${field}
    Input Sort Sources Command
    Input  ${field}
    Input Yes Command

