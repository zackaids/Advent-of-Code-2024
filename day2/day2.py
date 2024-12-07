with open("./day2/test.txt", "r") as file:
    for line in file:
        
        num = line.strip()
        nums = [int(i) for i in num.split()]
        
        for i in range(len(nums)):
            difference = abs(nums[i+1]-nums[i])
            if difference <= 1:
                continue
            if difference >= 3:
                continue
            
