import requests
import time

now = time.strftime("\t\t%b %d, %Y %H:%M:%S\n\n")
print("\t\tCurrent time is: \n\n", now)


print("\t\tWelcome to the Weather Forecaster!\n\n")
print("\t\tYou can find the City you want the weather report!\n\n")
 
city_name = input("Enter the name of the City : ")
print("\n\n")

def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)