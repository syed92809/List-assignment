product1=[2,4,7,8]
product2=[6,5,9,1]


def calculate(i_1,i_2):
    result=i_1*i_2
    return result



for pr1 in product1:
    for pr2 in product2:
        checkCond=calculate(pr1,pr2)
        if checkCond==20:
            continue
        elif checkCond==18:
            break
        else:
            print(checkCond)

    print("------")

