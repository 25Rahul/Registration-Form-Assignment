# Flask Registration Form with MySQL

This is a simple web application built using Flask and MySQL. It allows users to submit their registration details (name, email, and date of birth) and stores the data in a MySQL database. Additionally, the app supports CRUD (Create, Read, Update, Delete) operations for managing registration entries.

# Features
Register a user with name, email, and date of birth.
Store user details in a MySQL database.
Flash messages to show success or error messages.
CRUD operations to create, read, update, and delete registrations.

# Prerequisites
Before running this project, make sure you have the following installed:

1)Python 3.x: Make sure Python is installed. You can download it from here.
2)Flask: A Python web framework, which you can install via pip.
3)MySQL: A relational database management system. You can install MySQL from here

# Installation and Setup

Step 1: Clone the repository or set up your project directory
```
git clone https://github.com/your-username/flask-registration-form.git
cd flask-registration-form 
```
Step 2: Install Python Dependencies

Install the required dependencies using pip:
```pip install flask mysql-connector-python```

Step 3: Set Up MySQL Database

1)Open MySQL and create a database called mydatabase:

```USE mydatabase;```
```CREATE TABLE Registration (```
    ```ID INT AUTO_INCREMENT PRIMARY KEY,```
    ```Name VARCHAR(100) NOT NULL,```
    ```Email VARCHAR(100) NOT NULL UNIQUE,```
    ```DateOfBirth DATE NOT NULL,```
    ```RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP```
```);```

