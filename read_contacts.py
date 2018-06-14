# Functions to read contacts from a given conntact file and return a
# list of names and email address


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            name.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

        return names, emails
