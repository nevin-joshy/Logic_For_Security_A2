# comments for CONFIDENTIALITY
""" comments for INTEGRITY """


# Customers database: key = user_id


customers_db = {
    "Alice Smith": {                                   #Integrity: """{market\: market}"""  Confidentiality:#{market: market}  
        "address": "123 Main St, Springfield, IL",     # """{market\: market}"""            #{market: market}
        "sell_data": True,                             # """{market\: market}"""            #{market: market}
        "searches": [101, 102],                        # """{market\: market, customer}"""  #{market: market}
        "purchases": [101]                             #"""{market\: market, customer}"""   #{market: market}
    },
    "Bob Johnson": { 
        "address": "456 Maple Ave, Denver, CO",
        "sell_data": True, 
        "searches": [101, 102],
        "purchases": []
    },
    "Charlie Davis": { 
        "address": "789 Oak Blvd, Boston, MA",
        "sell_data": False, 
        "searches": [101, 102], 
        "purchases": []
    }
}

sold_customers = {
    "Alice Smith": {                                   # Integrity: """{market\: market, customer}"""   Confidentiality: # {market: market, advertiser}
        "address": "123 Main St, Springfield, IL",     # """{market\: market, customer}"""              # {market: market, advertiser}
        "sell_data": True,                             # """{market\: market, customer}"""              # {market: market, advertiser}
        "searches": [101,102],                         # """{market\: market, customer}"""              # {market: market, advertiser}
        "purchases": [101]                             #"""{market\: market, customer}"""               # {market: market, advertiser}
    },
    "Bob Johnson": {
        "address": "456 Maple Ave, Denver, CO",
        "sell_data": True,
        "searches": [101,102],
        "purchases": []
    }
}

