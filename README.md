# Python-SQL Business Analytics Tool

## **Overview**
This project is a command-line application for managing and querying a Yelp-style database, designed to handle user interactions, business reviews, and social connections efficiently. Built with Python and SQL Server, the system allows users to log in, search for businesses, connect with other users, and submit reviews. The application is built with a modular and scalable architecture, ensuring ease of maintenance and extensibility. It employs database querying techniques and robust error handling to provide a smooth user experience.

---

## **Features**
### **User Authentication**
- Secure login system using unique user IDs
- Prevents unauthorized access with validations and error handling

### **Business Search**
- Query businesses based on:
  - Name
  - City
  - Star rating range [min, max]
- Results are sorted by name and displayed in a user-friendly format
- Case-insensitive search for improved usability

### **User Search**
- Search users by:
  - Name
  - Usefulness (yes/no)
  - Funny (yes/no)
  - Cool (yes/no)
- Users can add friends, recorded in the Friendship table

### **Review System**
- Users can write and submit reviews
- Business ratings and review counts update dynamically
- Ensures database consistency using triggers and validation

### **Error Handling**
- Prevents invalid inputs and ensures data integrity
- Automatically corrects minor input errors where possible
- Gracefully handles database connection issues

---

## **Technologies Used**
- **Programming Language**: Python
- **Database**: SQL Server
- **Libraries**:
  - `pyodbc` – Database connection
  - `string` – String manipulation
  - `secrets` – Secure key generation
  - `datetime` – Time-based operations

---

## **Setup**

### **1. Dependencies**
Ensure Python is installed along with the required libraries. Install missing packages using:
```
pip install {Package}
```

### **2. Database Configuration**
Configure your database connection in main.py:
```
connection = pyodbc.connect('Driver={SQL Server};Server=server.sample.ca;uid=user123;pwd=password123')
```

### **3. Running the Code**
Run the code by entering this into terminal:
```
python main.py
```
