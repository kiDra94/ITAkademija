import multiprocessing
  
def calculate_cube(num): 
    print("Cube: {}".format(num * num * num)) 
  
def calculate_square(num): 
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    process1 = multiprocessing.Process(target=calculate_square, args=(10,))

    process2 = multiprocessing.Process(target=calculate_cube, args=(10,)) 
    process1.start() 
    process2.start() 
  
    process1.join() 
    process2.join() 

    print("Done!")

