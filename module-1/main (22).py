#Christian Thompson
6/14/2026
#Module 1 Assignment On the Wall

def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall.")
        print(f"{bottles} bottles of beer.")
        print("Take one down, pass it around.")
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall.\n")

    print("1 bottle of beer on the wall.")
    print("1 bottle of beer.")
    print("Take one down, pass it around.")
    print("No more bottles of beer on the wall.\n")


def main():
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown(bottles)
    print("Time to buy more beer!")


main()


