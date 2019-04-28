import random
import webbrowser
import time


indVegBreakfast = ['Poha','Sooji Upma','Idli with Sambar Curry','Masala Dosa']

indNvegBreakfast = ['Prawn Dosa','Roti & Egg Bhurji','Chicken Masala Dosa']

indLunchVegApp= ['Kanji Vada','Peanut Gajak','Quinoa, Couscous, and Beetroot Tikki','Dahi Anjeer Ke Kebab','Singhade Ki Kadhi']
indLunchVegMain = ['Ajwaini Paneer Kofta Curry', 'Handi Paneer', 'Labra (Mixed Veg)','Sitaphal ki Subzi']
indLunchVegDes = ['Thandai Barfi','Kesari Gujiys', 'Bhang Peda','Pluck Style Classic Dahi Vada','Thandai Rasmalai']

indLunchNvegApp = ['Mutton Ghee Roast','Sous-Vide Salmon Tikka']
indLunchNvegMain = ['Hokh Hund Mutton Kofte','Marchwangan Korma']
indLunchNvegDes = ['Thandai Barfi','Kesari Gujiys', 'Bhang Peda','Pluck Style Classic Dahi Vada','Thandai Rasmalai']

indDinnerVegApp = ['Pluck Style Classic Dahi Vada','Gulab Badam Chikki','Subz Badam Ka Shorba','Ariselu']
indDinnerVegMain = ['Ruwangan Hachi Chaman','Basanti Pulao','Paneer Tamatar Ki Subzi']
indDinnerVegDes = ['Kesari Shrikhand','Chocolate Prunes Gujiyas','Pluck Style Classic Dahi Vada','Seviyan Kheer','Badam Aur Gulkand']

indDinnerNvegApp = ['Peshawari Chapli Kebab','Kalmi Kebab']
indDinnerNvegMain = ['Al Hachi Chicken','Char Minar Biryani',]
indDinnerNvegDes = ['Thandai Barfi','Kesari Gujiys', 'Bhang Peda','Pluck Style Classic Dahi Vada','Thandai Rasmalai']

mexVegBreakfast = ['Black Bean, Egg, And Vegetable Breakfast Enchiladas Verdes','Vegan Migas']

mexNvegBreakfast = ['Mexican Baked Eggs','Huevos Rancheros Breakfast Casserole']

mexLunchVegApp= ['Baked Black Bean Taquitos','Toasted Ravioli Nachos','Sweet Potato Quesadilla','Baked Chili Rellenos','Pico de Gallo','Savory Phyllo Cups','Jalapeno Popper Wontons']
mexLunchVegMain = ['One Pan Mexican Quinoa','Black Bean Vegan Enchiladas','Tofu Tacos','Mexican Rice Casseroles','Veggie Fajita Enchiladas','Mexican Red Lentil Stew','Grilled Zuchhini Tacos','Spinach Artichoke Enchiladas','Black Bean Stew']
mexLunchVegDes = ['Brown Sugar Churros','Sopaipillas','Keto Mexican Chocolate Cheesecake','Mexican Cinnamon Brownies','Mexican Flan',' Dessert Trifles']

mexDinnerVegApp = ['Baked Black Bean Taquitos','Toasted Rvioli Nachos','Sweet Potato Quesadilla','Baked Chili Rellenos','Pico de Gallo','Savory Phyllo Cups','Jalapeno Popper Wontons']
mexDinnerVegMain = ['One Pan Mexican Quinoa','Black Bean Vegan Enchiladas','Tofu Tacos','Mexican Rice Casseroles','Veggie Fajita Enchiladas','Mexican Red Lentil Stew','Grilled Zuchhini Tacos','Spinach Artichoke Enchiladas','Black Bean Stew']
mexDinnerVegDes = ['Brown Sugar Churros','Sopaipillas','Dessert Trifles']

mexLunchNvegApp= ['Chicken Taquitos','Chili Nachos','Warm Chicken Tacos','Deep Fried Jalapeno Slices','Mexican Style Meatballs']
mexLunchNvegMain = ['Cream Cheese Chicken Enchiladas','Rice and Steak Tacos','Chipotle Crusted Pork Tenderloin','Mexican Turkey Burger','Grilled Mexican Steak']
mexLunchNvegDes = ['Keto Mexican Chocolate Cheesecake','Mexican Cinnamon Brownies','Mexican flan','Dessert Trifles']

mexDinnerNvegApp = ['Chicken Taquitos','Chili Nachos','Warm Chicken Tacos','Deep Fried Jalapeno Slices','Mexican Style Meatballs']
mexDinnerNvegMain = ['Cream Cheese Chicken Enchiladas','Rice and Steak Tacos','Chipotle Crusted Pork Tenderloin','Mexican Turkey Burger','Grilled Mexican Steak']
mexDinnerNvegDes = ['Dessert Trifles','Brown Sugar Churros','Sopaipillas']

