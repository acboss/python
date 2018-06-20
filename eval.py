inserisci = "Inserire l'espressione matematica (premere invio e scrivere 'Fatto'): "
espressione_da_convertire_in_str = input(inserisci) 

Fatto = input()

def eval_ciclo(espressioneDaConvertireInStr, fatto):
    if fatto == "fatto" or fatto == "Fatto" or fatto == "FATTO":
        print (eval ('espressioneDaConvertireInStr'))

eval_ciclo(espressione_da_convertire_in_str, Fatto)