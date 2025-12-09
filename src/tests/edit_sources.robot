*** Settings ***
Resource  resource.robot
Test Setup  Create Sources

*** Test Cases ***

Edit Existing Source Successfully
    Input Edit Source Command
    Input  testiavain2
    Input  uusitestiavain
    Input  Matti Meikalainen
    Input  Uusi uljas muokattu otsikko
    Input  Nothing
    Input  -100

    Input Nothing

    Input Quit Command

    Run Application

    Output Should Contain  Tallennetaan uusi muokattu

Cancel Edit Without Saving
    Input Edit Source Command
    Input  testiavain3
    Input  Antti Anttinen
    Input  Muokattu otsikko jota ei tallenneta
    Input  Fake Journal
    Input  1999
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Nothing
    Input Quit Command
    Start Application
    Output Should Contain  testiavain3
    Output Should Contain  Kaikki parhaat lohkaisuni
    Output Should Contain  200

Delete Existing Source Successfully
    Input Edit Source Command
    Input  testiavain1

    Input  d
    Input Quit Command

    Start Application
    Output Should Contain  poistettu
    Output Should Contain  testiavain2
    Output Should Contain  testiavain3