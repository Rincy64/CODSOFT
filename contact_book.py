contacts={}
def add_contact():
  name=input("Enter name:").strip()
  phone=input("Enter phone number:").strip()
  email=input("Enter email:").strip()
  address=input("Enter address:").strip()
  contacts[name.lower()]={
  'Name':name,
  'Phone':phone,
  'Email':email,
  'Address':address
  }
  print("Contact added successfully.\n")

def view_contacts():
  if not contacts:
    print("No contacts to display.\n")
  else:
    print("\n Contact List:")
    for contact in contacts.values():
      print(f"{contact['Name']{-{contact['Phone']}")
      print()

def search_contact():
  key= input("Enter name or phone number to search:").strip().lower()
  found=False
  for contact in contacts.values():
    if key in contact['Name'].lower() or key in contact['Phone']:
      print("\n Contact Found:")
      for k, v in contact.items():
        print(f"{k}:{v}")
        found = True
        break

    if not found:
      print("Contact not found.\n")

def update_contact():
  name=input("Enter the name of the contact to update:").strip().lower()
  if name in contacts:
    print("Enter new details (leave blank to keep unchanged):")
    contact = contacts[name]
    phone = input(f"New phone ({contact['Phone']}):") or contact['Phone']
    email = input(f"New email({contact['Email']}):") or contact['Email']
    address = input(f"New address({contact['Address']}):") or contact['Address']
    contacts[name]={
    'Name':contact['Name'],
    'Phone':phone,
    'Email':email,
    'Address':address
    }
    print("Contact updated successfully.\n")

  else:
    print("Contact not found.\n")

def delete_contact():
  name = input("Enter the name of the contact to delete:").strip()lower()
  if name in contacts:
    del contacts[name]
    print("Contact deleted successfully.\n")

  else:
    print("Contact not found.\n")

def main():
  while True:
    print("======Contact Book=======")
    print("1.Add Contact")
    print(2.View Contacts")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    choice= input("Enter your choice (1-6):").strip()
    if choice=='1':
      add_contact()
    elif choice=='2':
      view_contacts()
    elif choice=='3':
      search_contact()
    elif choice=='4':
      update_contact()
    elif choice=='5':
      delete_contact()
    elif choice=='6':
      print("Exiting Contact Book.Goodbye!")
      break
    else:
      print("!Invalid choice.Try again.\n")

if __name__ =="__main__":
  main()



    
