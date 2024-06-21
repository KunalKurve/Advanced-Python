def divide(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print(e)
        raise e
    

for i in range(3):
    try:
        x=int(input("Enter num: "))
        print(x+10)
        a=23
        b=0
        ans=divide(a,b)
        print(ans)
        break
    
    except ValueError:
        print("pls enter number and not character")
    
    except (ZeroDivisionError,KeyError,IndexError) as e:
        print("error occured",e)
    
    except Exception as e:
        print("error occured",e)
    
    else:
        print("test")
    
    finally:
        print("in finally block")