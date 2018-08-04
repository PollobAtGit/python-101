def get_input_covert_to_int():
    try:
        val = int(input())
    except ValueError:
        return "couldn't convert string to int"

    # val is defined here. not block scoped
    return val

def i_catch_all():
    try:
        float(input())

    # same operation for multiple exception(s). Use tuple
    except (ValueError, TypeError, NameError):
        print("conversion failed")
        pass
        
class User_Defined_Exception(Exception):
    pass

class UDE_One(User_Defined_Exception):
    pass

class UDE_Two(UDE_One):
    pass

class UDE_Three(UDE_Two):
    pass
    

def raise_exception():
    try:
        choice = int(input())

        if choice == 0: raise User_Defined_Exception()
        if choice == 1: raise UDE_One()
        if choice == 2: raise UDE_Two()
        if choice == 3: raise UDE_Three()
        else: raise Exception()

    except UDE_One: print('1')
    except UDE_Two: print('2')
    except UDE_Three: print('3')
    except User_Defined_Exception as err: print('0')
    except: print("match not found")

def raise_exception_other():
    try:
        choice = int(input())

        if choice == 0: raise User_Defined_Exception()
        if choice == 1: raise UDE_One()
        if choice == 2: raise UDE_Two()
        if choice == 3: raise UDE_Three()
        else: raise Exception()

    except UDE_Three: print('3')
    except UDE_Two: print('2')
    except UDE_One: print('1')
    except User_Defined_Exception as err: print('0')
    except: print("match not found")

def dynamic_obj_creation():

    for e_cls in [User_Defined_Exception, UDE_One, UDE_Two, UDE_Three]:
        try:
            raise e_cls()
        except User_Defined_Exception as err:
            print(type(err))
            print(isinstance(err, User_Defined_Exception))
            print(isinstance(err, UDE_One))
            # print(typeof(err))
        

class A:
    name = "A"

class B:
    b_name = "B"

class C:
    name = "C"

def create_obs_one_by_one():
    for cls in [A, B, C]:
        try:
            print(cls().name)
        except AttributeError as err:
            print(err)
        finally:
            print('cleaned up everything')
            

# raise_exception()
# raise_exception_other()
# dynamic_obj_creation()
create_obs_one_by_one()
