# Library

books={"Wings of fire":45,"Discovery Of India":62,"The White Tiger":27,"Five Point Someone":100,"Three Mistakes Of My Life":108}
def display():
    print("The available books are: ")
    available=[i for i in books if books[i]>0]
    print(available)

def help():
    print(''' Choose the function:
            1. Display available books
            2. Issue a book
            3. Return a book
            Enter any other key for help menu
            Enter x to exit
            ''')

def issue():
    book=input("Enter the book name: ")
    if book in books and books[book]>0:
        books[book]-=1
        print(book,"issued successfully")
    else:
        print("The entered books is not available")

def ret():
    book=input("Enter the book name to return: ")
    books[book]+=1
    print(book,"returned successfully")


if __name__=='__main__':
    help()
    while True:
        key=str(input("Enter your choice: "))
        if key=='1':
            display()
        elif key=='2':
            issue()
        elif key=='3':
            ret()
        elif key in 'xX':
            print("Thank-you")
            break
        else:
            help()