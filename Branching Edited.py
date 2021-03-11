Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = input("Greetings! What is your year of origin?")
Greetings! What is your year of origin?
>>> if year < 1900:
    print ("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
elif year > 1900 & year > 2020:
    print ("Far out, that's the future!!")