*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Add New Source Command
    Input Article  source_key=testiavain  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde

Add Source With New Type
    Input Add New Source Command
    Input  kissa
    Input  kissa-avain
    Input Nothing
    Input Yes Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde

Add Source With No Key
    Input Add New Source Command
    Input  article
    Input Nothing
    Input  avain
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty avain on tyhjä, lisää parempi

Add Source With No Author
    Input Add New Source Command
    Input  article
    Input  avain
    Input Nothing
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty author on tyhjä, lisää parempi

Add Source With Duplicate Key
    Input Add New Source Command
    Input Article  source_key=testiavain  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Add New Source Command
    Input  article
    Input  testiavain
    Input  avain
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty avain on jo olemassa, lisää parempi

Dont Add Anything Just Quit
    Input Quit Command
    Run Application
    Output Should Contain  Kiitoksia käytöstä

Give False Command
    Input  kissa
    Input Quit Command
    Run Application
    Output Should Contain  Antamaanne käskyä ei tunnistettu, antakaa se uudestaan
