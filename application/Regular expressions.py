import csv
import re

def open_csv():

    ''' This function reads the csv document line by line and returns a list of lists'''

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return contacts_list


def format_number(contacts_list):

    ''' This function finds phone numbers and converts them by pattern '''

    number_pattern_raw = r'(\+7|8|7)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for card in contacts_list:
        card_as_string = ','.join(card)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated


def format_full_name(contacts_list):

    ''' The function separates first name, middle name and last name by columns '''

    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    c_list_updated = []
    for item in contacts_list:
        item_string = ','.join(item)
        formatted_item = re.sub(name_pattern_raw, name_pattern_new, item_string)
        item_list = formatted_item.split(',')
        c_list_updated.append(item_list)
    return c_list_updated


def join_duplicates(contacts_list):

    ''' The function formats the list and removes duplicates '''

    new_phonebook_list = []
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                elif i[3] == '':
                    i[3] = j[3]
                elif i[4] == '':
                    i[4] = j[4]
                elif i[5] == '':
                    i[5] = j[5]
                elif i[6] == '':
                    i[6] = j[6]

    for card in contacts_list:
        if card not in new_phonebook_list:
            new_phonebook_list.append(card)
    return new_phonebook_list


def write_file(new_phonebook_list):

    ''' The function writes the updated contact list to a csv file '''

    with open("phonebook_updated.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_phonebook_list)


def main():
    contacts_list = open_csv()
    contacts_list_updated = format_number(contacts_list)
    c_list_updated = format_full_name(contacts_list_updated)
    new_phonebook_list = join_duplicates(c_list_updated)
    write_file(new_phonebook_list)


if __name__ == '__main__':
    main()