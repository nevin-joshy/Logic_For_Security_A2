# Customers database: key = user_id
customers_db = {
    "Alice Smith": {
        "address": "123 Main St, Springfield, IL"
    },
    "Bob Johnson": {
        "address": "456 Maple Ave, Denver, CO"
    },
    "Charlie Davis": {
        "address": "789 Oak Blvd, Boston, MA"
    }
}

# Books database: key = book_id
books_db = {
    101: {
        "vendor_name": "BookWorld",
        "title": "The Art of Coding",
        "author": "Jane Doe",
        "year": 2020,
        "edition": "1st",
        "publisher": "TechBooks Publishing",
        "condition": "new",
        "description": "A comprehensive guide to modern software engineering.",
        "price": 39.99,
        "issold": False
    },
    102: {
        "vendor_name": "Readers Haven",
        "title": "Python for Beginners",
        "author": "John Smith",
        "year": 2018,
        "edition": "2nd",
        "publisher": "CodePress",
        "condition": "used",
        "description": "An easy-to-follow introduction to Python programming.",
        "price": 19.50,
        "issold": False

    },
    103: {
        "vendor_name": "BookWorld",
        "title": "Data Structures Unlocked",
        "author": "Maria Garcia",
        "year": 2022,
        "edition": "1st",
        "publisher": "LearnTech",
        "condition": "new",
        "description": "Mastering data structures through practical examples.",
        "price": 45.00,
        "issold": False
    }
}


def handle_new_book_offer(books_db, book_id, vendor_name, title, author, year, edition, publisher, condition, description, price):
    """
    Event handler for a new book offer uploaded by a vendor.

    QUESTIONS:
    Do I need to define returns like in the paper?
    Does the returned value need to be only owned by receiver i.e. vendor? (should success be {vendor, vendor} by the end - declassify it)
        In the if statement, success should be declassified, but then is it allowed to be there
    Do we need to do out the for loops and define the type and label of the iterator?
    Do we need to make a user interactive? or just these functions with the inputs?
    """

    # LABELS
    # book_id          : {vendor: vendor, system}
    # vendor_name      : {vendor: vendor, system}
    # title            : {vendor: vendor, system}
    # author           : {vendor: vendor, system}
    # year             : {vendor: vendor, system}
    # edition          : {vendor: vendor, system}
    # publisher        : {vendor: vendor, system}
    # condition        : {vendor: vendor, system}
    # description      : {vendor: vendor, system}
    # price            : {vendor: vendor, system}
    # issold           : {system: system}

    # success          : {system, vendor: system}

    # allowed write flow: {system, vendor: system}
    success = ""

    # allowed write flow: {system: system}
    issold = False

    # allowed read flow: {vendor: vendor, system}
    if not all([title, author, year, edition, publisher, condition, description, price]):
        #must declassify so vendor can read
        #DECLASSIFY(success, {vendor: vendor})
        #{vendor: vendor, system} U {vendor: vendor} = {vendor: vendor}
        return success

    # allowed read from system DB
    if vendor_name not in customers_db:
        #must declassify so vendor can read
        #DECLASSIFY(success, {vendor: vendor})
        #{vendor: vendor, system} U {vendor: vendor} = {vendor: vendor}
        return success
    
    # allowed read from system DB
    if book_id in books_db:
        #must declassify so vendor can read
        #DECLASSIFY(success, {vendor: vendor})
        #{vendor: vendor, system} U {vendor: vendor} = {vendor: vendor}
        return success 

    # All data fields owned by vendor, shared with system for storage
    # Information Flow: All below are secure as values are inserted into system-controlled DB
    books_db[book_id] = {
        "vendor_name": vendor_name,              # {vendor: vendor, system}
        "title": title,                          # {vendor: vendor, system}
        "author": author,                        # {vendor: vendor, system}
        "year": year,                            # {vendor: vendor, system}
        "edition": edition,                      # {vendor: vendor, system}
        "publisher": publisher,                  # {vendor: vendor, system}
        "condition": condition,                  # {vendor: vendor, system}
        "description": description,              # {vendor: vendor, system}
        "price": price,                          # {vendor: vendor, system}
        "issold": issold                         # {system: system}
    }

    #{system, vendor: system}
    success = f"Offer added successfully"

    #must declassify so vendor can read
    #DECLASSIFY(success, {vendor: vendor})
    return success

def handle_search_book(books_db, book_id, vendor_name, title, author, year, edition, publisher, condition, description, price):
    """
        Event handler for a user searching for a book.
    """

    # LABELS
    # book_id          : {vendor: vendor, system}
    # vendor_name      : {vendor: vendor, system}
    # title            : {vendor: vendor, system}
    # author           : {vendor: vendor, system}
    # year             : {vendor: vendor, system}
    # edition          : {vendor: vendor, system}
    # publisher        : {vendor: vendor, system}
    # condition        : {vendor: vendor, system}
    # description      : {vendor: vendor, system}
    # price            : {vendor: vendor, system}
    # issold           : {system: system}

    if book_id:
        pass
    
    if vendor_name:
        pass

    if title:
        pass

    if author:
        pass

    if year:
        pass

    if edition:
        pass

    if publisher:
        pass

    if condition:
        pass

    if description:
        pass

    if price:
        pass


