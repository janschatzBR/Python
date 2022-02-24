def elefantes(n):

    if n == 1: return "Um elefante incomoda muita gente"
    
    ini = "{numero} {plural} muita gente\n{numero2} elefantes {incomodam} muito mais"

    for elefante in range(1, n):
        print(ini.format(
            numero = elefante,
            plural = "elefantes incomodam" if elefante > 1 else "elefante incomoda",
            numero2 = elefante + 1,
            incomodam=" ".join(["incomodam"] * (elefante + 1))
        ))