itVegBreakfast = ['Veggie Sausage Strata','Tiramisu Crepes', 'Italian Veg Sandwich']
itNvegBreakfast = ['Italian Brunch Torte','Italian Baked Eggs & Sausage','Italian Clouded Eggs']

itLunchVegApp = ['Bruschetta','Italian Stuffed Mushrooms','Fried Cheese Sticks','Zuchhini Bites','Mini Caprese Bites']
itLunchVegMain = ['Eggplant Parmigiana','Mushroom Risotto','4 Cheese Pasta','Spinach and Cheese Ravioli','Tomato Spaghetti']
itLunchVegDes = ['Panna Cotta','Tiramisu Layer Cake','Brownie Biscotti','Strawberry Gelato','White Peach Tart']

itDinnerVegApp = ['Tomato Tartletts','Squash Blossoms with Pimento Ricotta','Feta and Radish Toast','Leek and Mushroom Croquettes','Crispy Kale with Lemon Yogurt Dip']
itDinnerVegMain = ['Caprese Salad with Pesto Sauce','Panzanella','Green Asparagaus Risotto','Vegetable Lasagna','']
itDinnerVegDes = ['Panna Cotta','Tiramisu layer cake','Brownie Biscotti','Strawberry Gelato','White peach tart']

itLunchNvegApp = ['Fried Anchovy Zuchhini stuffed with Blossoms','Shrimp and Rosemary Crostini','Italian Stuffed Mussels','Cavolo Nero and Prosciutto Bruschetta','Spaghetti Fritters with Ham and Smoked Mozzarella']
itLunchNvegMain = ['Chicken Pesto Pasta','Spaghetti with Meatballs','Pizza Napoletana','Shrimp Scampi with Pasta','Italian Breaded Pork Chops']
itLunchNvegDes = ['Panna Cotta','Tiramisu Layer Cake','Brownie Biscotti','Strawberry Gelato','White Peach Tart']

itDinnerNvegApp = ['Slow Cooked Italian Meatballs','Italian Steak Bruschetta','Italian Stuffed Mussels','Cavolo Nero and Prosciutto Bruschetta','Spaghetti Fritters with Ham and Smoked Mozzarella']
itDinnerNvegMain = ['Chicken Pesto Pasta','Spaghetti with Meatballs','Shrimp Scampi with Pasta','Eggplant Parmesan Pizza','Italian Breaded Pork chops']
itDinnerNvegDes = ['Panna Cotta','Tiramisu Layer cake','Brownie Biscotti','Strawberry Gelato','White Peach Tart']


mood = ''
meal = ''
pref = ''


name = (input("Hello, what is your name? "))
print("")
print("Hi,",name,"!  Welcome to CraveRave. We hope this service helps make your life easier when it comes to meal planning.")
print("")

time.sleep(3)

while mood not in range(1,4):
    try:
        mood = int(input("Let's get started!  What are you craving for? : Enter 1 for Indian, 2 for Mexican, or 3 for Italian. "))
        print("")
    except ValueError:
        print("Sorry, could you please repeat that?")
        print("")
        time.sleep(1)

while meal not in range(4,7):
    try:
        meal = int(input("And are you eating breakfast (4), lunch (5), or dinner (6)? "))
        print("")
    except ValueError:
        print("Sorry, could you please repeat that?")
        print("")
        time.sleep(1)

while pref not in range(7,9):
    try:
        pref = int(input("One last thing: do you want to meat in your food?  Press 7 for yes, 8 for no."))
        print("")
    except ValueError:
        print("Sorry, could you please repeat that?")
        print("")
        time.sleep(1)

print("OK ",name,"!  We're bringing you your custom meal!  Hold tight.")

time.sleep(3)

if mood == 1 and meal == 4 and pref == 7 :
    print("")
    print("To start off the day, you should have",random.choice(indVegBreakfast), "with a fresh cup offilter coffee to maximize your daily potential.")
    print("")

if mood == 1 and meal == 4 and pref == 8 :
    print("")
    print("Good morning!  Make some",random.choice(indNvegBreakfast), "with a cup of nice, hot chai to start the day on a high note!")
    print("")

if mood == 1 and meal == 5 and pref == 7  :
    print("")
    print("Try",random.choice(indLunchVegApp),"as an appetizer, and", random.choice(indLunchVegMain), "for your main course, with", random.choice(indLunchVegDes), ".")
    print("")

if mood == 1 and meal == 5 and pref == 8:
    print("")
    print("You should consider eating",random.choice(indLunchNvegApp),"as an appetizer, and", random.choice(indLunchNvegMain), "as your main course, with", random.choice(indLunchNvegDes), ".")
    print("")

if mood == 1 and meal == 6 and pref == 7 :
    print("")
    print("Treat yourself to a three-course meal!  Eat",random.choice(indDinnerVegApp),"as an appetizer, and then make", random.choice(indDinnerVegMain), "for your main course.  Finally, have some", random.choice(indDinnerVegDes), ".")
    print("")

