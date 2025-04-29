# comments for CONFIDENTIALITY
""" comments for INTEGRITY """

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


def handle_new_book_offer(books_db, customers_db, book_id, vendor_name, title, author, year, edition, publisher, condition, description, price):
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
    
    books_db         : {all: market}
    customers_db     : {all: market}

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
    
    issold           : {all: market}
    """



    # if_acts_for(handle_new_book_offer, (market and vendor)):
    """ if_acts_for(handle_new_book_offer, (all)): """

    #DECLASSIFY all labels to be owned by market
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
    #DECLASSIFY all labels to be written by market

        book_id -> m_book_id             : {all: vendor} -> {all: market}
        vendor_name -> m_vendor_name     : {all: vendor} -> {all: market}
        title -> m_title                 : {all: vendor} -> {all: market}
        author -> m_author               : {all: vendor} -> {all: market}
        year -> m_year                   : {all: vendor} -> {all: market}
        edition -> m_edition             : {all: vendor} -> {all: market}
        publisher -> m_publisher         : {all: vendor} -> {all: market}
        condition -> m_condition         : {all: vendor} -> {all: market}
        description -> m_description     : {all: vendor} -> {all: market}
        price -> m_price                 : {all: vendor} -> {all: market}

        PROOF
        {all: market} U {all: {}} = {all: {market}}
        {all: vendor} C {all: market}
    """
    

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # allowed read flow: {market: market}
    """{all: market}"""
    success = ""

    # {market : market}
    """{all: market}"""
    flag = False

    # allowed read flow: {market: market}
    """{all: market}"""
    issold = False

    # allowed read flow: {vendor: vendor, market}
    """{all:  vendor, market}"""
    if not all([m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price]):
        #Allowed flow: {market: market} C {market: market}
        """{all: market} C {all: market}"""
        flag = True

    # allowed read from market DB
    if m_vendor_name not in customers_db:
        #Allowed flow: {market: market} C {market: market}
        """{all: market} C {all: market}"""
        flag = True
    
    # allowed read from market DB
    if m_book_id in books_db:
        #Allowed flow: {market: market} C {market: market}
        """{all: market} C {all: market}"""
        flag = True
    
    #DECLASSIFY 
    # flag -> v_flag  {market: market} -> {market: market, vendor}
    #PROOF
    # {market: market, vendor} U {market: {}; vendor: {}} = {market: {}; vendor: {}}
    # {market: market} C {market: {}; vendor: {}}

    """
    DECLASSIFY 
        flag -> v_flag  {all: market} -> {all: market, vendor}
        PROOF
        {all: market, vendor} U {market: {}; vendor: {}} = {market: {vendor, market}, vendor: {vendor, market}}
        {all: market} C {market: {vendor, market}, vendor: {vendor, market}}
    """

    v_flag = flag

    if v_flag:
        #allowed flow {market: market, vendor}
        return success

    # All data fields owned by vendor, shared with market for storage
    # Information Flow: All below are secure as values are inserted into market-controlled DB
    books_db[book_id] = {
        "vendor_name": m_vendor_name,              """{all/: market}""" # {market: market} 
        "title": m_title,                          """{all/: market}""" # {market: market}
        "author": m_author,                        """{all/: market}""" # {market: market}
        "year": m_year,                            """{all/: market}""" # {market: market}
        "edition": m_edition,                      """{all/: market}""" # {market: market}
        "publisher": m_publisher,                  """{all/: market}""" # {market: market}
        "condition": m_condition,                  """{all/: market}""" # {market: market}
        "description": m_description,              """{all/: market}""" # {market: market}
        "price": m_price,                          """{all/: market}""" # {market: market}
        "issold": issold                            # {market: market}
    }

    #{market: market}
    """{all/: market}"""
    success = f"Offer added successfully" 

    #must declassify so vendor can read
    #DECLASSIFY(success, {vendor: vendor})
        # success -> success          {market: market} -> {market: market, vendor}  

        # PROOF:
        # {market: market, vendor} U {market: {}; vendor: {}} = {market: {}; vendor: {}}
        # {market: market} C {market: {}; vendor: {}}

    """
    DECLASSIFY(success, {all: vendor, market})
        success -> success          {all: market} -> {all: vendor, market}  

        PROOF:
        {all: market, vendor} U {market: {}; vendor: {}} = {market: {vendor, market}, vendor: {vendor, market}}
        {all: market} C {market: {vendor, market}, vendor: {vendor, market}}
    """

    return success

