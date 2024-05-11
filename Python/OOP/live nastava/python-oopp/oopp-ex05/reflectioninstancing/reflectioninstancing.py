import importlib
mod = "games"
game = "GameClass"
start_method = "start"
hit_method = "hit"
games_mod = importlib.import_module("games")
game_class = getattr(games_mod,game) 
game_obj = game_class() 
method = getattr(game_obj,start_method) 
method()
method = getattr(game_obj,hit_method) 
game_obj.hit(10)
game_obj.hit(20)
game_obj.hit(30) 