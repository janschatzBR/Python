def elefantes(n):
    if n <= 0: return ""
    if n == 1: return "Um elefante incomoda muita gente "
    return (elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente " if n % 2 > 0 else "muito mais "))

def incomodam(n):
    if n <= 0: return ""
    if n == 1: return "incomodam "
    return ("incomodam " + incomodam(n - 1))



'''
def incomodam(n):
   if (type(n) == int):
      if n > 0:
         return "incomodam " + incomodam(n-1)
   return ""


def elefantes(n):
   if n <1:
       return str()
   elif n== 1:
       return str("Um elefante incomoda muita gente ")
   elif n== 2:
       return str("Um elefante incomoda muita gente " + "\n" + "2 elefantes incomodam incomodam muito mais" + "\n")
   else:
       frase1= str(n-1) + " elefantes " + str(incomodam(n-1)) + "muita gente"
       frase2= str(n) + " elefantes " + str(incomodam(n)) + "muito mais"       
       return elefantes(n-1) + str(frase1) +"\n"+ str(frase2) 

#print(elefantes(n))
'''
