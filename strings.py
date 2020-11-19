#brief refresher on strings, the very first level of complexity 

Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Akhil Varanasi'
#defines the string variable name
>>> age = 21
#defines the string variable age
>>> favorite_cars = ['McLaren', 'Porsche', 'Lamborghini']
#creates a list array with three entries
>>> print(name)
#prints variable name
Akhil Varanasi
>>> print(age)
#prints variable age
21
>>> print (favorite_cars[0])
#prints the first entry from the previously defined array
McLaren
>>> str.find("Akhil Varanasi","kh")
#uses str to find the position at which 'kh' first appears
#since the first instance of kh appears at position 1, 1 is printed 
1
>>> str.replace(name,"Akhil", "Akh")
#Replaces first name 'Akhil' with 'Akh'
'Akh Varanasi'
>>> name = str.replace(name,"Akhil", "Akh")
#sets name variale equal to 'Akh Varanasi'
>>> name
'Akh Varanasi'
#prints aforementioned line
>>> car_string = "Bugatti,Pagani,Ferrari"
>>> car_list = str.split(car_string,',')
>>> car_list
['Bugatti', 'Pagani', 'Ferrari']
