#!/usr/bin/python3

def main():
    mylist = ["bert", 55, "juniper", "cisco", ["bigip", "meraki", "dell"]]
    print(mylist[2])

    print("my primary network providers are " + mylist[2] + " " + mylist[3], ".")

    print(f"my primary network providers are {mylist[2]} {mylist[3]}.")
    print(mylist[4][1])


main()

