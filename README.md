# Tutorial: Parallel processing, mutiple variables and break statement
This example shows how to use Python's parallel processing with multivariate functions and a break condition. In the example we pretend to be solving a 6 digit code. The search for the code is parallelized and breaks once the correct code is found. 

## Walkthrough
As commonly, we first import the relevant libraries. It turns out that this simple example requires only one, the multiprocessing library which we import as follows:
``` python
import multiprocessing as mp
```

Afterwards, we define the relevant parameters of the example:

``` python
correct_code = 915232
chunk_size = 200
n_proc = 8
```

In the block of code above, ```correct_code``` is the code that we are looking for, ```chunk_size``` (approximately) defines the size of the pieces that the data is split into and ```n_proc``` is the number of processes used (not the same as the number of processors). You can play around with the parameters ```chunk_size``` and ```n_proc``` and see that it changes how fast the code is running. 

We then define the method that checks if a certain code is correct. This method should generally be something much more complext and case specific. Here in this tutorial let's just say that we simply check if a ceratin integer is equal to the correct code provided to this method. 

``` python
def check_code_correct(original_code, tested_code):
    return original_code == tested_code
```

The other custom method we will use is one that takes a string input, performs the check and returns whether or not the input is as required. While the method can only take a single input, we can see that we can get other variables in by unwrapping them from a list. 

``` python
def format_and_check(the_input):
    el_0, el_1, el_2, el_3, el_4, el_5, searched_code= the_input
    number_string = el_0 + el_1 + el_2 + el_3 + el_4 + el_5
    #print(number_string)
    return check_code_correct(searched_code, int(number_string)), number_string
```

What remains is to initialize and run the process and then check which code returned "True" by the checking method. When the code returns "True" we break so as to stop any other needless computations. If you uncomment the print statement in the ```format_and_check``` method of the inputs you will see that this does not generally happen af the very first instance that the relevant for loop created the correct combination, but that the process overshoots and checks a few extra samples. This is because the call to the breaking procedure has not yet finished while other parallel processes are still running.


``` python
if __name__ == '__main__':
    p = mp.Pool(N_proc)
    for result in p.imap_unordered(format_and_check, [(str(i), str(j), str(k), str(l), str(m), str(n), correct_code)
                                                      for i in range(10)
                                                      for j in range(10)
                                                      for k in range(10)
                                                      for l in range(10)
                                                      for m in range(10)
                                                      for n in range(10)], chunksize=chunk_size):
        if result[0]:
            print('Found code: {}'.format(result[1]))
            p.terminate()
            break
``` 
The ``` if __name__ == '__main__ ```  ensures that the program will only run if the code is called direclty. Notice that the nested for loops are used to construct a nested list where each element contains the defacto multivariate input. The generated numbers are first converted to strings so as to try and immitate the fact that a more general code might have been searched for, not just numbers. The first variable that ```format_and_check``` returns is a Boolean that tells us whethera ceratin code was correct or not. When that variable is True we finish and print the found code. 
