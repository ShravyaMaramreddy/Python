#duplicates count in the array
arr = [2,3,3,2,5,1]
count = 0
for num in arr:
    if arr.count(num) > 1:
        count += 1
print(count)