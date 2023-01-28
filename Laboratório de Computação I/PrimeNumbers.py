def PrimeNumbers():
    index = 2
    maximum = 100000
    primes = []

    while index <= maximum :
  
      if (index % 2 != 0 and index % 3 != 0 and index % 5 != 0 and index % 7 != 0) or index == 2 or index == 3 or index == 5 or index == 7:
          primes.append(index)

      index = index + 1

    x = 0
    y = len(primes) - 1

    while x < len(primes) - 1 :
        while y >= 0 :
            if primes[y] != primes[x] and primes[y] % primes[x] == 0 :
                primes.remove(primes[y])
        
            y = y - 1
    
        y = len(primes) - 1
        x = x + 1


    for x in primes :
        print(x)

