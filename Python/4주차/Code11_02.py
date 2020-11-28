import Code11_01

print("Enter a celsius value: ", end='')
celsius = float(input())
fahrenheit = Code11_01.convert_c_to_f(celsius)
print(f"That's {fahrenheit} degrees Fahrenheit.")