# CodeClan Library Weekend Homework

Your task is to model a Flask app which will list books in a Library.

## MVP

Your application should have a single class - Book - and should contain the following properties:

* Title
* Author
* Genre

Provide the following functionality:

* List all Books
* Show an individual Book
* Add a new Book to the Library.
* Remove a Book from the Library

## Extensions

* Add a `checked_out` boolean property to the `Book` class.
* When displaying a book, display whether it is checked in or checked out.
* Style the app using CSS.

## Advanced Extensions

* Give the user the ability to update whether a book is checked in or out. 
    * Because we can't use the `PUT` HTTP method you will need to use a form to send a `POST` route to `/books/<index>`. This form should use a checkbox or radio buttons to update the checked out status.
* Anything else you can think of.

#### Guidance

To style a Flask app you will need to put your CSS files inside a folder called `static` inside the `app` package.

Then add the following line inside the <HEAD> tag of your `base.html`

```html
    <link rel="stylesheet" href="{{ url_for('static', filename='your_file_name.css') }}">
```

> When deleting the Book use a form and the index position of the book to determine which book should be deleted.

> An HTML checkbox input value will only be included in the form dictionary if the box is checked. By default, no value will be present if the checkbox is not checked and the value 'on' will be present if it is checked.

> Grouped Radio buttons need to have the same `name` attribute to allow you to toggle between them.

> Remember and test your Book class properties. In the top level folder of the app create a tests folder with a `book_test.py` file. Create a `run_tests.py` file with the following:

```python
import unittest
from tests.book_test import TestBook

if __name__ == '__main__':
    unittest.main()
```
