grille=['','','','','','','','','']


#------------------symbole-----------------#

symbj= str(input("Joueur 1 choisissez votre symbole (X ou O): "))                 #Le joueur 1 choisi son symbole
while symbj!='O' and symbj!='X':
    symbj=str(input("Joueur 1 choisissez un des symboles proposés (X ou O): "))

if symbj=='X':
    print("Joueur 1, Vous avez choisi 'X' et Joueur 2, Vous jouerez avce 'O'")    

else :
    print("Vous avez choisi 'O' et Joueur 2, Vous jouerez avce 'X'")
        


def afficher_grille(grille):                                                      #C'est la construction de la grille 3x3 avec les indices 0, 1 et 2.
   #pour les colonnes                                                           # Ces indices permetent au joueur de se retrouver dans la grille.
    print("     [0]  [1]  [2]")
    print("     -------------")

   #pour la ligne 0
    print("[0]",  end='')
    for i in range(3):
        print("  | "+str(grille[i]), end='')
    print("  |")

    print("     -------------")
   #pour la ligne 1
    print("[1]", end='')
    for i in range(3):
        print("  | "+str(grille[i+3]), end='')
    print("  |")

    print("     -------------")
   #pour la ligne 2
    print("[2]", end='')
    for i in range(3):
        print("  | "+str(grille[i+6]), end='')
    print("  |")
    print("     -------------")

    

#--------------coup_du_debut-----------------#:
coup1=0
while coup1!='Oui' and coup1!='Non':
    coup1=str(input("Joueur 1, Voulez-vous joué le premier ?,(Répondre:Oui ou Non): "))      #Le joueur 1 choisit s'il veut commencer.
if coup1=='Oui':
    print("Joueur 1, Vous commencez la partie")
else :
    print("Joueur 2, Vous commencez la partie")



def fin_de_partie():
    v=3
    global a
    global n
    #les lignes                                                                     #cette fonction permet de déterminer une grille finale.
    if (grille[0]==grille[1]==grille[2]!=""):
        if grille[0]=='X':
            v=1
        else:
            v=2
    if (grille[3]==grille[4]==grille[5]!=""):                                      #soit un des joueurs a réussi à gagner.
        if grille[3]=='X':
            v=1
        else:
            v=2
    if (grille[6]==grille[7]==grille[8]!=""):                                      
        if grille[6]=='X':
            v=1
        else:
            v=2
   #les colonnes
    if (grille[0]==grille[3]==grille[6]!=""):
        if grille[0]=='X':
            v=1
        else:
            v=2
    if (grille[1]==grille[4]==grille[7]!=""):
        if grille[1]=='X':
            v=1
        else:
            v=2
    if (grille[2]==grille[5]==grille[8]!=""):
        if grille[2]=='X':
            v=1
        else:
            v=2
   #les diagonales
    if (grille[0]==grille[4]==grille[8]!=""):
        if grille[0]=='X':
            v=1
        else:
            v=2
    if (grille[2]==grille[4]==grille[6]!=""):
        if grille[2]=='X':
            v=1
        else:
            v=2
    
            
    if v==1:
        print("Le joueur doté du symbole X à gagnée.")
        return 1
       
        
    elif v==2:
        print("Le joueur doté du symbole X à gagnée.")
        return 1
       
    else :
        if grille[0]!="" and grille[1]!="" and grille[2]!="" and grille[3]!="" and grille[4]!="" and grille[5]!="" and grille[6]!="" and grille[7]!="" and grille[8]!="":
            print("Match nul")                                                  #soit la grille est remplie est aucun des joueurs n'a gagnés: match nul
            return 1
            



def tour_du_joueur1():
    global symbj
                   #le joueur choisi sa case
    print("C'est au tour du joueur 1")
    colonne=3
    while colonne!='0' and colonne!='1' and colonne!='2':
            colonne=input("Choisissez la colonne(0,1 ou 2) : ")                                #cette fonction demande au joueur 1 quelle case a-t-il choisi

    ligne=3
    while ligne!='0' and ligne!='1' and ligne!='2':
        ligne=input("Choisissez la ligne(0,1 ou 2) : ")

                   #l'ordinateur place le symbole choisi dans la case
    print("Vous avez joué la case","(",colonne,",",ligne,")")
    while grille[int(colonne)+int(ligne)*3]!='':
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=3
        while colonne!='0' and colonne!='1' and colonne!='2':
                colonne=input("Choisissez la colonne(0,1 ou 2) : ")

        ligne=3
        while ligne!='0' and ligne!='1' and ligne!='2':
            ligne=input("Choisissez la ligne(0,1 ou 2) : ")

        print("Vous avez joué la case","(",colonne,",",ligne,")")

                    #affichage du coup joué
    if symbj=="X":
        grille[int(colonne)+int(ligne)*3]="X"
        afficher_grille(grille)
    else:
        grille[int(colonne)+int(ligne)*3]="O"
        afficher_grille(grille)

    
   


def tour_du_joueur2():
    global symbj
    print("C'est au tour du joueur 2")
                   #le joueur choisi sa case
    colonne=3
    while colonne!='0' and colonne!='1' and colonne!='2':                                      #cette fonction demande au joueur 2 quelle case a-t-il choisi
            colonne=input("Choisissez la colonne(0,1 ou 2) : ")

    ligne=3
    while ligne!='0' and ligne!='1' and ligne!='2':
        ligne=input("Choisissez la ligne(0,1 ou 2) : ")

                   #l'ordinateur place le symbole choisi dans la case
    print("Vous avez joué la case","(",colonne,",",ligne,")")
    while grille[int(colonne)+int(ligne)*3]!='':
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=3
        while colonne!='0' and colonne!='1' and colonne!='2':
                colonne=input("Choisissez la colonne(0,1 ou 2) : ")

        ligne=3
        while ligne!='0' and ligne!='1' and ligne!='2':
            ligne=input("Choisissez la ligne(0,1 ou 2) : ")
            
        print("Vous avez joué la case","(",colonne,",",ligne,")")

                    #affichage du coup joué
    if symbj=="X":
        grille[int(colonne)+int(ligne)*3]="O"
        afficher_grille(grille)
    else:
        grille[int(colonne)+int(ligne)*3]="X"
        afficher_grille(grille)

    
   

end=0
a=0
n=0
while end==0:
    if coup1=='Oui':
        if n==a:
            tour_du_joueur1()                          # Cette partie du programme permet de passer d'un tour à l'autre des joueurs
            n=n+1
        else:
            tour_du_joueur2()                        # en prenant en considération la fin d'une partie( victoire ou match nul)
            a=a+1
    if coup1=='Non':
        if a==n:
            tour_du_joueur2()
            a=a+1
        else:
            tour_du_joueur1()
            n=n+1
    if fin_de_partie():
        end=1
            
    
            
            
            
        
    


        
        
        
       
    
