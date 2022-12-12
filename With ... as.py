try:
    # file = open ('text.txt', 'r')
    # file.read()
    # file.close()
    with open('text.txt', 'r', encoding='utf-8') as file:
        file.read()
except FileNotFoundError:
    print("File does not exist")

# with and ass este un meneger ideal de a lucra cu file-urile


