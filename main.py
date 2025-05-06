from info_flow import customers_db, books_db, sold_customers, handle_new_book_offer, handle_search_book, handle_purchase_book

if __name__ == "__main__":
    print("Initial Databases:")
    print("Customers:", customers_db)
    print("Books:", books_db)
    print("Sold Customers:", sold_customers)
    print("-" * 30)

    # --- Test Case 1: Successful Offer ---
    print("\n--- Test Case 1: BookWorld adds a new book ---")
    result1 = handle_new_book_offer(
        books_db, book_id=104, vendor_name="Charlie Davis",
        title="Advanced Algorithms", author="Alex Chen", year=2023, edition="1st",
        publisher="Academia Press", condition="new", description="Deep dive into algorithms.", price=55.00
    )
    print(f"Result 1: {result1}")
    print("Books DB after offer:", books_db.get(104))
    print("-" * 30)

    # --- Test Case 2: Offer Validation Fail (Duplicate ID) ---
    print("\n--- Test Case 2: BookWorld tries to add duplicate ID ---")
    result2 = handle_new_book_offer(
        books_db, book_id=104, vendor_name="Charlie Davis",
        title="Another Book", author="Test Author", year=2024, edition="1st",
        publisher="Test Pub", condition="new", description="Desc.", price=25.00
    )
    print(f"Result 2: {result2}")
    print("-" * 30)

    # --- Test Case 3: Search (Anonymous) ---
    print("\n--- Test Case 3: Anonymous search for 'Python' ---")
    result3 = handle_search_book(books_db=books_db, customers_db=customers_db, sold_customers=sold_customers, user_name=None, title="python")
    print(f"Result 3: Found {len(result3)} match(es)")
    for book in result3.values(): print(f"  - {book}")
    print("-" * 30)

    # --- Test Case 4: Search (Alice, Opted-In) ---
    print("\n--- Test Case 4: Alice searches for 'Coding' ---")
    result4 = handle_search_book(books_db=books_db, customers_db=customers_db, sold_customers=sold_customers, user_name="Alice Smith", title="data")
    print(f"Result 4: Found {len(result4)} match(es)")
    for book in result4: print(f"  - {book}")
    print("Alice's Searches after:", customers_db["Alice Smith"]["searches"])  # Check if logged
    print("-" * 30)

    # --- Test Case 5: Search (Charlie, Opted-Out) ---
    print("\n--- Test Case 5: Charlie searches for 'Data' ---")
    result5 = handle_search_book(books_db=books_db, customers_db=customers_db, sold_customers=sold_customers, user_name="Charlie Davis", title="Data")
    print(f"Result 5: Found {len(result5)} match(es)")
    for book in result5: print(f"  - {book}")
    print("Charlie's Searches after:", customers_db["Charlie Davis"]["searches"])  # Should log new ID 103
    print("-" * 30)

    # --- Test Case 6: Successful Purchase (Bob buys Python book) ---
    print("\n--- Test Case 6: Bob buys Python book (ID 103) ---")
    result6 = handle_purchase_book(books_db, customers_db, sold_customers, book_id=103, price=45.00, name="Bob Johnson")
    print(f"Result 6: {result6}")
    print("Book 103 issold status after:", books_db[103]['issold'])
    print("Bob's Purchases after:", customers_db["Bob Johnson"]["purchases"])
    print("-" * 30)

    # --- Test Case 7: Purchase Fail (Charlie tries to buy sold book) ---
    print("\n--- Test Case 7: Charlie tries to buy sold Python book (ID 103) ---")
    result7 = handle_purchase_book(books_db, customers_db, sold_customers, book_id=103, price=45.00, name="Charlie Davis")
    print(f"Result 7: {result7}")
    print("-" * 30)

    # --- Test Case 8: Purchase Fail (Alice tries with wrong price) ---
    print("\n--- Test Case 8: Alice tries to buy Algo book (ID 102) with wrong price ---")
    result8 = handle_purchase_book(books_db, customers_db, sold_customers, book_id=102, price=50.00, name="Alice Smith")
    print(f"Result 8: {result8}")
    print("Book 102 status after:", books_db[102]['issold'])  # Should still be False
    print("-" * 30)

    # --- Test Case 9: Purchase Fail (Non-existent customer) ---
    print("\n--- Test Case 9: Fake User tries to buy book (ID 103) ---")
    result9 = handle_purchase_book(books_db, customers_db, sold_customers, book_id=101, price=39.99, name="Fake User")
    print(f"Result 9: {result9}")
    print("-" * 30)

    print("\nFinal Databases:")
    print("Customers:", customers_db)
    print("Books:", books_db)
    print("Sold Customers:", sold_customers)
    print("-" * 30)
