*** Settings ***
Resource  resource.robot
Test Setup  Create Sources

*** Test Cases ***
List All Sources
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Kaikki lähteet:
    Output Should Contain  testiavain1
    Output Should Contain  testiavain2
    Output Should Contain  testiavain3

List All Sources After Adding One
    Input Add New Source Command
    Input Article  source_key=jalkapallo  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan
    Output Should Contain  Kaikki lähteet:
    Output Should Contain  testiavain1
    Output Should Contain  testiavain2
    Output Should Contain  testiavain3
    Output Should Contain  jalkapallo

List No Sources
    Delete Source According To Key  testiavain1
    Delete Source According To Key  testiavain2
    Delete Source According To Key  testiavain3
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Ei yhtään lähdettä

List All Sources After Deleting One
    Delete Source According To Key  testiavain1
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Kaikki lähteet:
    Output Should Contain  testiavain2
    Output Should Contain  testiavain3

List All Sources After Editing One
    Input Edit Source Command
    Input  testiavain2
    Input  uusitestiavain
    Input  Matti Meikalainen
    Input  Uusi uljas muokattu otsikko
    Input  Nothing
    Input  -100
    Input Nothing
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan uusi muokattu
    Output Should Contain  Kaikki lähteet:
    Output Should Contain  testiavain1
    Output Should Contain  uusitestiavain
    Output Should Contain  testiavain3

List All Sources After Deleting All And Adding One
    Delete Source According To Key  testiavain1
    Delete Source According To Key  testiavain2
    Delete Source According To Key  testiavain3
    Input Add New Source Command
    Input Article  source_key=jalkapallo  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input List Sources Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan
    Output Should Contain  Kaikki lähteet:
    Output Should Contain  jalkapallo