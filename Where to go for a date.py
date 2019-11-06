#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Where to go for a date
print("Welcome to: Where to go for a date?")
print("Choose situation: \n1.First date\n2.Daily routine\n3.After an argument")
situation=int(input("Your situation is:"))
print ("   ")
print("Choose budget: \n1.Low 5€ \n2.Normal 15€ \n3.High 50€")
budget=int(input("Your budget is:"))
print ("   ")
print("Choose type of girl: \n1.Ambitious \n2.Nerd  \n3.Feminine")
girl=int(input("Your girl is:"))

def date():
    #Ambitious
    if situation==1 and budget==1 and girl==1:
        return ("You should take her to Museum with free enternance")
    if situation==1 and budget==2 and girl==1:
        return ("You should take her for a walk to nice park")
    if situation==1 and budget==3 and girl==1:
        return ("You should buy her flowers and apologize :(")
    if situation==2 and budget==1 and girl==1:
        return ("You should take her to Museum with free enternance")
    if situation==2 and budget==2 and girl==1:
        return ("You should take her for a walk to nice park")
    if situation==2 and budget==3 and girl==1:
        return ("You should buy her flowers and apologize :(")
    if situation==3 and budget==1 and girl==1:
        return ("You should take her to Museum with free enternance")
    if situation==3 and budget==2 and girl==1:
        return ("You should take her for a walk to nice park")
    if situation==3 and budget==3 and girl==1:
        return ("You should buy her flowers and apologize :(")



    #Nerd
    if situation==1 and budget==1 and girl==2:
        return ("You should take her to Museum with free enternance")
    if situation==1 and budget==2 and girl==2:
        return ("You should take her for a walk to nice park")
    if situation==1 and budget==3 and girl==2:
        return ("You should buy her flowers and apologize :(")
    if situation==2 and budget==1 and girl==2:
        return ("You should take her to Museum with free enternance")
    if situation==2 and budget==2 and girl==2:
        return ("You should take her for a walk to nice park")
    if situation==2 and budget==3 and girl==2:
        return ("You should buy her flowers and apologize :(")
    if situation==3 and budget==1 and girl==2:
        return ("You should take her to Museum with free enternance")
    if situation==3 and budget==2 and girl==2:
        return ("You should take her for a walk to nice park")
    if situation==3 and budget==3 and girl==2:
        return ("You should buy her flowers and apologize :(")

    #Nerd
    if situation==1 and budget==1 and girl==3:
        return ("You should take her to Museum with free enternance")
    if situation==1 and budget==2 and girl==3:
        return ("You should take her for a walk to nice park")
    if situation==1 and budget==3 and girl==3:
        return ("You should buy her flowers and apologize :(")
    if situation==2 and budget==1 and girl==3:
        return ("You should take her to Museum with free enternance")
    if situation==2 and budget==2 and girl==3:
        return ("You should take her for a walk to nice park")
    if situation==2 and budget==3 and girl==3:
        return ("You should buy her flowers and apologize :(")
    if situation==3 and budget==1 and girl==3:
        return ("You should take her to Museum with free enternance")
    if situation==3 and budget==2 and girl==3:
        return ("You should take her for a walk to nice park")
    if situation==3 and budget==3 and girl==3:
        return ("You should buy her flowers and apologize :(")

date()


# In[ ]:
