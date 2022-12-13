import pymysql.cursors

connection1 = pymysql.connect(host='localhost',
                             user='root',
                             password='WHATEVER')

connection2 = pymysql.connect(host='localhost', user='root', password='WHATEVER', db='library',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


def cursor():
    try:
        cursor = connection2.cursor(pymysql.cursors.DictCursor)
        return cursor
    except Exception as e:
        print(e)


while True:
    print("enter 1 to show all tables")
    print("enter 2 to select all from table")
    print("enter 3 to insert into table")
    print("enter 4 to update table")
    print("enter 5 to delete from table")
    print("enter 6 to enter JOIN to perform")
    print("0 - EXIT")
    cmd = input("Enter your command: ")
    table_prompt = "Enter your table: "
    #try:
    connection = cursor()
    if cmd == "1":
        connection.execute('show tables;')
        #connection.commit()
        print(connection.fetchall())
    elif cmd == "2":
        table = input(table_prompt)
        connection.execute(f'select * from {table} ;')
        print(connection.fetchall())
        #connection.commit()
    elif cmd == "3":
        table = input(table_prompt)
        if table == 'Category':
            category_id = input("Enter category_id: ")
            category_name = input("Enter category_name: ")
            connection.execute(
                f"""INSERT INTO `library`.`Category` (`category_id`, `category_name`) VALUES ({category_id}, '{category_name}');""")
            print(connection.fetchall())
            #connection.commit()
        elif table == 'Book':
            book_id = input("Enter book_id: ")
            title = input("Enter title: ")
            publish_year = input("Enter publish-year: ")
            category_id = input("Enter category_id: ")
            copies_owned = input("Enter copies_owned: ")
            connection.execute(f"""INSERT INTO `library`.`Book` (`book_id`, `title`, `publish-year`,"""
                                        f""" `category_id`, `copies_owned`) VALUES ({book_id}, '{title}',"""
                                        f""" {publish_year}, {category_id}, {copies_owned});""")
            print(connection.fetchall())
        elif table == 'Author':
            author_id = input("Enter author_id: ")
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            connection.execute(
                f"""INSERT INTO `library`.`Author` (`author_id`, `firstname`, `lastname`)"""
                f""" VALUES ({author_id}, '{firstname}', '{lastname}');""")
            print(connection.fetchall())
        elif table == 'Book_author':
            book_id = input("Enter book_id: ")
            author_id = input("Enter author_id: ")
            connection.cursor().execute(
                f"""INSERT INTO `library`.`Book_author` (`book_id`, `author_id`) VALUES ({book_id}, {author_id});""")
            connection.commit()
            print(connection.fetchall())
        elif table == 'Reader_status':
            Status_id = input("Enter Status_id: ")
            status_value = input("Enter status_value: ")
            connection.execute(
                f"""INSERT INTO `library`.`Reader_status` (`Status_id`, `status_value`) VALUES ({Status_id}, '{status_value}');""")
            print(connection.fetchall())
        elif table == 'Reader':
            reader_id = input("Enter reader_id: ")
            firstname = input("Enter firstname: ")
            lastname = input("Enter lastname: ")
            phone_number = input("Enter phone-number: ")
            active_status_id = input("Enter active_status_id: ")
            connection.execute(f"""INSERT INTO `library`.`Reader` """
                               f"""(`reader_id`, `firstname`, `lastname`, `phone-number`, `active_status_id`)"""
                               f"""VALUES ({reader_id}, '{firstname}', '{lastname}', '{phone_number}', {active_status_id});""")
            print(connection.fetchall())
        elif table == 'Current Loan':
            loan_id = input("Enter loan_id: ")
            reader_id = input("Enter reader_id: ")
            book_id = input("Enter book_id: ")
            loan_date = input("Enter loan-date: ")
            due_date = input("Enter due-date: ")
            returned_date = input("Enter returned-date: ")
            connection.execute(
                f"""INSERT INTO `library`.`Current Loan` (`loan_id`, `reader_id`, `book_id`, `loan-date`, `due-date`,"""
                f""" `returned-date`) VALUES ({loan_id}, {reader_id}, {book_id}, '{loan_date}', '{due_date}', '{returned_date}');""")
            print(connection.fetchall())
        elif table == 'Fine':
            #fine_id = input("Enter fine_id: ")
            #reader_id = input("Enter reader_id: ")
            #loan_id = input("Enter loan_id: ")
            reader = input("Enter reader's last name: ")
            reader_id1 = connection.execute(f'select reader_id from Reader where lastname = "{reader}";')
            list1 = connection.fetchall()
            reader_id = list1[0]['reader_id']
            loan_id1 = connection.execute(f'select loan_id from `library`.`Current Loan` where reader_id = {reader_id};')
            list2 = connection.fetchall()
            loan_id = list2[0]['loan_id']
            fine_date = input("Enter fine_date: ")
            fine_amount = input("Enter fine_amount: ")
            connection.execute(
                f"""INSERT INTO `library`.`Fine` (`reader_id`, `loan_id`, `fine_date`, `fine_amount`) """
                f"""VALUES ({reader_id}, {loan_id}, '{fine_date}', '{fine_amount}');""")
            connection1.commit()
            print(connection.fetchall())
        elif table == 'Fine_payment':
            id = input("Enter id: ")
            reader_id = input("Enter reader_id: ")
            payment_date = input("Enter payment_date: ")
            payment_amount = input("Enter payment_amount: ")
            connection.execute(
                f"""INSERT INTO `library`.`Fine_payment` (`id`, `reader_id`, `payment_date`, `payment_amount`)"""
                f""" VALUES ({id}, {reader_id}, '{payment_date}', '{payment_amount}');""")
            print(connection.fetchall())

    elif cmd == "4":
        table = input(table_prompt)
        column = input("Enter column you want to update: ")
        new_value = input("Enter new value: ")
        condition = input("Condition WHERE: ")
        connection.execute(f"""UPDATE `library`.`{table}` SET {column} = {new_value} WHERE {condition};""")
        print(connection.fetchall())

    elif cmd == "5":
        table = input(table_prompt)
        condition = input("Condition WHERE: ")
        connection.execute(f"""DELETE FROM `library`.`{table}` WHERE {condition};""")
        print(connection.fetchall())

    elif cmd == "6":
        join = input("Enter: ")
        connection.execute(f"""{join}""")
        print(connection.fetchall())

    elif cmd == "0":
        break
    else:
        print("You've chosen wrong option. Try again.")


connection.close()

"""
SELECT lastname, status_value FROM Reader JOIN Reader_status ON active_status_id = Status_id;

SELECT lastname, payment_amount FROM Reader JOIN Fine_payment ON Reader.reader_id = Fine_payment.reader_id GROUP BY payment_amount;
"""
