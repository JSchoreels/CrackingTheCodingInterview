def count_eval(repr, expected):
    memo = {}
    def count_eval_rec(repr, expected):
        if len(repr) == 0:
            return 0
        if len(repr) == 1:
            return 1 if (repr == ('1' if expected else '0')) else 0
        if repr + str(expected) in memo:
            return memo[repr + str(expected)]
        total = 0
        for i in range(1, len(repr), 2):
            current_operator = repr[i]
            left_side = repr[0:i]
            right_side = repr[i+1:]
            if current_operator == '&':
                if expected:
                    total += count_eval_rec(left_side, True) * count_eval_rec(right_side, True)
                else:
                    total += count_eval_rec(left_side, False) * count_eval_rec(right_side, True) \
                           + count_eval_rec(left_side, True) * count_eval_rec(right_side, False) \
                           + count_eval_rec(left_side, False) * count_eval_rec(right_side, False)
            elif current_operator == '|':
                if expected:
                    total += count_eval_rec(left_side, False) * count_eval_rec(right_side, True) \
                           + count_eval_rec(left_side, True) * count_eval_rec(right_side, False) \
                           + count_eval_rec(left_side, True) * count_eval_rec(right_side, True)
                else:
                    total += count_eval_rec(left_side, False) * count_eval_rec(right_side, False)
            elif current_operator == '^':
                if expected:
                    total += count_eval_rec(left_side, False) * count_eval_rec(right_side, True) \
                           + count_eval_rec(left_side, True) * count_eval_rec(right_side, False)
                else:
                    total += count_eval_rec(left_side, False) * count_eval_rec(right_side, False) \
                           + count_eval_rec(left_side, True) * count_eval_rec(right_side, True)
            else:
                raise ValueError("Unexpected Operator")
        print(f"For repr:{repr:20} with expected:{expected}, total:{total}")
        memo[repr+str(expected)] = total
        return total
    return count_eval_rec(repr, expected)


test1 = "1^0|0|1"
test2 = "0&0&0&1^1|0"

print(count_eval(test1, False))
print(count_eval(test1, True))
print(count_eval(test2, False))
print(count_eval(test2, True))