# Books database: key = book_id
books_db = {
    101: {                                                                        # Integrity: """{market\: market}""" Confidentiality: #{market: market}
        "vendor_name": "BookWorld",                                               # """{market\: market}"""         #{market: market}
        "title": "The Art of Coding",                                             # """{market\: market}"""         #{market: market}
        "author": "Jane Doe",                                                     # """{market\: market}"""         #{market: market}
        "year": 2020,                                                             # """{market\: market}"""         #{market: market}
        "edition": "1st",                                                         # """{market\: market}"""         #{market: market}
        "publisher": "TechBooks Publishing",                                      # """{market\: market}"""         #{market: market}
        "condition": "new",                                                       # """{market\: market}"""         #{market: market}
        "description": "A comprehensive guide to modern software engineering.",   # """{market\: market}"""         #{market: market}
        "price": 39.99,                                                           # """{market\: market}"""         #{market: market}
        "issold": False                                                           #"""{market\: market, customer}""" #{market: market}
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


def handle_new_book_offer(books_db, book_id, vendor_name, title, author, year, edition, publisher,
                          condition, description, price):
    """
    Event handler for a new book offer uploaded by a vendor.

    """

    # CONFIDENTIALITY LABELS
    # books_db         : as shown above
    # customers_db     : as shown above

    # book_id          : {vendor: vendor, market}
    # vendor_name      : {vendor: vendor, market}
    # title            : {vendor: vendor, market}
    # author           : {vendor: vendor, market}
    # year             : {vendor: vendor, market}
    # edition          : {vendor: vendor, market}
    # publisher        : {vendor: vendor, market}
    # condition        : {vendor: vendor, market}
    # description      : {vendor: vendor, market}
    # price            : {vendor: vendor, market}
    # issold           : {market: market}

    """
    INTEGRITY LABELS
    
    books_db         : as shown above
    customers_db     : as shown above

    book_id          : {all: vendor}
    vendor_name      : {all: vendor}
    title            : {all: vendor}
    author           : {all: vendor}
    year             : {all: vendor}
    edition          : {all: vendor}
    publisher        : {all: vendor}
    condition        : {all: vendor}
    description      : {all: vendor}
    price            : {all: vendor}
    
    issold           : {market: customer, market}
    """

    # if_acts_for(handle_new_book_offer, (market and vendor)):
    """ if_acts_for(handle_new_book_offer, (market)): """

    # DECLASSIFY all labels to be owned by market
    # CONFIDENTIALITY LABELS:

    # book_id -> m_book_id             : {vendor: vendor, market} -> {market:  market}
    # vendor_name -> m_vendor_name     : {vendor: vendor, market} -> {market:  market}
    # title -> m_title                 : {vendor: vendor, market} -> {market:  market}
    # author -> m_author               : {vendor: vendor, market} -> {market:  market}
    # year -> m_year                   : {vendor: vendor, market} -> {market:  market}
    # edition -> m_edition             : {vendor: vendor, market} -> {market:  market}
    # publisher -> m_publisher         : {vendor: vendor, market} -> {market:  market}
    # condition -> m_condition         : {vendor: vendor, market} -> {market:  market}
    # description -> m_description     : {vendor: vendor, market} -> {market:  market}
    # price -> m_price                 : {vendor: vendor, market} -> {market:  market}

    # PROOF
    # {market: market} U {market: {}; vendor: {}} = {market: {}; vendor: {}}
    # {vendor: vendor, market} C {market: {}; vendor: {}}

    """
    #Use allowed flow to change all labels

        book_id -> m_book_id             : {all: vendor} -> {market: market, vendor}
        vendor_name -> m_vendor_name     : {all: vendor} -> {market: market, vendor}
        title -> m_title                 : {all: vendor} -> {market: market, vendor}
        author -> m_author               : {all: vendor} -> {market: market, vendor}
        year -> m_year                   : {all: vendor} -> {market: market, vendor}
        edition -> m_edition             : {all: vendor} -> {market: market, vendor}
        publisher -> m_publisher         : {all: vendor} -> {market: market, vendor}
        condition -> m_condition         : {all: vendor} -> {market: market, vendor}
        description -> m_description     : {all: vendor} -> {market: market, vendor}
        price -> m_price                 : {all: vendor} -> {market: market, vendor}

        PROOF:
        {all: vendor} C {market: market, vendor}
    """

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # {market: market, vendor}
    """{market: market}"""
    success = ""

    # {market : market}
    """{market: market, vendor}"""
    flag = False

    # {market: market}
    """{market: customer, market}"""
    issold = False

    if not all([m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price]):
        # Flowing from m_variable block {market:market} to flag {market:market}
        # {market: market} C {market: market}
        """Flowing from m_variable block {market:market, vendor} to flag {market:market, vendor}"""
        """{market: market, vendor} C {market: market, vendor}"""
        flag = True

    # allowed read from market DB
    if m_book_id in books_db:
        # Block label: {market: market}(m_book_id) U {market: market}(books_db[id])
        # {market: market}(block) C {market: market}(flag)
        """Block label: {market: market, vendor}(m_book_id) U {market: market}(books_db[id])"""
        """{market: market, vendor} C {market: market, vendor}"""
        flag = True

    # if_acts_for(handle_new_book_offer, (market)):
    # DECLASSIFY
    # flag -> v_flag  {market: market} -> {market: market, vendor}
    # PROOF
    # {market: market, vendor}(dest label) U {market: {}}(authority) = {market: {}}
    # {market: market} C {market: {}}

    v_flag = flag

    if v_flag:
        # allowed flow - both are {market: market, vendor}
        return success

    """
    #ENDORSE to remove vendor from writers

        book_id -> m_book_id             : {market: market, vendor} -> {market: market}
        vendor_name -> m_vendor_name     : {market: market, vendor} -> {market: market}
        title -> m_title                 : {market: market, vendor} -> {market: market}
        author -> m_author               : {market: market, vendor} -> {market: market}
        year -> m_year                   : {market: market, vendor} -> {market: market}
        edition -> m_edition             : {market: market, vendor} -> {market: market}
        publisher -> m_publisher         : {market: market, vendor} -> {market: market}
        condition -> m_condition         : {market: market, vendor} -> {market: market}
        description -> m_description     : {market: market, vendor} -> {market: market}
        price -> m_price                 : {market: market, vendor} -> {market: market}

        PROOF:
        {market: market, vendor} int {market: {}} = {market: {}}
        {market:{}} C {market: market}

    """

    # All data fields owned by vendor, shared with market for storage
    # Information Flow: All below are secure as values are inserted into market-controlled DB
    books_db[book_id] = {
        "vendor_name": m_vendor_name,           #     """{market/: market}""" # {market: market}
        "title": m_title,                       #     """{market/: market}""" # {market: market}
        "author": m_author,                      #    """{market/: market}""" # {market: market}
        "year": m_year,                           #   """{market/: market}""" # {market: market}
        "edition": m_edition,                    #    """{market/: market}""" # {market: market}
        "publisher": m_publisher,                #    """{market/: market}""" # {market: market}
        "condition": m_condition,                #    """{market/: market}""" # {market: market}
        "description": m_description,            #    """{market/: market}""" # {market: market}
        "price": m_price,                         #   """{market/: market}""" # {market: market}
        "issold": issold                         # """{market/: customer, market}""" # {market: market}
    }

    # {market: market, vendor}
    """{market: market}"""
    success = f"Offer added successfully"

    return success


def handle_search_book(
        books_db=None,
        customers_db=None,
        sold_customers=None,
        book_id=None,
        user_name=None,
        vendor_name=None,
        title=None,
        author=None,
        year=None,
        edition=None,
        publisher=None,
        condition=None,
        description=None,
        price=None
):
    """
        Event handler for a customer searching for a book.
    """

    # LABELS

    # books_db         : see label at top of file
    # customers_db     : see label at top of file
    # sold_customers   : see label at top of file

    # user_name        : {customer: customer, market}
    # book_id          : {customer: customer, market}
    # vendor_name      : {customer: customer, market}
    # title            : {customer: customer, market}
    # author           : {customer: customer, market}
    # year             : {customer: customer, market}
    # edition          : {customer: customer, market}
    # publisher        : {customer: customer, market}
    # condition        : {customer: customer, market}
    # description      : {customer: customer, market}
    # price            : {customer: customer, market}

    """
    INTEGRITY LABELS
    
    books_db         : see label at top of file
    customers_db     : see label at top of file
    sold_customers   : see label at top of file

    user_name        : {all: customer}
    book_id          : {all: customer}
    vendor_name      : {all: customer}
    title            : {all: customer}
    author           : {all: customer}
    year             : {all: customer}
    edition          : {all: customer}
    publisher        : {all: customer}
    condition        : {all: customer}
    description      : {all: customer}
    price            : {all: customer}
    
    """

    # if_acts_for(handle_search_book, (market and customer)):

    # DECLASSIFY all labels to be owned by market
    # book_id -> m_book_id             : {customer: customer, market} -> {market: customer, market}
    # user_name -> user_name           : {customer: customer, market} -> {market: customer, market}
    # vendor_name -> m_vendor_name     : {customer: customer, market} -> {market: customer, market}
    # title -> m_title                 : {customer: customer, market} -> {market: customer, market}
    # author -> m_author               : {customer: customer, market} -> {market: customer, market}
    # year -> m_year                   : {customer: customer, market} -> {market: customer, market}
    # edition -> m_edition             : {customer: customer, market} -> {market: customer, market}
    # publisher -> m_publisher         : {customer: customer, market} -> {market: customer, market}
    # condition -> m_condition         : {customer: customer, market} -> {market: customer, market}
    # description -> m_description     : {customer: customer, market} -> {market: customer, market}
    # price -> m_price                 : {customer: customer, market} -> {market: customer, market}
    # PROOF:
    # {market: market, customer} U {market: {}; customer: {}} = {market: {}; customer: {}}
    # {customer: customer, market} C {market: {}; customer: {}}

    """
    #Use allowed flow to change all labels

        book_id -> m_book_id             : {all: customer} -> {market: market, customer}
        user_name -> user_name           : {all: customer} -> {market: market, customer}
        vendor_name -> m_vendor_name     : {all: customer} -> {market: market, customer}
        title -> m_title                 : {all: customer} -> {market: market, customer}
        author -> m_author               : {all: customer} -> {market: market, customer}
        year -> m_year                   : {all: customer} -> {market: market, customer}
        edition -> m_edition             : {all: customer} -> {market: market, customer}
        publisher -> m_publisher         : {all: customer} -> {market: market, customer}
        condition -> m_condition         : {all: customer} -> {market: market, customer}
        description -> m_description     : {all: customer} -> {market: market, customer}
        price -> m_price                 : {all: customer} -> {market: market, customer}

        PROOF:
        {all: customer} C {market: market, customer}
    """

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # {market: market}
    """{market: market, customer}"""
    matches = {}
    for id, data in books_db.items():
        # All variables have label {market: market}, so allowed flow
        '''{market: market}(block-books_db) C {market: market, customer}(matches)'''
        matches[id] = data
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches_copy = matches.copy()

    if m_book_id:
        for (id, data) in matches.items():
            if m_book_id != id:
                # Block Label: {market: customer, market}(m_book_id) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_book_id) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_vendor_name:
        for (id, data) in matches.items():
            if m_vendor_name.lower() not in data['vendor_name'].lower():
                # Block Label: {market: customer, market}(m_vendor_name) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_vendor_name) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_title:
        for (id, data) in matches.items():
            print(data)
            if m_title.lower() not in data['title'].lower():
                # Block Label: {market: customer, market}(m_title) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_title) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_author:
        for (id, data) in matches.items():
            if m_author.lower() not in data['author'].lower():
                # Block Label: {market: customer, market}(m_author) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_author) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_year:
        for (id, data) in matches.items():
            if m_year != data['year']:
                # Block Label: {market: customer, market}(m_year) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_year) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_edition:
        for (id, data) in matches.items():
            if m_edition != data['edition']:
                # Block Label: {market: customer, market}(m_edition) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_edition) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_publisher:
        for (id, data) in matches.items():
            if m_publisher.lower() not in data['publisher'].lower():
                # Block Label: {market: customer, market}(m_publisher) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_publisher) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_condition:
        for (id, data) in matches.items():
            if m_condition.lower() != data['condition'].lower():
                # Block Label: {market: customer, market}(m_condition) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_condition) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_description:
        for (id, data) in matches.items():
            if m_description.lower() not in data['description'].lower():
                # Block Label: {market: customer, market}(m_description) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_description) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    if m_price:
        for (id, data) in matches.items():
            if m_price != data['price']:
                # Block Label: {market: customer, market}(m_price) U {market: market}(matches) = {market: market}
                # Allowed flow: {market: market}(block) C {market: market}(matches_copy)
                """Block Label: {market: market, customer}(m_price) U {market: market, customer}(matches) = {market: market, customer}"""
                """{market: market, customer}(block) C {market: market, customer}(matches_copy)"""
                matches_copy.pop(id, None)
    # Flow back into same label {market: market}
    """ Flow back into same label {market: market, customer}"""
    matches = matches_copy.copy()

    # SELLING DATA

    # {market:market}
    """ {market: market, customer} """
    user_exists = False
    if user_name in customers_db:
        # Block Label: {market: market, customer}(user_name) U {market: market}(customers_db[name]) = {market: market}
        # {market: market}(block) C {market: market}(user_exists)
        """Block Label: {market: market, customer}(user_name) U {market: market}(customers_db[name]) = {market: market, customer}"""
        """{market: market, customer}(block) C {market: market, customer}(user_exists)"""
        user_exists = True

    # {market: market}
    """ {market: market, customer} """
    sell_data = False
    if user_exists:
        if customers_db[user_name]["sell_data"]:
            #Block Label: {market: market}(user_exists) U {market: market}(customers_db[user_name]["sell_data"]) = {market: market}
            # {market: market}(block) C {market: market}(sell_data)
            """Block Label: {market: market, customer}(user_exists) U {market: market}(customers_db[user_name]["sell_data"]) = {market: market, customer}"""
            """ {market: market, customer}(block) C {market: market, customer}(sell_data)""" 
            sell_data = True

    # if_acts_for(handle_search_book, (market)):
    #DECLASSIFY
        # sell_data            : {market: market} -> {market: market, adveritser}
        # user_exists          : {market: market} -> {market: market, adveritser}
        # PROOF
        # {market: market, advertiser} U {market: {}} = {market: {}}
        # {market: market} C {market: {}}
        
    if user_exists:
        #Block Label: {market: market}(user_exists)
        # e U B = {market: market}(matches) U {market: market}(block) = {market: market}
        # {market: market}(e U B) C {market: market}(customers_db[user_name]["searches"])
        """Block Label: {market: market, customer}(user_exists)"""
        """e U B = {market: customer, market}(matches) U {market: customer, market}(block) = {market: customer, market}"""
        """{market: customer, market}(e U B) C {market: customer, market}(customers_db[user_name]["searches"])"""
        customers_db[user_name]["searches"].extend(matches.keys())
        if sell_data:
            # if_acts_for(handle_search_book, (market)):
            #DECLASSIFY
                # customers_db[user_name] -> temp        : {market: market}(all data for a user is {market:market}) -> {market: market, adveritser}
                # PROOF
                # {market: market, advertiser} U {market: {}} = {market: {}}
                # {market: market} C {market: {}}
            """e U B = {market: market}(customers_db[user_name]) U {market: customer, market}(block) = {market: customer, market}"""
            """{market: customer, market}(e U B) C {market: customer, market}(sold_customers[user_name])"""
            # e U B = {{market: market, adveritser}}(customers_db[user_name]) U {market: market, advertiser}(block/sell_data and user_exists) = {market: market, adveritser}
            # {market: market, adveritser}(e U B) C {market: market, adveritser}(sold_customers[user_name])
            temp = customers_db[user_name].copy()
            sold_customers[user_name] = temp


    # if_acts_for(handle_search_book, (market)):
    # DECLASSIFY
    # matches -> p_matches            : {market: market} -> {market: customer, market}
    # PROOF
    # {market: market, customer}(target) U {market: {}}(authority) = {market: {}}
    # {market: market}(start) C {market: {}}

    """ Already {market: market, customer}, sufficient for return to customer """

    p_matches = matches.copy()

    return p_matches


def handle_purchase_book(books_db, customers_db, sold_customers, book_id, price, name):
    # LABELS

    # books_db         : labels at top of file
    # customers_db     : labels at top of file
    # sold_customers   : labels at top of file
    # book_id          : {customer: customer, market}
    # price            : {customer: customer, market}
    # name             : {customer: customer, market}

    """
    INTEGRITY LABELS
    
    books_db         : labels at top of file
    customers_db     : labels at top of file
    sold_customers   : labels at top of file
    book_id          : {all: customer, market}
    price            : {all: customer, market}
    name             : {all: customer, market}
    """

    # if_acts_for(handle_purchase_book, (market and customer)):

    # DECLASSIFY labels to be owned by market
    # book_id -> m_book_id             : {customer: customer, market} -> {market: customer, market}
    # price -> m_price                 : {customer: customer, market} -> {market: customer, market}
    # name -> m_name                   : {customer: customer, market} -> {market: customer, market}
    # PROOF:
    # {market: market, customer} U {market: {}; customer: {}} = {market: {}; customer: {}}
    # {customer: customer, market} C {market: {}; customer: {}}

    """
     #Use allowed flow to change all labels
        book_id -> m_book_id             : {all: customer} -> {market: customer, market}
        price -> m_price                 : {all: customer} -> {market: customer, market}
        name -> m_name                   : {all: customer} -> {market: customer, market}
    """

    m_book_id, m_price, m_name = book_id, price, name

    # {market: market, customer}
    """ {market: customer, market} """
    ret = ""

    # {market: market}
    """ {market: customer, market} """
    match = None

    for id, data in books_db.items():
        if m_book_id == id and data['issold'] == False and m_price == data['price']:
            # Block Label: {market: market}(books_db items) U {market: market, customer}(m_book_id, m_price) = {market: market}
            # e U B = {market: market}(id,data) U {market: market}(block) = {market: market}
            # {market: market}(e U B) C {market: market}(match)
            """
            Block Label: {market: market}(books_db items) U {market: market, customer}(m_book_id, m_price) = {market: customer, market}
            e U B = {market: market}(id,data) U {market: customer, market}(block) = {market: customer, market}
            {market: customer, market}(e U B) C {market: customer, market}(match)
            """
            match = (id, data)
            break

    # if_acts_for(handle_purchase_book, (market)):
    # DECLASSIFY match to be read by customer
    # match -> c_match      : {market: market} -> {market: customer, market}
    # PROOF:
    # {market: customer, market} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}

    """ Already {market: customer, market}, sufficient for return to customer """

    c_match = match

    if c_match is None:
        # Block Label: {market: customer, market}(c_match)
        # {market: customer, market}(block) C {market: market, customer}(ret/output)
        """ Block Label: {market: customer, market}(c_match)"""
        """{market: customer, market}(block) C {market: market, customer}(ret/output)"""
        ret = "Error purchasing book"
        return ret

    # {market: market}
    """ {market: customer, market} """
    m_vendor_name = match[1]['vendor_name']

    # {market: market}
    """ {market: customer, market} """
    m_cust_address = None

    # {market: market}
    """ {market: customer, market} """
    user_exists = False

    for user_name, data in customers_db.items():
        if m_name == user_name:
            # Block Label: {market: market}(user_name, data) U {market: customer, market}(m_name) = {market: market}
            # e U B = {market: market}(data["address"]) U {market: market}(block) = {market: market} 
            # {market: market}(e U B) C {market: market}(m_cust_address) - also applies for user_exists because it is {market: market}!!
            """ Allowed flow {market: market} U {market: customer, market} = {market: customer, market}
                e U B = {market: market} U {market: customer, market} = {market: customer, market} 
                {market: customer, market}  C {market: customer, market} """
            m_cust_address = data["address"]
            user_exists = True

    # if_acts_for(handle_purchase_book, (market)):
    # DECLASSIFY return variables to be read by customer, vendor
    # user_exists -> cv_user_exists          : {market: market} -> {market: customer, vendor, market}
    # m_cust_address -> cv_cust_address      : {market: market} -> {market: customer, vendor, market}
    # m_vendor_name -> cv_vendor_name        : {market: market} -> {market: customer, vendor, market}
    # PROOF:
    # {market: customer, vendor, market} U { market: {}} = {market: {}}
    # {market: market} C {market: {}}

    # if_acts_for(handle_purchase_book, (market)):
    # DECLASSIFY return variables to be read by customer, vendor
    # ret -> cv_ret                          : {market: customer, market} -> {market: customer, vendor, market}
    # m_book_id -> cv_book_id                : {market: customer, market} -> {market: customer, vendor, market}
    # m_name -> cv_name                      : {market: customer, market} -> {market: customer, vendor, market}
    # PROOF:
    # {market: customer, vendor, market} U {market: {}} = {market: {}}
    # {market: customer, market} C {market: {}}

    """Same label flow into {market: market, customer}"""
    cv_cust_address = m_cust_address
    """Same label flow into {market: market, customer}"""
    cv_vendor_name = m_vendor_name
    """Same label flow into {market: market, customer}"""
    cv_user_exists = user_exists
    """Same label flow into {market: market, customer}"""
    cv_ret = ret
    """Same label flow into {market: market, customer}"""
    cv_book_id = m_book_id
    """Same label flow into {market: market, customer}"""
    cv_name = m_name

    if cv_user_exists:
        # Block Label: {market: customer, vendor, market}(cv_user_exists)
        # e U B = {market: customer, vendor, market}(cv_book_id, cv_vendor_name, cv_name, cv_cust_address) U {market: customer, vendor, market}(block)
        # = {market: customer, vendor, market}
        # {market: customer, vendor, market}(e U B) C {market: customer, vendor, market}(cv_ret)
        """ Block Label: {market: customer, market}(cv_user_exists)"""
        """e U B = {market: customer, market}(cv_book_id, cv_vendor_name, cv_name, cv_cust_address) U {market: customer, market}(block)"""
        """ = {market: customer, market}"""
        """{market: customer, market}(e U B) C {market: customer, market}(cv_ret)"""
        cv_ret = f"Book: {cv_book_id} sold by {cv_vendor_name} to {cv_name} at {cv_cust_address}"

        # {market: customer, vendor, market}(block) C {market: market}(books_db[cv_book_id]["issold"])
        """ {market: customer, market}(block) C {market: customer, market}(books_db[cv_book_id]["issold"])"""
        books_db[cv_book_id]["issold"] = True

        # {market: customer, vendor, market}(block) C {market: market}(customers_db[m_name]["purchases"])
        """ {market: customer, market}(block) C {market: customer, market}(books_db[cv_book_id]["issold"])"""
        customers_db[m_name]["purchases"].append(cv_book_id)

    if not cv_user_exists:
        # Block Label: {market: customer, vendor, market}(cv_user_exists)
        # {market: customer, vendor, market}(block) C {market: customer, vendor, market}(cv_ret)
        """ {market: customer, market}(block) C {market: customer, market}(cv_ret)"""
        cv_ret = "User does not exist"
        return cv_ret

    # {market: market}
    """{market: customer, market}"""
    sell_data = False
    if customers_db[m_name]["sell_data"]:
        #Block label: {market: market}(customers_db[m_name]["sell_data"])
        # {market: market}(block) C {market: market}(sell_data)
        """{market: customer, market}(block/customers_db[m_name]["sell_data"]) C {market: customer, market}(sell_data)"""
        sell_data = True

    # if_acts_for(handle_search_book, (market)):
        #DECLASSIFY
            # sell_data            : {market: market} -> {market: market, adveritser}
            # PROOF
            # {market: market, advertiser} U {market: {}} = {market: {}}
            # {market: market} C {market: {}}
    if sell_data:
        # if_acts_for(handle_search_book, (market)):
        #DECLASSIFY
            # customers_db[user_name] -> temp            : {market: market}(all data for a user is {market:market}) -> {market: market, adveritser}
            # PROOF
            # {market: market, advertiser} U {market: {}} = {market: {}}
            # {market: market} C {market: {}}
        """{market: market}(sell_data) C {market: customer, market}(sold_customers[user_name])"""
        # e U B = {{market: market, adveritser}}(customers_db[user_name]) U {market: market, advertiser}(block/sell_data) = {market: market, adveritser}
        # {market: market, adveritser}(e U B) C {market: market, adveritser}(sold_customers[user_name])
        temp = customers_db[user_name].copy()
        sold_customers[user_name] = temp

    return cv_ret
