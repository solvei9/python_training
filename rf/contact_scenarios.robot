*** Settings ***
Library    rf.AddressBook
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=    Get Contact List
    ${contact}=    New Contact    firstname    lastname    nickname    Moscow    +79139201212    petrov@mail.ru
    Create Contact    ${contact}
    ${new_list}=    Get Contact List
    Append to list    ${old_list}    ${contact}
    Contact Lists Should Be Equal   ${old_list}    ${new_list}

Modify contact
    ${old_list}=    Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate    random.randrange(${len})    random
    ${old_contact}=    Get From List    ${old_list}    ${index}
    ${new_contact}=    New Contact    firstname1    lastname1    nickname1    StPetersburg    +79239224444    sidorov@mail.ru
    ${new_contact}=    Modify Contact    ${old_contact}    ${new_contact}
    ${new_list}=    Get Contact List
    Remove Values From List    ${old_list}    ${old_contact}
    Append to list    ${old_list}    ${new_contact}
    Contact Lists Should Be Equal   ${old_list}    ${new_list}

Delete contact
    ${old_list}=    Get Contact List
    ${len}=    Get Length    ${old_list}
    ${index}=    Evaluate    random.randrange(${len})    random
    ${contact}=    Get From List    ${old_list}    ${index}
    Delete Contact    ${contact}
    ${new_list}=    Get Contact List
    Remove Values From List    ${old_list}    ${contact}
    Contact Lists Should Be Equal   ${old_list}    ${new_list}
