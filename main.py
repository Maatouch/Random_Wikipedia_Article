import wikipedia
import webbrowser


user_input = "No"
wikipedia.set_rate_limiting(True)


while user_input =="No":

    title = wikipedia.random(pages=1)
    #generate a random article title
    page = wikipedia.page(title)
    #accessing the article page

    print(title + "\n" + wikipedia.summary(title))

    user_input = input("Do you want to read the full article? Yes/No \n")

    if user_input == "Yes":
        webbrowser.open(page.url, new=2)
        #this open up the article page in browser
    elif user_input == "No":
        continue

    while not (user_input =="Yes") | (user_input =="No") :
        user_input = input("Do you want to read the full article? Yes/No \n")
        #making sure that the user input is Yes or No


