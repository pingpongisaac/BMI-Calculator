def round_ans(val):
    var_rounded = "{:.1f}".format(val)
    return var_rounded


test1 = 25.333
test1 = round_ans(test1)

test2 = 25.5
test2 = round_ans(test2)

test3 = 25.75
test3 = round_ans(test3)

print(test1, test2, test3)
