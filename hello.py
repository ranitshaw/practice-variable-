def hello(to = "Gamer"):  #it's working AS default value if the user didn't enter their name it will print hello Gamer
    # soja kotha hello ta k akta role deya hoche .

    print("hello,", to)   # akhane jeta thakbe double collone er modhe seta to role  function er age asbe like jodi comma no deya hoi okhane o comma porbe na
    

hello()
name = input("what's your name? ").strip().capitalize().title()

hello(name)