if mood == 1 and meal == 6 and pref == 8 :
    print("")
    print("After a long day, you deserve a tasty dinner!  ",random.choice(indDinnerNvegApp)," would make a great starter.  Then make ", random.choice(indLunchVegMain), "as your main course.  And to end your day happily, treat yourself to ", random.choice(indLunchVegDes), ".")
    print("")


if mood == 2 and meal == 4 and pref == 7 :
    print("")
    print("To start off the day, you should have",random.choice(mexVegBreakfast), "with a refreshing Tamarind Agua Refresca to maximize your daily potential.")
    print("")

if mood == 2 and meal == 4 and pref == 8 :
    print("")
    print("Good morning!  Make some",random.choice(mexNvegBreakfast), "with a sweet Licuado de Mango to start the day on a high note!")
    print("")

if mood == 2 and meal == 5 and pref == 7 :
    print("")
    print("Try",random.choice(mexLunchVegApp),"as an appetizer, and", random.choice(mexLunchVegMain), "for your main course, with", random.choice(mexLunchVegDes) ".")
    print("")

if mood == 2 and meal == 5 and pref == 8 :
    print("")
    print("You should consider eating",random.choice(mexLunchNvegApp),"as an appetizer, and",random.choice(mexLunchNvegMain), "as your main course, with", random.choice(mexLunchNvegDes))
    print("")

if mood == 2 and meal == 6 and pref == 7 :
    print("")
    print("Treat yourself to a three-course meal!  Eat",random.choice(mexDinnerVegApp),"as an appetizer, and then make", random.choice(mexDinnerVegMain), "for your main course.  Finally, have some", random.choice(mexDinnerVegDes), ".")
    print("")

if mood == 2 and meal == 6 and pref == 8 :
    print("")
    print("After a long day, you deserve a tasty dinner!  ",random.choice(mexDinnerNvegApp)," would make a great starter.  Then make ", random.choice(mexLunchVegMain), "as your main course.  And to end your day happily, treat yourself to ", random.choice(mexLunchVegDes), ".")
    print("")


if mood == 3 and meal == 4 and pref == 7 :
    print("")
    print("To start off the day, you should have",random.choice(itVegBreakfast), "with a tangy glass of Creamy Limoncello daily potential.")
    print("")

if mood == 3 and meal == 4 and pref == 8 :
    print("")
    print("Good morning!  Make some",random.choice(itNvegBreakfast), "with some treacly Strawberry Bellini to start the day on a high note!")
    print("")

if mood == 3 and meal == 5 and pref == 7 :
    print("")
    print("Try",random.choice(itLunchVegApp),"as an appetizer, and", random.choice(itLunchVegMain), "for your main course, with", random.choice(itLunchVegDes), ".")
    print("")

if mood == 3 and meal == 5 and pref == 8 :
    print("")
    print("You should consider eating",random.choice(itLunchNvegApp)," as an appetizer, and",random.choice(itLunchNvegMain), "as your main course, with", random.choice(itLunchNvegDes))
    print("")

if mood == 3 and meal == 6 and pref == 7 :
    print("")
    print("Treat yourself to a three-course meal!  Eat",random.choice(itDinnerVegApp),"as an appetizer, and then make", random.choice(itDinnerVegMain), "for your main course.  Finally, have some", random.choice(itDinnerNvegDes), ".")
    print("")

if mood == 3 and meal == 6 and pref == 8 :
    print("")
    print("After a long day, you deserve a tasty dinner!",random.choice(itDinnerNvegApp),"would make a great starter.  Then make", random.choice(itDinnerNvegMain), "as your main course.  And to end your day happily, treat yourself to", random.choice(itDinnerNvegDes), ".")
    print("")

time.sleep(6)
indRest = ['https://www.google.com/maps/search/chaat+bhavan/@37.5284644,-122.077326,11z/data=!3m1!4b1','https://www.google.com/maps/search/sarvanna+bhavan/@37.5288443,-122.0773265,11z/data=!3m1!4b1','https://www.google.com/maps/search/peacock+indian+cuisine+/@37.5292243,-122.0773269,11z/data=!3m1!4b1']
mexRest = ['https://www.google.com/maps/search/chipotle/@37.5296042,-122.0773274,11z/data=!3m1!4b1','https://www.google.com/maps/search/on+the+border+/@37.5299841,-122.0773279,11z/data=!3m1!4b1','https://www.google.com/maps/search/el+pollo+loco/@37.530364,-122.0773283,11z/data=!3m1!4b1']
itRest = ['https://www.google.com/maps/search/olive+garden/@37.5303256,-122.4966629,9z/data=!3m1!4b1','https://www.google.com/maps/search/maggianos/@36.1394101,-115.390102,11z/data=!3m1!4b1','https://www.google.com/maps/search/sbarro/@37.5133399,-124.1756073,7z/data=!3m1!4b1']

print("")
print("You can find the food over here!")
time.sleep(2)
if mood == 1:
    webbrowser.open(random.choice(indRest))
if mood == 2:
    webbrowser.open(random.choice(mexRest))
if mood == 3:
    webbrowser.open(random.choice(itRest))
