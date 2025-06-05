# 🌟 **Fitness Class Booking API Documentation** 🌟

Welcome to the **Fitness Class Booking API**! This API allows you to manage fitness classes, book available slots, and retrieve details of your fitness bookings.


## 🏋️‍♀️ **Fitness Class Endpoints**

### 1️⃣ **GET /fitness-classes/**

#### 📝 **Description**:
Retrieves a list of all fitness classes, ordered by the most recent first. Perfect for displaying available classes to users.

#### 🔧 **Request**:
GET /fitness-classes/
✅ Response Example:
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "MyYoga",
            "date_time": "2025-06-10T12:00:00Z",
            "instructor": "Joe",
            "total_slots": 2,
            "available_slots": 0,
            "create_at": "2025-06-04T18:06:53.447548Z"
        },
        {
            "id": 2,
            "name": "XOXO",
            "date_time": "2025-06-10T12:00:00Z",
            "instructor": "Ravi",
            "total_slots": 5,
            "available_slots": 3,
            "create_at": "2025-06-04T17:41:02.600314Z"
        },
        {
            "id": 1,
            "name": "Zumba",
            "date_time": "2025-06-04T15:30:00Z",
            "instructor": "Rohit",
            "total_slots": 10,
            "available_slots": 9,
            "create_at": "2025-06-03T18:08:04.146113Z"
        }
    ]
}
💬 Response Status Codes:
    200 OK: Success! The list of fitness classes is retrieved.


2️⃣ POST /fitness-classes/
📝 Description:
    Create a new fitness class with the given details, including name, date/time, instructor, and available slots.
🔧 Request:
POST /fitness-classes/

📋 Request Example:
{
    "name": "Zumba",
    "date_time": "2025-06-04 15:30",
    "instructor": "Rohit",
    "total_slots": 10,
    "available_slots": 10
}

✅ Response Example:
{
    "detail": {
        "id": 5,
        "name": "My Yoda Academy",
        "date_time": "2025-06-06T15:30:00Z",
        "instructor": "Raj Sir",
        "total_slots": 10,
        "available_slots": 10,
        "create_at": "2025-06-04T19:24:21.117011Z"
    }
}


📅 Booking Endpoints

3️⃣ GET /get-all-bookings/
📝 Description:
    Retrieve a list of all bookings, optionally filtered by client email.

🔧 Request:
GET /get-all-bookings/?email=rutik@gmail.com

✅ Response Example:
[
    {
        "id": 4,
        "fitness_class_name": "MyYoga",
        "client_id": "04",
        "client_name": "Rutik Patel",
        "client_email": "rutik@gmail.com",
        "fitness_class": 3
    }
]

4️⃣ GET /get-all-bookings/
📝 Description:
    Retrieve all bookings without any filters.
🔧 Request:
GET /get-all-bookings/

✅ Response Example:
[
    {
        "id": 5,
        "fitness_class_name": "MyYoga",
        "client_id": "04",
        "client_name": "Rishab Pawar",
        "client_email": "Rishab@gmail.com",
        "fitness_class": 3
    },
    {
        "id": 4,
        "fitness_class_name": "MyYoga",
        "client_id": "04",
        "client_name": "Rutik Patel",
        "client_email": "rutik@gmail.com",
        "fitness_class": 3
    },
    {
        "id": 3,
        "fitness_class_name": "XOXO",
        "client_id": "1",
        "client_name": "Raj Patel",
        "client_email": "raj@gmail.com",
        "fitness_class": 2
    },
    {
        "id": 2,
        "fitness_class_name": "XOXO",
        "client_id": "1",
        "client_name": "Raj Patel",
        "client_email": "raj@gmail.com",
        "fitness_class": 2
    },
    {
        "id": 1,
        "fitness_class_name": "Zumba",
        "client_id": "1",
        "client_name": "Rahul Nair",
        "client_email": "rahul@gmail.com",
        "fitness_class": 1
    }
]

5️⃣ POST /create-booking/
📝 Description:
Schedule a booking for a fitness class. This checks if there are available slots for the chosen class and then creates the booking.

🔧 Request:
POST /create-booking/
📋 Request Example:
{
  "client_id": "1",
  "client_name": "Rahul Nair",
  "client_email": "rahul@gmail.com",
  "fitness_class": "2"
}

✅ Response Example (Success):
{
    "id": 6,
    "fitness_class_name": "XOXO",
    "client_id": "6",
    "client_name": "Madav Shaik",
    "client_email": "madav@gmail.com",
    "fitness_class": 2
}

***POSTMAN-COLLECTION***
https://api.postman.com/collections/40801920-202d418f-f0fa-42de-b2e0-c9a02323980a?access_key=PMAT-01JX0JKGEA7D38REHRQFQ2S7EJ


