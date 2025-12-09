*** Settings ***
Resource  resource.robot
Test Setup  Create Sources

*** Test Cases ***
List All Sources
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  testiavain1
    Output Should Contain  testiavain2
    Output Should Contain  testiavain3

List All Sources After Adding One
    Input Add New Source Command
    Input Article  source_key=jalkapallo  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input List Sources Command
    Input Quit Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan
    Output Should Contain  jalkapallo