import timeit

def my_function():
  for i in range(100):
   print(i)

time = timeit.timeit(my_function, number=2)  
print(f"Execution time: {time:.2f} seconds")
