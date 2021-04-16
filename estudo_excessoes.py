# estudo_excessoes

try:
    print(a)

except:
    print('erro')

# ###############

try:
    print(a)

except NameError as erro:
    print('Error:', erro)