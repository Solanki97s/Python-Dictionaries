def my_personal_information():
    name=input("Enter your name-")
    age=int(input("Enter your age-"))
    gender=input("Enter your gender-")
    my_information={
        'Name':name,
        'Age' :age,
        'Gender' : gender
    }

    return my_information
personal_info=my_personal_information()
print(personal_info)



"""
def info(name,age,gender):
    d1={}
    d1['Name']=name
    d1['Age']=age
    d1['Gender']=gender
    print(f"info={d1}")
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
gender=input("Enter your gender:-")
info(name,age,gender)
"""











