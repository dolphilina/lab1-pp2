class Filter_prime():
    
    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return False
        return True   
    """
    isPrime(self, num): Метод, который проверяет, 
    является ли число простым. Он возвращает True, 
    если число простое, и False в противном случае. 
    Для проверки простоты числа используется 
    метод перебора делителей.
    """
    def filter_primes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)
    """
    filter_primes(self, listofnums): Метод, который фильтрует 
    список чисел, оставляя только простые числа. 
    Он использует функцию filter(), 
    передавая в неё лямбда-функцию, 
    которая вызывает isPrime() для каждого элемента списка.
    """
prime_filter = Filter_prime() #Создаётся объект prime_filter типа Filter_prime.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filter_primes(nums))
"""
Применяется метод filter_primes() объекта prime_filter 
к списку nums. Он фильтрует список, 
оставляя только простые числа, 
и результат сохраняется в переменной prime_numbers.
"""
print(prime_numbers) #[2, 3, 5, 7]