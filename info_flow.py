# comments for CONFIDENTIALITY
""" comments for INTEGRITY """

'''
Why so much declassifying
what do security goals mean for cofidentiality and integrity, and info flow analysis
Is it bad that our customers_db has differnt labels conditionally?

Assumed strength - we usually assume customers is {market: market}. if it is {market: market, advertiser}, then flow in will be an issue
because it was weak -> strong and strong got weaker, if it gets <weak then flow is not allowed. Rn we dont flow into customers unless selling
data which I think is okay, but we need to start adding to customers_db the searches even if they dont sell the data, unless we dont?
adding to customers
Change header definition of db labels - both cases for books_db and for integrity, change search and purchase to always be {market: market, customer}
'''

# Customers database: key = user_id
customers_db = {
    "Alice Smith": {
        "address": "123 Main St, Springfield, IL",
        "sell_data": True,
        "searches": [101, 102],
        "purchases": [101]
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


def handle_new_book_offer(books_db, customers_db, book_id, vendor_name, title, author, year, edition, publisher,
                          condition, description, price):
    """
    Event handler for a new book offer uploaded by a vendor.

    """

    # CONFIDENTIALITY LABELS
    # books_db         : {market: market}
    # customers_db     : {market: market}

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
    
    books_db         : {market: market}
    customers_db     : {market: market}

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

    # allowed read flow: {market: market}
    """{market: market}"""
    success = ""

    # {market : market}
    """{market: market, vendor}"""
    flag = False

    # allowed read flow: {market: market}
    """{market: customer, market}"""
    issold = False

    # allowed read flow: {vendor: vendor, market}
    """{market:  market, vendor}"""
    if not all([m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price]):
        # Allowed flow: {market: market} C {market: market}
        """{market: market, vendor} C {market: market, vendor}"""
        success = "Book data incomplete"
        flag = True

    # allowed read from market DB
    if m_vendor_name not in customers_db:
        # Allowed flow: {market: market} C {market: market}
        """{market: market} C {market: market, vendor}"""
        success = "Vendor does not exist"
        flag = True

    # allowed read from market DB
    if m_book_id in books_db:
        # Allowed flow: {market: market} C {market: market}
        """{market: market} C {market: market, vendor}"""
        success = "Book already exists"
        flag = True

    # DECLASSIFY
    # flag -> v_flag  {market: market} -> {market: market, vendor}
    # PROOF
    # {market: market, vendor} U {market: {}; vendor: {}} = {market: {}; vendor: {}}
    # {market: market} C {market: {}; vendor: {}}

    v_flag = flag

    if v_flag:
        # allowed flow {market: market, vendor}
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

    # {market: market}
    """{all/: market}"""
    success = f"Offer added successfully"

    # must declassify so vendor can read
    # DECLASSIFY(success, {vendor: vendor})
    # success -> success          {market: market} -> {market: market, vendor}

    # PROOF:
    # {market: market, vendor} U {market: {}; vendor: {}} = {market: {}; vendor: {}}
    # {market: market} C {market: {}; vendor: {}}

    """
    Allowed Flow
        success -> success          {market: market} -> {market: vendor, market}  

        PROOF:
        {market: market} C {market: vendor, market} 
    """

    return success


def handle_search_book(
        books_db=None,
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
        Event handler for a user searching for a book.
    """

    # LABELS

    # books_db         : {market: market}

    # user_name        : {user: user, market}
    # book_id          : {user: user, market}
    # vendor_name      : {user: user, market}
    # title            : {user: user, market}
    # author           : {user: user, market}
    # year             : {user: user, market}
    # edition          : {user: user, market}
    # publisher        : {user: user, market}
    # condition        : {user: user, market}
    # description      : {user: user, market}
    # price            : {user: user, market}

    """
    INTEGRITY LABELS
    
    books_db         : {market: market}
    customers_db     : {market: market}

    user_name        : {all: user}
    book_id          : {all: user}
    vendor_name      : {all: user}
    title            : {all: user}
    author           : {all: user}
    year             : {all: user}
    edition          : {all: user}
    publisher        : {all: user}
    condition        : {all: user}
    description      : {all: user}
    price            : {all: user}
    
    """

    # if_acts_for(handle_search_book, (market and user)):
    """ if_acts_for(handle_search_book, none): """

    # DECLASSIFY all labels to be owned by market
    # book_id -> m_book_id             : {user: user, market} -> {market: user, market}
    # user_name -> user_name           : {user: user, market} -> {market: user, market}
    # vendor_name -> m_vendor_name     : {user: user, market} -> {market: user, market}
    # title -> m_title                 : {user: user, market} -> {market: user, market}
    # author -> m_author               : {user: user, market} -> {market: user, market}
    # year -> m_year                   : {user: user, market} -> {market: user, market}
    # edition -> m_edition             : {user: user, market} -> {market: user, market}
    # publisher -> m_publisher         : {user: user, market} -> {market: user, market}
    # condition -> m_condition         : {user: user, market} -> {market: user, market}
    # description -> m_description     : {user: user, market} -> {market: user, market}
    # price -> m_price                 : {user: user, market} -> {market: user, market}
    # PROOF:
    # {market: market, user} U {market: {}; user: {}} = {market: {}; user: {}}
    # {user: user, market} C {market: {}; user: {}}

    """
    #Use allowed flow to change all labels

        book_id -> m_book_id             : {all: user} -> {market: market, user}
        user_name -> user_name           : {all: user} -> {market: market, user}
        vendor_name -> m_vendor_name     : {all: user} -> {market: market, user}
        title -> m_title                 : {all: user} -> {market: market, user}
        author -> m_author               : {all: user} -> {market: market, user}
        year -> m_year                   : {all: user} -> {market: market, user}
        edition -> m_edition             : {all: user} -> {market: market, user}
        publisher -> m_publisher         : {all: user} -> {market: market, user}
        condition -> m_condition         : {all: user} -> {market: market, user}
        description -> m_description     : {all: user} -> {market: market, user}
        price -> m_price                 : {all: user} -> {market: market, user}

        PROOF:
        {all: user} C {market: market, user}
    """

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # {market: market}
    """{market: market, user}"""
    matches = {}
    for id, data in books_db.items():
        '''{market: market} C {market: market, user}'''
        matches[id] = data
    # {market: market}
    """{market: market, user}"""
    matches_copy = matches.copy()

    if m_book_id:
        for (id, data) in matches.items():
            if m_book_id != id:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_vendor_name:
        for (id, data) in matches.items():
            if m_vendor_name.lower() not in data['vendor_name'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_title:
        for (id, data) in matches.items():
            if m_title.lower() not in data['title'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_author:
        for (id, data) in matches.items():
            if m_author.lower() not in data['author'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_year:
        for (id, data) in matches.items():
            if m_year != data['year']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_edition:
        for (id, data) in matches.items():
            if m_year != data['year']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_publisher:
        for (id, data) in matches.items():
            if m_publisher.lower() not in data['publisher'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_condition:
        for (id, data) in matches.items():
            if m_condition.lower() != data['condition'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches_copy.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_description:
        for (id, data) in matches.items():
            if m_description.lower() not in data['description'].lower():
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                # matches.remove((id, data))
                matches_copy.pop(id, None)
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    if m_price:
        for (id, data) in matches.items():
            if m_price != data['price']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{market: market, user} U {market: market, user} = {market: market, user}"""
                """{market: market, user} C {market: market, user}"""
                matches_copy.pop(id, None)
                # matches.remove((id, data))
    # {market: market}
    """{market: market, user}"""
    matches = matches_copy.copy()

    # SELLING DATA
    # if_acts_for(handle_search_book, (market)):

    # {market:market}
    """-----------------------hwo to determine the block label when user_name is different than customers_db--------------------------"""
    """ {market: market, user} """
    user_exists = False
    if user_name in customers_db:
        """{market: market, user} C {market: market, user}"""
        user_exists = True
    # DECLASSIFY
    # user_exists -> a_user_exists    : {market: market} -> {market: user, market, advertiser}
    # PROOF
    # {market: market, user, advertiser} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}
    """ {market: market, user} """
    a_user_exists = user_exists

    # {market: market}
    """ {market: market, user} """
    sell_data = False
    if user_exists:
        if customers_db[user_name]["sell_data"]:
            """ {market: market, user} U {market: market} = {market: market, user}"""
            sell_data = True

    # DECLASSIFY
    # sell_data -> sell_data     : {market: market} -> {market: user, market, advertiser}
    # PROOF
    # {market: user, market, advertiser} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}

    if a_user_exists and sell_data:
        # DECLASSIFY
        # m_book_id -> a_book_id            : {market: user, market} -> {market: user, market, advertiser}
        # PROOF
        # {market: user, market, advertiser} U {market: {}} = {market: {}}
        # {market: user, market} C {market: {}}

        # {market: user, market, advertiser} U {market: user, market, advertiser} C {market: user, market, advertiser}
        a_book_id = m_book_id

        # DECLASSIFY
        # customers_db[user_name] -> customers_db[user_name]     : {market: market} -> {market: market, advertiser}
        # PROOF
        # {market: market, advertiser} U {market: {}} = {market: {}}
        # {market: market} C {market: {}}

        """
            Change label with allowed flow:
            customers_db[user_name]["searches"] -> customers_db[user_name]["searches"]   :  {market: market} -> {market: user, market}
        """
        # {market: user, market, advertiser} C {market: market, advertiser}
        """{market: user(customer), market} C {market: user(customer), market}"""
        if matches:
            # Only update user searches if there are some matches.
            customers_db[user_name]["searches"].extend(matches.keys())


    # if_acts_for(handle_search_book, (market)):
    # DECLASSIFY
    # matches -> p_matches            : {market: market} -> {market: user, market}
    # PROOF
    # {market: market, user} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}

    """ Already {market: market, user}, sufficient for return to user """

    p_matches = matches.copy()

    return p_matches


def handle_purchase_book(books_db, customers_db, book_id, price, name):
    # LABELS

    # books_db         : {market: market}
    # customers_db     : {market: market}
    # book_id          : {customer: customer, market}
    # price            : {customer: customer, market}
    # name             : {customer: customer, market}

    """
    INTEGRITY LABELS
    
    books_db         : {market: market}
    customers_db     : {market: market}
    book_id          : {all: customer, market}
    price            : {all: customer, market}
    name             : {all: customer, market}
    """

    # if_acts_for(handle_purchase_book, (market and customer)):
    """if_acts_for(handle_purchase_book, (none))"""

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
            # Allowed flow: {market: market, customer} U {market: market} = {market: market}
            # e U B = {market: market} U {market: market} = {market: market} is equal to match
            """
            Allowed flow: {market: customer, market} U {market: market} = {market: customer, market}
            e U B = {market: market} U {market: customer, market} = {market: customer, market}
            {market: customer, market} C {market: customer, market}
            """
            match = (id, data)
            break

    # if_acts_for(handle_purchase_book, (market)):
    # DECLASSIFY match to be read by customer
    # match -> c_match      : {market: market} -> {market: customer, market}
    # PROOF:
    # {market: customer, market} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}

    """ Already {market: customer, market}, sufficient for return to user """

    c_match = match

    if c_match is None:
        # Allowed flow: {market: customer, market}
        """ Allowed flow: {market: customer, market} """
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
        # Allowed flow {market: market}
        """ Allowed flow {market: market} """
        if m_name == user_name:
            # Allowed flow {market: market} U {market: customer, market} = {market: market}
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

    """ Already {market: customer, market}, sufficient for purchase """

    cv_cust_address = m_cust_address
    cv_vendor_name = m_vendor_name
    cv_user_exists = user_exists
    cv_ret = ret
    cv_book_id = m_book_id
    cv_name = m_name

    if cv_user_exists:
        # Allowed flow {market: customer, vendor, market}
        """ Allowed flow {market: customer, market} U {market: customer, market} """
        cv_ret = f"Book: {cv_book_id} sold by {cv_vendor_name} to {cv_name} at {cv_cust_address}"

        # Allowed flow {market: customer, vendor, market} C {market: market}
        """ Allowed flow {market: customer, market} U {market: customer, market} C {market: customer, market}"""
        books_db[cv_book_id]["issold"] = True

        # Allowed flow {market: customer, vendor, market} C {market: market}
        """ Allowed flow {market: customer, market} U {market: customer, market} C {market: customer, market}"""
        customers_db[m_name]["purchases"].append(cv_book_id)

    if not cv_user_exists:
        # Allowed flow: {market: customer, market}
        """ Allowed flow: {market: customer, market} """
        ret = "User does not exist"
        return ret

    # {market: market}
    """{market: customer, market}"""
    sell_data = False
    if customers_db[m_name]["sell_data"]:
        """----------------------can we say true is market: customer, market------------------------"""
        """{market: customer, market} C {market: customer, market}"""
        sell_data = True

    # if_acts_for(handle_purchase_book, (market)):
    # DECLASSIFY
    # sell_data -> sell_data     : {market: market} -> {market: customer, vendor, market, advertiser}
    # PROOF
    # {market: customer, vendor, market, advertiser} U {market: {}} = {market: {}}
    # {market: market} C {market: {}}

    if sell_data:
        # if_acts_for(handle_purchase_book, (market)):
        # DECLASSIFY
        # customers_db[user_name] -> customers_db[user_name]     : {market: market} -> {market: market, advertiser}
        # PROOF
        # {market: market, advertiser} U {market: {}} = {market: {}}
        # {market: market} C {market: {}}
        # {market: market, advertiser} C {market: market, advertiser}

        pass

    return cv_ret
