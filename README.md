# Django Web Based Inventory App

![Landing Page](https://imgur.com/Lg8BNQZ.png)



> A web-based inventory management application developed using Django.

---

## Table of Contents

- [Project Name](#django-inventory-app)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The Django Inventory App is a web-based application built with Django framework that allows users to manage their inventory. It provides features such as adding products, tracking stock levels, recording sales, generating reports, and more.

[View Deployed Site](http://mikiyas.pythonanywhere.com)
[Final Project Blog Article](https://www.example.com)
[Author(s) LinkedIn]
[Mikiyas Ayele Kore](https://www.linkedin.com/in/mikiyas-ayele)
[Mikiyas Ayele Kore](https://linkedin.com/in/dagim-wallelgne-218860231)

---

## Installation

To run the Django Inventory App on your local machine, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Mickykore/Web_Based_Inventory_managment.git
   ```

2. Change to the project's directory:

   ```shell
   cd django-inventory-app
   ```

3. Create a virtual environment:

   ```shell
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```shell
   python manage.py migrate
   ```

7. Create a superuser:

   ```shell
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```shell
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000`.

---

## Usage

- To access the admin interface, go to `http://localhost:8000/admin` and log in using the superuser credentials.
- Use the admin interface to manage products, sales, and generate reports.
- Regular users can register for an account and log in to access their inventory management dashboard.

### How To use

#### Add Product in product page
![Product Page](https://i.imgur.com/4wxwMz2.png)

#### Add Sales in sales page
![Sales Page](https://i.imgur.com/nzuB0zQ.png)

#### Add Order in order page
![Order Page](https://i.imgur.com/NqXgS3i.png)

#### View Reports in 
![Report Page](https://i.imgur.com/BwqV12c.png)

---

## Contributing

Contributions to the Django Inventory App are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request detailing your changes.

---


## License

The Django Inventory App is open source and available under the [MIT License](LICENSE).