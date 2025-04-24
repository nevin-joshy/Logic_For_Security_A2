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

    QUESTIONS:
    Do I need to define returns like in the paper?
    Does the returned value need to be only owned by receiver i.e. vendor? (should success be {vendor, vendor} by the end - declassify it)
        In the if statement, success should be declassified, but then is it allowed to be there
    Do we need to do out the for loops and define the type and label of the iterator?
    Do we need to make a user interactive? or just these functions with the inputs?
    info flow analysis - page 136 diagram?
    show books in search that are sold out?
    """

    # LABELS
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

    # success          : {market : market}

    # if_acts_for(handle_new_book_offer, (market and vendor)):

    #DECLASSIFY all labels to be owned by market
        # book_id -> m_book_id             : {vendor: vendor, market} -> {market: vendor, market}
        # vendor_name -> m_vendor_name     : {vendor: vendor, market} -> {market: vendor, market}
        # title -> m_title                 : {vendor: vendor, market} -> {market: vendor, market}
        # author -> m_author               : {vendor: vendor, market} -> {market: vendor, market}
        # year -> m_year                   : {vendor: vendor, market} -> {market: vendor, market}
        # edition -> m_edition             : {vendor: vendor, market} -> {market: vendor, market}
        # publisher -> m_publisher         : {vendor: vendor, market} -> {market: vendor, market}
        # condition -> m_condition         : {vendor: vendor, market} -> {market: vendor, market}
        # description -> m_description     : {vendor: vendor, market} -> {market: vendor, market}
        # price -> m_price                 : {vendor: vendor, market} -> {market: vendor, market}

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price

    # allowed write flow: {market: market}
    success = ""

    # allowed write flow: {market: market}
    issold = False

    # allowed read flow: {vendor: vendor, market}
    if not all([m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price]):
        #Allowed flow: {market: vendor, market}
        #must declassify so vendor can read
        #DECLASSIFY(success, {market: market, vendor})
        return success

    # allowed read from market DB
    if m_vendor_name not in customers_db:
        #Allowed flow: {market: vendor, market}
        #must declassify so vendor can read
        #DECLASSIFY(success, {market: market, vendor})
        return success
    
    # allowed read from market DB
    if m_book_id in books_db:
        #Allowed flow: {market: vendor, market}
        #must declassify so vendor can read
        #DECLASSIFY(success, {market: market, vendor})
        return success 

    # All data fields owned by vendor, shared with market for storage
    # Information Flow: All below are secure as values are inserted into market-controlled DB
    books_db[book_id] = {
        "vendor_name": vendor_name,              # {market: vendor, market}
        "title": title,                          # {market: vendor, market}
        "author": author,                        # {market: vendor, market}
        "year": year,                            # {market: vendor, market}
        "edition": edition,                      # {market: vendor, market}
        "publisher": publisher,                  # {market: vendor, market}
        "condition": condition,                  # {market: vendor, market}
        "description": description,              # {market: vendor, market}
        "price": price,                          # {market: vendor, market}
        "issold": issold                         # {market: market}
    }

    #{market: market}
    success = f"Offer added successfully"

    #must declassify so vendor can read
    #DECLASSIFY(success, {vendor: vendor})
    return success

def handle_search_book(books_db, book_id, vendor_name, title, author, year, edition, publisher, condition, description, price):
    """
        Event handler for a user searching for a book.
    """

    # LABELS

    # books_db         : {market: market}
    
    # book_id          : {public: public, market}
    # vendor_name      : {public: public, market}
    # title            : {public: public, market}
    # author           : {public: public, market}
    # year             : {public: public, market}
    # edition          : {public: public, market}
    # publisher        : {public: public, market}
    # condition        : {public: public, market}
    # description      : {public: public, market}
    # price            : {public: public, market}


    # if_acts_for(handle_search_book, (market and public)):

    #DECLASSIFY all labels to be owned by market
    # book_id -> m_book_id             : {public: public, market} -> {market: public, market}
    # vendor_name -> m_vendor_name     : {public: public, market} -> {market: public, market}
    # title -> m_title                 : {public: public, market} -> {market: public, market}
    # author -> m_author               : {public: public, market} -> {market: public, market}
    # year -> m_year                   : {public: public, market} -> {market: public, market}
    # edition -> m_edition             : {public: public, market} -> {market: public, market}
    # publisher -> m_publisher         : {public: public, market} -> {market: public, market}
    # condition -> m_condition         : {public: public, market} -> {market: public, market}
    # description -> m_description     : {public: public, market} -> {market: public, market}
    # price -> m_price                 : {public: public, market} -> {market: public, market}

    m_book_id, m_vendor_name, m_title, m_author, m_year, m_edition, m_publisher, m_condition, m_description, m_price = book_id, vendor_name, title, author, year, edition, publisher, condition, description, price



    matches = set() # {market: market}

    if m_book_id:
        for id, data in books_db:
            if m_book_id == id:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    
    if m_vendor_name:
        for id, data in books_db:
            if m_vendor_name == data['vendor_name']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_title:
        for id, data in books_db:
            if m_title == data['title']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_author:
        for id, data in books_db:
            if m_author == data['author']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_year:
        for id, data in books_db:
            if m_year == data['year']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_edition:
        for id, data in books_db:
            if m_year == data['year']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_publisher:
        for id, data in books_db:
            if m_publisher == data['publisher']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_condition:
        for id, data in books_db:
            if m_condition == data['condition']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_description:
        for id, data in books_db:
            if m_description == data['description']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    if m_price:
        for id, data in books_db:
            if m_price == data['price']:
                # Allowed flow: {market: public, market} U {market: market} = {market: market}
                matches.add((id,data))

    #DECLASSIFY
    # matches -> p_matches            : {market: market} -> {market: public, market}
    p_matches = matches.copy()

    return p_matches


def handle_purchase_book(books_db, customers_db, book_id, price, name):
    
    # LABELS

    # books_db         : {market: market}
    # customers_db     : {market: market}
    
    # book_id          : {customer: customer, market}
    # price            : {customer: customer, market}
    # name             : {customer: customer, market}

    # if_acts_for(handle_purchase_book, (market and customer)):

    #DECLASSIFY labels to be owned by market
    # book_id -> m_book_id             : {customer: customer, market} -> {market: customer, market}
    # price -> m_price                 : {customer: customer, market} -> {market: customer, market}
    # name -> m_name                   : {customer: customer, market} -> {market: customer, market}

    m_book_id, m_price, m_name = book_id, price, name

    ret = "" # {market: market, customer}
    match = None # {market: market}

    for id, data in books_db:
        if m_book_id == id and data['issold'] == False and m_price == data['price']:
            # Allowed flow: {market: market, customer} U {market: market} = {market: market}
            # e U B = {market: market} U {market: market} = {market: market} is equal to match
            match = (id,data)
            break

    #DECLASSIFY match to be read by customer
    # match -> c_match      : {market: market} -> {market: customer, market}
    c_match = match

    if c_match == None:
        # Allowed flow: {market: customer, market}
        ret = "Error purchasing book"
        return ret

    m_vendor_name = match[1]['vendor_name'] # {market: market}
    vendor_exists = False # {market: market}
    m_cust_address = None # {market: market}


    for user_name, address in customers_db:
        #Allowed flow {market: market}
        if m_name == user_name:
            # Allowed flow {market: market} U {market: customer, market} = {market: market}
            m_cust_address = address
        if m_vendor_name == user_name:
            # Allowed flow {market: market} U {market: market} = {market: market}
            vendor_exists = True

    #DECLASSIFY return variables to be read by customer, vendor
    # vendor_exists -> cv_vendor_exists      : {market: market} -> {market: customer, vendor, market}
    # ret -> cv_ret                          : {market: market, customer} -> {market: customer, vendor, market}
    # m_book_id -> cv_book_id                : {market: customer, market} -> {market: customer, vendor, market}
    # m_vendor_name -> cv_vendor_name        : {market: market} -> {market: customer, vendor, market}
    # m_name -> cv_name                      : {market: customer, market} -> {market: customer, vendor, market}
    # m_cust_address -> cv_cust_address      : {market: market} -> {market: customer, vendor, market}
    cv_vendor_exists = vendor_exists
    cv_ret = ret

    if cv_vendor_exists:
        # Allowed flow {market: customer, vendor, market}
        cv_ret = f"Book: {m_book_id} sold by {m_vendor_name} to {m_name} at {m_cust_address}"
        return cv_ret

    

    

    
    

                    
    
















