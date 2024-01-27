class Calculator:
    def __init__(self) :
        pass
    def add(self,n1,n2):
        return n1+n2 
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        if n2!=0:
            return n1/n2
        else:
            return "Error: Division by zero"
        
def main():
    calc=Calculator()

    while True:#to continuously display the menu and prompt the user for input.
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")  
        print("4. Division")
        print("5. Exit")


        choice = int(input("Enter your choice (1/2/3/4/5): "))


        if choice==1:
            print("choice=Addition")
            n1,n2=map(int,input("Enter number 1 and number 2\n").split())
            
            answer=calc.add(n1,n2)
            print("Answer=",answer)

        elif choice==2:
            print("choice=Substraction")
            n1,n2=map(int,input("Enter number 1 and number 2\n").split())
            answer=calc.sub(n1,n2)
            print("Answer=",answer)

        elif choice==3:
            print("choice=Multiplication")
            n1,n2=map(int,input("Enter number 1 and number 2\n").split())
            answer=calc.mul(n1,n2)
            print("Answer=",answer)

        elif choice==4:
            print("choice=Division")
            n1,n2=map(int,input("Enter number 1 and number 2\n").split())
            answer=calc.div(n1,n2)
            print("Answer=",answer)
            
        elif choice==5:
            print("choice=Exit")
            print("Shutting Down..")
            break

        else:
            print("Invalid entry. Please look in the menu and try again")


if __name__=="__main__":
    main()
    