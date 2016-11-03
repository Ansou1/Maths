# !/usr/bin/python
# -*- encoding:utf-8 -*-

def langage(lang):

    #francais
    fr = []
    fr.append("La taille de la population doit etre plus grande que la taille de l'echantillon.\n")
    fr.append("taille de la population :\t\t%d\n")
    fr.append("taille de l'echantillon :\t\t%d\n")
    fr.append("resultat du sondage :\t\t%0.2f%%\n")
    fr.append("variance estimee :\t\t%f\n")
    fr.append("intervalle de confiance a 95%% :\t[%0.2f%% ; %0.2f%%]\n")
    fr.append("intervalle de confiance a 99%% :\t[%0.2f%% ; %0.2f%%]\n")

    #allemand
    de = []
    de.append("Die Grope der Bevolkerung muss groper als die Stichprobengrope sein.\n")
    de.append("Grope der Bevolkerung :\t\t%d\n")
    de.append("Grope der Probe :\t\t%d\n")
    de.append("Ergebnisse der Umfrage :\t\t%0.2f%%\n")
    de.append("Geschatzte Varianz :\t\t%f\n")
    de.append("Konfidenzintervall 95%% :\t\t[%0.2f%% ; %0.2f%%]\n")
    de.append("Konfidenzintervall 99%% :\t\t[%0.2f%% ; %0.2f%%]\n")

    #anglais
    en = []
    en.append("The size of population must be greater than the size sample.\n")
    en.append("Size of population :\t\t%d\n")
    en.append("Size of sample :\t\t%d\n")
    en.append("result of the survey :\t\t%0.2f%%\n")
    en.append("estimated variance :\t\t%f\n")
    en.append("confidence interval at 95%% :\t\t[%0.2f%% ; %0.2f%%]\n")
    en.append("confidence interval  at 99%% :\t\t[%0.2f%% ; %0.2f%%]\n")

    #espagnaol
    sp = []
    sp.append("El tamano de la poblacion debe ser mayor que el tamano de la muestra.\n")
    sp.append("tamano de la poblacion :\t\t%d\n")
    sp.append("tamano de la muestra :\t\t%d\n")
    sp.append("resultados de la encuesta :\t\t%0.2f%%\n")
    sp.append("varianza estimada :\t\t%f\n")
    sp.append("intervalo de confianza 95%% :\t\t[%0.2f%% ; %0.2f%%]\n")
    sp.append("intervalo de confianza 99%% :\t\t[%0.2f%% ; %0.2f%%]\n")

    #italien
    it = []
    it.append("La dimensione della popolazione deve essere maggiore della dimensione del campione.\n")
    it.append("dimensione della popolazione :\t%d\n")
    it.append("dimensione del campione :\t\t%d\n")
    it.append("risultati del sondaggio :\t\t%0.2f%%\n")
    it.append("varianza stimata :\t\t%f\n")
    it.append("intervallo di confidenza 95%% :\t\t[%0.2f%% ; %0.2f%%]\n")
    it.append("intervallo di confidenza 99%% :\t\t[%0.2f%% ; %0.2f%%]\n")

    lang.append(fr)
    lang.append(de)
    lang.append(en)
    lang.append(sp)
    lang.append(it)

    return lang
