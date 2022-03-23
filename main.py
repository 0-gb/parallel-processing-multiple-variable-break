import multiprocessing as mp

correct_code = 915232
chunk_size = 200
N_proc = 8


def check_code_correct(original_code, tested_code):
    return original_code == tested_code


def format_and_check(the_input):
    el_0, el_1, el_2, el_3, el_4, el_5, searched_code= the_input
    number_string = el_0 + el_1 + el_2 + el_3 + el_4 + el_5
    #print(number_string)
    return check_code_correct(searched_code, int(number_string)), number_string


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
