import importlib
games_mod = importlib.import_module("games") # import file games.py.

print(dir(games_mod)) #check the contents of the file , GameClass is the first element, the name of the class.

game = "GameClass" # save that name for future use

game_class = getattr(games_mod,game) #save the element with a name GameClass from file games.py
game_obj = game_class()  # instantiate class with name GameClass

print(dir(game_obj)) # show me what's inside class GameClass, there are two user defined methods

start_method = "start" # save first method
hit_method = "hit" # save second method

method = getattr(game_obj,start_method)  # get method
method() #start method
method = getattr(game_obj,hit_method)  #get method
game_obj.hit(10) #start method 3 times
game_obj.hit(20)
game_obj.hit(30) 

