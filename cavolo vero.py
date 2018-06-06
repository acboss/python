Nome = "Andrea"
Cognome = "Ceccarelli"
Soprannome = "Cecca"
Eta = 17
Risposta = "No"
p = "PYTHON: "
y = "You: "
print (p + "Ciao, il mio nome e' Python e sono tipo Dio, ma a differenza del vero Dio io faccio tutto quello che mi dici di fare devi sapere solo coome parlarmi :) \nTu invece come ti chiami?")
print (y + Nome)
print (p + "Bene..., pero' " + Nome + ' non mi piace come nome, posso chiamarti Gervaso?')
if Risposta == "No" or Risposta == "no" :
    print (y + "No ma che razza di nome e' Gervaso, piuttosto chiamami " + Soprannome)
    print (p + "Mi piace da oggi sarai il mio " + Soprannome + " personale")
    print (y + "Vabene")
    print (p + "Perfetto " + Soprannome + ", ora cosa vuoi fare?")
if Risposta == "Si" or Risposta = "si" :
    print (p + "Perfetto Gervaso, ora cosa vuoi fare?")
else:
    print ("Risposta non valida, rispondi solo si o no")