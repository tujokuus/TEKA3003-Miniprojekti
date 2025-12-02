*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Add New Source Command
    Input Article  source_key=testiavain  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde
