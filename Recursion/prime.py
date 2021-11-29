def prime(num,i):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else:
        i = i+1
        print(num,i)
        if (num%i == 0):
            return 0
        else:
            if i < num-1:
              return prime(num,i)
            else:
              return 1
      
  
print(prime(5, 2))
