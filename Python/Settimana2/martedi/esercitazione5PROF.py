studenti = {}

while True:
    comando = input("Inserisci il nome Studente o 'Media' per conoscere le medie dei voti: ")
    if comando.lower() == "media":
    #media
        if len(studenti)== 0:
            print("Nessun alunno presente")
        else:
            break
    else:
    #aggiungi nomi e voti
        studenti[comando] = []
        Nvoti = input("Quanti voti vuoi inserire? ")
        for num in range(int(Nvoti)):
            voto = input("Inserisci il voto: ")
            studenti[comando].append(int(voto))
            studenti = {'Tommaso': [7, 10], 'Giovanni': [10, 6, 7]}
            print(studenti)

        for studente in studenti:
            if len(studenti[studente]) == 0:
                print(f"Nome: {studente}, Media: {0}")
        else:
            media = sum(studenti[studente]) /len(studenti[studente])
            print(f"Nome: {studente}, Media: {media}")