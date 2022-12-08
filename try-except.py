# try:
#     x = int(input("Introduceti un numar: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("Puteti introduce doar numere! ")

# x = 0
# while x == 0:
#     try:
#         x = int(input("Introduceti un numar: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Introduceti doar numere! : ")

# ---------------------------------------------------------------------------

try:
    x = 5 / 1
    x = int(input())
except ZeroDivisionError:
    print("Impartire la 0! ")
except ValueError:
    print("Ati introdus ceva gresit! ")
else:
    print("else")
finally:
    print("Finally")
