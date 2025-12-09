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

#REGEX olisi kiva, mutten saanut toimimaan. Vai onko muita tapoja tarkistaa oikea järjestys?