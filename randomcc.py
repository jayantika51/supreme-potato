from tkinter import*
import random

root=Tk()
root.geometry("600x600")
root.title("Country Capital")

enter_country = Entry(root)
enter_country.place(relx = 0.5, rely = 0.2, anchor=CENTER)

enter_country_list = Label(root)
enter_country_list = Label(root)


enter_cities = Entry(root)
enter_cities.place(relx = 0.5, rely = 0.3, anchor=CENTER)

enter_cities_list = Label(root)
enter_cities_list = Label(root)

country_list=[]
cities_list=[]

def country_city_list():
    country = enter_country.get()
    country_list.append(country)
    display_country_list["text"]= "country name :"+ str(country_list)
    
    city= enter_capital.get()
    city_list.append(city)
    display_city_list["text"]="cities name:"+ str(city_list)
    
    
def random_country_city():
    length1 = len(country_list)
    random_no1 = random.randint(0,length1-1)
    
    random_country = country_list[random_no1]
    display_random_country_list["text"]="Random Countries :" +str(random_country)


    length2 = len(cities_list)
    random_no2 = random.randint(0,length2-1)

    random_cities = cities_list[random_no2]
    display_random_cities_list["text"]="Random Cities :" +str(random_cities)



btn = Button(root, text = "Display Country and Cities Name", command=country_city_list, bg="Royal Blue",fg="White")
btn.place(relx=0.5, rely=0.4, anchor= CENTER)

display_country_list.place(relx=0.5, rely=0.5, anchor=CENTER)
    
display_city_list.place(relx=0.5,rely=0.6, anchor = CENTER)


btn2=Button(root, text="Display Country and City Name Randomly",command=random_country_city,bg="Royal Blue", fg="White")
btn2.place(relx = 0.5, rely=0.7, anchor=CENTER)




main.loop()



























