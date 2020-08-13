# product-catalog aka DealBoxer
a Django application for the following problem statement. <br> 1. Product listing page which lists all the products available in the database. List their name and quantity.<br> 2. Product detail page where details of a product is displayed. Details are:- Name, Quantity, Image of the product. <br> 3. Registration Page​,  User should register before accessing detail page or listing page. User Registration details: - email, phone number, username, full name &amp; password ​ .
 <br>4. Login​ functionality with ​session management ​ .   

#Features
1 : User Registration <br>
2 : Basic Authentication with username and password


Getting Started
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/shubham2637/product-catalog.git
    $ cd product-catalog

    # Install the requirements
    $ pip install -r requirements.txt



    # Perform database migrations if required
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Start the server
    $ python manage.py runserver
    
    Open bowser at http://127.0.0.1:8000/


**NOTE**: I highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).

<hr>
------------
Contributing
------------

We welcome contributions of all kinds. If you would like to know what work is needed to be done, check the [issue tracker](https://github.com/DrkSephy/django-hackathon-starter/issues). Before sending a pull request, please open an issue. This project follows the [pep-0008](https://www.python.org/dev/peps/pep-0008/) style guide.
