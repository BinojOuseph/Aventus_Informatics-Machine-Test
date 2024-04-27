# Employee Management API

This API provides endpoints to manage employee data.

Use the command : "python manage.py createsuperuser" for create a super admin to view and control the sqllite database

## API Endpoints (you can use tools like swagger or postman etc. for testing this endpoints.)

### 1. Get Employee Data

- URL : `http://127.0.0.1:8000/app/employee`
- Method : GET
- Functionality : Retrieve a list of all employees.

### 2. Create New Employee

- URL : `http://127.0.0.1:8000/app/employee`
- Method : POST
- Body : {
  	   "name": "string",
  	   "address": "string",
  	   "email": "user@example.com",
  	   "image": "jpg", "jpeg", "png", "webp"
	 }
- Functionality : Create a new employee record.

### 3. Get, Update, or Delete Employee by ID

- URL : `http://127.0.0.1:8000/app/employee/<employee_id>`
- Method : 
  - GET: Retrieve details of a specific employee.
  - PUT: Update details of a specific employee.
	- Body : {
  	   "name": "string",
  	   "address": "string",
  	   "email": "user@example.com",
  	   "image": "jpg", "jpeg", "png", "webp"
	 }
  - DELETE: Delete a specific employee.