def handle_search_book(books_db, book_id, vendor_name, title, author, year, edition, publisher, condition, description, price):
    """
        Event handler for a user searching for a book.
    """

    # LABELS

    # books_db         : {market: market}
    
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
    
    books_db         : {all: market}
    customers_db     : {all: market}

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
    
    issold           : {all: market}
    """


    # if_acts_for(handle_search_book, (market and user)):
    """ if_acts_for(handle_search_book, (all)): """

    #DECLASSIFY all labels to be owned by market
    # book_id -> m_book_id             : {user: user, market} -> {market: user, market}
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
    DECLASSIFY all labels to be written by market

        book_id -> m_book_id             : {all: user} -> {all: market, user}
        vendor_name -> m_vendor_name     : {all: user} -> {all: market, user}
        title -> m_title                 : {all: user} -> {all: market, user}
        author -> m_author               : {all: user} -> {all: market, user}
        year -> m_year                   : {all: user} -> {all: market, user}
        edition -> m_edition             : {all: user} -> {all: market, user}
        publisher -> m_publisher         : {all: user} -> {all: market, user}
        condition -> m_condition         : {all: user} -> {all: market, user}
        description -> m_description     : {all: user} -> {all: market, user}
        price -> m_price                 : {all: user} -> {all: market, user}

        PROOF
        {all: market, user} U {all: {}} = {all: {market, user}}
        {all: user} C {all: market, user}
    """

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # {market: market}
    """{all: market, user}"""
    matches = set() 
    for id, data in books_db:
        matches.add((id,data))
    # {market: market}
    """{all: market, user}"""
    matches_copy = matches.copy() 

    if m_book_id:
        for (id, data) in matches:
            if not m_book_id == id:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_vendor_name:
        for (id, data) in matches:
            if not m_vendor_name == data['vendor_name']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 

    if m_title:
        for (id, data) in matches:
            if not m_title == data['title']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 

    if m_author:
        for (id, data) in matches:
            if not m_author == data['author']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 

    if m_year:
        for (id, data) in matches:
            if not m_year == data['year']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_edition:
        for (id, data) in matches:
            if not m_year == data['year']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""            
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_publisher:
        for (id, data) in matches:
            if not m_publisher == data['publisher']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_condition:
        for (id, data) in matches:
            if not m_condition == data['condition']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches_copy.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_description:
        for (id, data) in matches:
            if not m_description == data['description']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    if m_price:
        for (id, data) in matches:
            if not m_price == data['price']:
                # Allowed flow: {market: user, market} U {market: market} = {market: market}
                """{all: market, user} U {all: market, user} = {all: market, user}""" 
                """{all: market, user} C {all: market, user}"""                
                matches.remove((id,data))
    # {market: market}
    """{all: market, user}"""
    matches = matches_copy.copy() 
    
    #DECLASSIFY
        # matches -> p_matches            : {market: market} -> {market: user, market}
        # PROOF
        # {market: market, user} U {market: {}; user: {}} = {market: {}; user: {}}
        # {market: market} C {market: {}; user: {}}

    """ Already {all: market, user}, sufficient for return to user """

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
    
    books_db         : {all: market}
    customers_db     : {all: market}
    book_id          : {all: customer, market}
    price            : {all: customer, market}
    name             : {all: customer, market}
    """


    # if_acts_for(handle_purchase_book, (market and customer)):

    #DECLASSIFY labels to be owned by market
    # book_id -> m_book_id             : {customer: customer, market} -> {market: customer, market}
    # price -> m_price                 : {customer: customer, market} -> {market: customer, market}
    # name -> m_name                   : {customer: customer, market} -> {market: customer, market}
    # PROOF:
    # {market: market, customer} U {market: {}; customer: {}} = {market: {}; customer: {}}
    # {customer: customer, market} C {market: {}; customer: {}}


    """
    Already {all: customer, market}, sufficient for checking db

        book_id -> m_book_id             : {all: customer, market}
        price -> m_price                 : {all: customer, market}
        name -> m_name                   : {all: customer, market}
    """

    m_book_id, m_price, m_name = book_id, price, name

    # {market: market, customer}
    """ {all/: customer, market} """ 
    ret = ""    

    # {market: market}
    """ {all: customer, market} """
    match = None 

    for id, data in books_db:
        if m_book_id == id and data['issold'] == False and m_price == data['price']:
            # Allowed flow: {market: market, customer} U {market: market} = {market: market}
            # e U B = {market: market} U {market: market} = {market: market} is equal to match
            """
            Allowed flow: {all: customer, market} U {all: market} = {all: customer, market}
            e U B = {all: market} U {all: customer, market} = {all: customer, market}
            {all: customer, market} C {all: customer, market}
            """
            match = (id,data)
            break

    #DECLASSIFY match to be read by customer
    # match -> c_match      : {market: market} -> {market: customer, market}
    # PROOF:
    # {market: cusomter, market} U {market: {}; customer: {}} = {market: {}; customer: {}}
    # {market: market} C {market: {}; customer: {}}
    
    """ Already {all: customer, market}, sufficient for return to user """

    c_match = match

    if c_match == None:
        # Allowed flow: {market: customer, market}
        """ Allowed flow: {all: customer, market} """
        ret = "Error purchasing book"
        return ret

    # {market: market}
    """ {all: customer, market} """
    m_vendor_name = match[1]['vendor_name'] 

    # {market: market}
    """ {all: customer, market} """
    vendor_exists = False 

    # {market: market}
    """ {all: customer, market} """
    m_cust_address = None 


    for user_name, address in customers_db:
        # Allowed flow {market: market}
        """ Allowed flow {all: market} """
        if m_name == user_name:
            # Allowed flow {market: market} U {market: customer, market} = {market: market}
            """ Allowed flow {all: market} U {all: customer, market} = {all: customer, market}
                e U B = {all: market} U {all: customer, market} = {all: customer, market} 
                {all: customer, market} C {all: customer, market} """
            m_cust_address = address
        if m_vendor_name == user_name:
            # Allowed flow {market: market} U {market: market} = {market: market}
            """ Allowed flow {all: market} U {all: customer, market} = {all: customer, market}
                e U B = {all: market} U {all: customer, market} = {all: customer, market} 
                {all: customer, market} C {all: customer, market} """
            vendor_exists = True

    #DECLASSIFY return variables to be read by customer, vendor
    # vendor_exists -> cv_vendor_exists      : {market: market} -> {market: customer, vendor, market}
    # m_cust_address -> cv_cust_address      : {market: market} -> {market: customer, vendor, market}
    # m_vendor_name -> cv_vendor_name        : {market: market} -> {market: customer, vendor, market}
    # PROOF:
    # {market: customer, vendor, market} U { market: {}; customer: {}} = {market: {}; customer: {}}
    # {market: market} C {market: {}; customer: {}}

    #DECLASSIFY return variables to be read by customer, vendor
    # ret -> cv_ret                          : {market: customer, market} -> {market: customer, vendor, market}
    # m_book_id -> cv_book_id                : {market: customer, market} -> {market: customer, vendor, market}
    # m_name -> cv_name                      : {market: customer, market} -> {market: customer, vendor, market}
    # PROOF:
    # {market: customer, vendor, market} U {market: {}; customer: {}} = {market: {}; customer: {}}
    # {market: customer, market} C {market: {}; customer: {}}

    """ Already {all: customer, market}, sufficient for purchase """

    cv_cust_address = m_cust_address
    cv_vendor_name = m_vendor_name
    cv_vendor_exists = vendor_exists
    cv_ret = ret
    cv_book_id = m_book_id
    cv_name = m_name

    if cv_vendor_exists:
        # Allowed flow {market: customer, vendor, market}
        """ Allowed flow {all: customer, market} U {all: customer, market} """
        cv_ret = f"Book: {cv_book_id} sold by {cv_vendor_name} to {cv_name} at {cv_cust_address}"
        return cv_ret

    