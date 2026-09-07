## Test Failure Output
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_books_page_contains_title (catalog.tests.BookListTest.test_books_page_contains_title)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ErikB\cidm3312\book-catalog\catalog\tests.py", line 16, in test_books_page_contains_title
    self.assertContains(response, "Theodore Rex")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Theodore Rex' in the following response
b'<html>\n<head>\n    <title>Book Catalog</title>\n</head>\n<body>\n    <nav>\n        <a href="/">Book List</a> |\n        <a href="/publishers/">Publisher List</a> |\n        <a href="/reviews/">Review List</a>\n    </nav>\n\n    \n\n    <h1>Book List</h1>\n\n    <ul>\n    \n        <li>\n            <b></b>\n            <ul>\n                <li> pages</li>\n                <li>Published by: </li>\n                <li>Number of reviews: </li>\n            </ul>\n        </li>\n    \n    </ul>\n\n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.022s

FAILED (failures=1)
Destroying test database for alias 'default'...

## Test Failure Reflection:
This failure tells me that the book I added to my database has not been displayed correctly on my Book List page, but this particular failure could have multiple potential causes.

## Question 1:
I am picking the "book" foreign key. This foreign key resides in the Review model. This foreign key points to the Book model because each individual book might have multiple reviews that are associated with it. If I had reversed this relationship, then each review could point to multiple different books. Logically, this does not make any sense - a book review is written for a specific book.

## Question 2:
I chose to add a field which specified the number of pages for each book in my database. I chose the integer field because the data stored is always going to be a whole number - books do not have fractional page counts. By storing this data using an integer field, it allows me the option to perform arithmetic with the page counts stored in my database. For example, I could add up and display the total number of pages that have been published by each publisher. If I had stored this data as a CharField, I would no longer be able to perform calculations in this way, since trying to add these values together would simply concatenate the strings together.