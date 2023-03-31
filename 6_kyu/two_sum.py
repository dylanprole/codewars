def two_sum(numbers, target):
    for base in range(len(numbers)):
        for add in range(len(numbers)):
            if base != add:
                if numbers[base] + numbers[add] == target:
                    return [base, add]
			    

print(two_sum([1,2,3], 4))