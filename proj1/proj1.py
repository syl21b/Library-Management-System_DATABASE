# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:01:27 2023

@author: sauvl
"""
from implement1 import Library

def main():
    library = Library('localhost', 'root', 'syl21b', 'proj1')
    with library:
        while True:
            print("Select an option:\n1 - Update member information\n2 - Update book information\n3 - Exit")
            option = input("Option: ")
            if option == '1':
                member_id = input("Enter the Member ID: ")
                library.update_member_info(member_id)
            elif option == '2':
                book_id = input("Enter the Book ID: ")
                library.update_book_info(book_id)
            elif option == '3':
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()

