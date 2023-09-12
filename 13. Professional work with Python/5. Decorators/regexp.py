import csv
import re
from pprint import pprint
from decorators import logger

@logger(path='log_regexp.log')
def extract_names(full_name):
    match = re.search(r'(\w+)\s(\w+)\s?(\w+)?', full_name)
    if match:
        lastname = match.group(1)
        firstname = match.group(2)
        surname = match.group(3) if match.group(3) else ""
    else:
        lastname = ""
        firstname = ""
        surname = ""
    return lastname, firstname, surname

@logger(path='log_regexp.log')
def format_phone(phone):
    match = re.search(r'(\+7|8)?\s?\(?(\d{3})\)?\s?-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(.+доб.+(\d{4}))?', phone)
    if match:
        phone = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}'
        if match.group(7):
            phone += f' доб.{match.group(7)}'
    return phone

@logger(path='log_regexp.log')
def process_contact(contact):
    full_name = ' '.join(contact[:3])
    lastname, firstname, surname = extract_names(full_name)
    organization = contact[3] if len(contact) > 3 else ""
    position = contact[4] if len(contact) > 4 else "Не указана"
    phone = format_phone(contact[5]) if len(contact) > 5 else ""
    email = contact[6] if len(contact) > 6 else ""
    return lastname, firstname, surname, organization, position, phone, email

@logger(path='log_regexp.log')
def process_csv(input_filename, output_filename):
    with open(input_filename, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    processed_contacts_list = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]

    for contact in contacts_list[1:]:
        lastname, firstname, surname, organization, position, phone, email = process_contact(contact)

        is_copy = False
        for i, processed_contact in enumerate(processed_contacts_list):
            if processed_contact[0] == lastname and processed_contact[1] == firstname:
                is_copy = True
                if len(surname) > len(processed_contact[2]):
                    processed_contact[2] = surname
                if len(phone) > len(processed_contact[5]):
                    processed_contact[5] = phone
                if position != "Не указана":
                    processed_contact[4] = position

        if not is_copy:
            processed_contacts_list.append([lastname, firstname, surname, organization, position, phone, email])

    with open(output_filename, 'w', encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(processed_contacts_list)

    return processed_contacts_list

if __name__ == "__main__":
    input_filename = 'phonebook_raw.csv'
    output_filename = 'phonebook.csv'

    processed_contacts = process_csv(input_filename, output_filename)

    for contact in processed_contacts:
        contact_info = f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Организация: {contact[3]}, Должность: {contact[4]}, Телефон: {contact[5]}, Email: {contact[6]}"
        pprint(contact_info)