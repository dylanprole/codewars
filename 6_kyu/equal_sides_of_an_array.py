# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    for N in enumerate(arr):
        if sum(arr[:N[0]]) == sum(arr[N[0] + 1:]):
            return N[0]
    return -1

test_arr = [1,2,3,4,3,2,1]

print(find_even_index(test_arr))

