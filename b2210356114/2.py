def email_checker(a):
    if '@' in a:
        if '.' in a:
            print("This email is valid")
        else:
            print("This email is not valid")  
    else:
        print("this email is not valid")

a = input("write your e-mail: ")
email_checker(a)

