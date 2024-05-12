import cc
import pp
import time

start_time = time.time()
prime1 = pp.factorial(5)
end_time = time.time()

print(prime1)
print(end_time - start_time)

start_time = time.time()
prime2 = cc.factorial_cython(5)
end_time = time.time()

print(prime2)
print(end_time - start_time)