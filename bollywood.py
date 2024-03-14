def play_game():
    from movies import movies
    import random
    import os
    i = -1
    bollywood = ["B","o","l","l","y","w","o","o","d"]
    entered_character = []
    clear = lambda: os.system('cls')
    random_movie = random.choice(movies)
    movie_name_length = len(random_movie)
    list_of_movie_name = []
    list_of_movie_name[:0]= random_movie            
    movie_name_into_dashes = (movie_name_length * "_" )
    dashes_list = []
    dashes_list[:0] = movie_name_into_dashes
    if movie_name_length <= 10:
        hints = (movie_name_length//2)
    elif movie_name_length > 10:
        hints = (movie_name_length//3) - 1
    for x in range(movie_name_length):
        if list_of_movie_name[x] == " ":
            dashes_list[x] = list_of_movie_name[x]
    for x in range(hints):
        random_place_fill = random.randint(0,movie_name_length)
        dashes_list[random_place_fill - 1] = list_of_movie_name[random_place_fill - 1] 
    while True:
        clear()
        bollywood_list_string = ""
        for x in bollywood:
            bollywood_list_string += x
        print(bollywood_list_string)
        print("\r")
        print("Characters you've enterd: {}".format(entered_character))
        print("\r")
        dashes_list_to_string = ""
        for x in dashes_list:
            dashes_list_to_string += x
        print(dashes_list_to_string,"\n")
        if i == 8:
                print("You Lost!!!")
                print("\r")
                print("The movie was {}".format(random_movie).title())
                play_again = input(("Do you want to play again?\nPress (y) for Yes and (n) for No\n"))
                print("\r")
                if play_again == "y":
                    play_game()
                else:
                    clear()
                    break
        if dashes_list == list_of_movie_name:
                print("You Won!!!")
                play_again = input(("Do you want to play again?\nPress (y) for Yes and (n) for No\n"))             
                if play_again == "y":
                    play_game()
                else:
                    clear()
                    break
        guess = input("Enter your guess: ").lower()
        print("\r")
        entered_character += guess
        if guess in list_of_movie_name:
            for x in range(0,movie_name_length):
                if list_of_movie_name[x] == guess:
                        dashes_list[x] = list_of_movie_name[x]
        elif guess not in list_of_movie_name:
            i+=1
            x = bollywood[i]
            x = (''.join([u'\u0336{}'.format(x)]))
            bollywood[i] = x
play_game()      
