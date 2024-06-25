Please test the following endpoints:


----Menu----

http://127.0.0.1:8000/menu/
http://127.0.0.1:8000/menu/1      i.e. http://127.0.0.1:8000/menu/<int:pk>     Test whichever numbers you wish for whichever menu items you wish to add with your superuser



----Signing Up (and for management checks of the number of users)----

http://127.0.0.1:8000/users



----Obtaining Authorization----

http://127.0.0.1:8000/api-token-auth/
http://127.0.0.1:8000/auth/token/login/
http://127.0.0.1:8000/auth/token/logout/


----Booking----

http://127.0.0.1:8000/restaurant/booking/

