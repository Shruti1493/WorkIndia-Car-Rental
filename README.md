API Points

1. SignUp API
   http://127.0.0.1:8000/api/signup/

    {
      "username": "test3",
      "password": "admin",
      "email":"test3@gmail.com"
    }
   
2.  Login API
  http://127.0.0.1:8000/api/login/

   {
    "username": "admin1",
    "password": "admin"  
   }
  
3.  Add a new Car for renting
   http://127.0.0.1:8000/api/car/create/

   Include API-KEY in headers
   API-KEY : shrutikedari

    
   {
    "category": 
        "SUV"
    ,
    "model": 
        "BMW Q3"
    ,
    "number_plate": 
        "KA1234"
   ,
    "current_city": 
        "bangalore"
    ,
    "rent_per_hr": 
        "100"
    
   }

4. GET car details
   http://127.0.0.1:8000/api/car/details/get-rides?origin=bangalore&dest=Delhi&cat=SUV&rh=1

5. Book a Car
   http://127.0.0.1:8000/api/car/details/rent/
   {
    "car_id": 
        "1"
    ,
    "origin": 
        "bangalore"
    ,
    "dest": 
        "Delhi"
    ,
    "hr":  "10"    
   }

6. Ride Completion
   http://127.0.0.1:8000/api/car/details/postsave/
   {

    "car_id": 
        "1"
    ,
    "origin": 
        "bangalore"
    ,
    "dest": 
        "Delhi"
    ,
    "hr":  "10"
    
   }

 
