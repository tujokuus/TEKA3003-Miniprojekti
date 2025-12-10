*** Settings ***
Resource  resource.robot
Test Setup  Create Sources

*** Test Cases ***
Search Sources According To Title
    Search Source According To Field Command  title  Epäluotettava lähde
    Input Quit Command
    Run Application
    Output Should Contain  Löydettiin 2 lähdettä

Search Sources According To Year
    Search Source According To Field Command  year  2000
    Input Quit Command
    Run Application
    Output Should Contain  Löydettiin 1 lähdettä

Search Sources According To All Fields
    Input Search Sources Command
    Input Nothing
    Input  2000
    Input Quit Command
    Run Application
    Output Should Contain  Löydettiin 1 lähdettä

Search Sources According To All Fields With Multiple Hits
    Input Search Sources Command
    Input Nothing
    Input  20
    Input Quit Command
    Run Application
    Output Should Contain  Löydettiin 3 lähdettä

Search Nonexistant Sources
    Search Source According To Field Command  title  Eipä taida olla tämännimisiä
    Input Quit Command
    Run Application
    Output Should Contain  Annetulla hakusanalle 'Eipä taida olla tämännimisiä' ei löydetty yhtään lähdettä.

Search No Sources
    Delete Source According To Key  testiavain1
    Delete Source According To Key  testiavain2
    Delete Source According To Key  testiavain3
    Search Source According To Field Command  title  otsikko
    Input Quit Command
    Run Application
    Output Should Contain  Annetulla hakusanalle 'otsikko' ei löydetty yhtään lähdettä.