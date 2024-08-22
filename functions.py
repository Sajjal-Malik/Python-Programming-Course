def cal_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total



tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

toms_total = cal_total(tom_exp_list)
joe_total = cal_total(joe_exp_list)

print("Tom's total expense is:",toms_total)
print("Joe's total expense is:",joe_total)




def sum(a, b):
    '''
    This is the docstring or documentation string
    that defines about this particular function 
    what it does and what is takes as argument
    '''
    ans = a + b
    return ans

n = sum(7,8)

print("Total of sum func is: ", n)