def squaring_sorted_arrayes_2_pointers(arr):
    i = 0
    k = j = len(arr) - 1
    out = [0] * len(arr)
    while k>=0:
        if abs(arr[i]) < abs(arr[j]):
            out[k] = abs(arr[j]) * abs(arr[j])
            j-=1
        else:
            out[k] = abs(arr[i]) * abs(arr[i])
            i+=1
        k-=1
    return out

if __name__ == "__main__":
    tests = []

    test1 = {
        "inputs": [-2,-1,0,3,4],
        "output": [0,1,4,9,16]
    }


    test2 = {
        "inputs": [-4,-1,0,3,10],
        "output": [0,1,9,16,100]
    }

    test3 = {
        "inputs": [-7,-3,2,3,11],
        "output": [4,9,9,49,121]
    }

    test3 = {
        "inputs": [-7,-1,2,2,3,11],
        "output": [1,4,4,9,49,121]
    }

    test4 = {
        "inputs": [-7,-3,2,2,3,11],
        "output": [4,4,9,9,49,121]
    }


    test5 = {
        "inputs": [-7,-3,-2,2,2,3,11],
        "output": [4,4,4,9,9,49,121]
    }

    tests.append(test1)
    tests.append(test2)
    tests.append(test3)
    tests.append(test4)
    tests.append(test5)

    print(tests)

    for test in tests:
        print (f'input is              {test["inputs"]}')
        fn_output = squaring_sorted_arrayes_2_pointers(test["inputs"])
        print (f'expected output is    {test["output"]} and \nfn_output is          {fn_output} \n')
        assert  fn_output == test["output"]