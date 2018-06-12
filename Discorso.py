
p = "PYTHON: "
y = "You: "
print (p + "Ciao, il mio nome e' Python e sono tipo Dio, ma a differenza del vero Dio io faccio tutto quello che mi dici di fare devi sapere solo come parlarmi :) \n        Tu invece come ti chiami?")
Nome = input(y)
print (p + "Bene..., pero' " + Nome + ' non mi piace come nome, posso chiamarti Gervaso?')
Risposta = input(y)
if Risposta == "No" or Risposta == "no" :
    print (y + "Ma che nome e' Gervaso, piuttosto chiamami " )
    Soprannome = input('     ')
    print (p + "Mi piace da oggi sarai il mio " + Soprannome + " personale")
    print (y + "Vabene")
    print (p + "Perfetto " + Soprannome + ", ora cosa vuoi fare?")
elif Risposta == "Si" or Risposta == "si" :
    print (p + "Perfetto Gervaso, ora cosa vuoi fare?")
else:
    print ("RISPOSTA NON VALIDA, RISPONDI SOLO SI O NO")