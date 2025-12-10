*** Settings ***
Resource  resource.robot
Test Setup  Create Sources

*** Test Cases ***
Sort Sources According To Author
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Lähteet järjestetty attribuutin 'author' mukaan:

Sort Sources According To Title
    Input Sort Sources According To Field Command  title
    Input Quit Command
    Run Application
    Output Should Contain  Lähteet järjestetty attribuutin 'title' mukaan:

Sort Sources According To Year
    Input Sort Sources According To Field Command  year
    Input Quit Command
    Run Application
    Output Should Contain  Lähteet järjestetty attribuutin 'year' mukaan:

Sort Sources According To Empty Value
    Input  c
    Input Nothing
    Input Quit Command
    Run Application
    Output Should Contain  Atribuutti ei voi olla tyhjä

Sort Sources According To Nonexistant Value
    Input  c
    Input  hakusana
    Input Quit Command
    Run Application
    Output Should Contain  Atribuuttia 'hakusana' ei löydy yhdeltäkään lähteeltä.

Sort No Sources
    Delete Source According To Key  testiavain1
    Delete Source According To Key  testiavain2
    Delete Source According To Key  testiavain3
    Input Sort Sources According To Field Command  year
    Input Quit Command
    Run Application
    Output Should Contain  Atribuuttia 'year' ei löydy yhdeltäkään lähteeltä.