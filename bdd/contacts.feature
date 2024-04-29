Scenario: Add new contact
  Given a contact list
  Given a contact with {firstname}, {lastname}, {nickname}, {address}, {mobilephone}, {email}
  When I add the contact to the list
  Then the new contact list is equal to the old contact with the added contact

  Examples:
  | firstname | lastname | nickname | address | mobilephone | email |
  | firstname1 | lastname1 | nickname1 | Moscow | +7 911 911 1212 | email1@email1.tu |

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I set {firstname}, {lastname}, {nickname} for the contact
  Then the new contact list is equal to the old contact with the modified contact

  Examples:
  | firstname | lastname | nickname |
  | firstname2 | lastname2 | nickname2 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact