import os
try:
    os.system("clear")
    arquivo = input("@ ")
    os.system("clear")
    print('(Ex: gmail.com, hotmail.com e etc)')
    email = input("tipo de email: ")
    os.system("clear")
    
    txtR = open(arquivo,"r").readlines()
    txtW = open("email.txt","w")

    print("executando...")
    for linha in txtR:
            linha2 = linha.rstrip('\n')
            l = linha2.lower()
            l2 = l.split()
            
            email2 = l2[0] + '.' + l2[1] + '@' + email
            txtW.write(email2)
            txtW.write("\n")
            
            email2 = l2[1] + '.' + l2[0] + '@' + email
            txtW.write(email2)
            txtW.write("\n")
            
            try:
                l3 = list(l2[1])
                email2 = l2[0] + '.' + l3[0] + l2[2] + '@' + email
                txtW.write(email2)
                txtW.write("\n")
            except:
                l3 = list(l2[1])
                email2 = l2[0] + '.' + l3[0] + '@' + email
                txtW.write(email2)
                txtW.write("\n")
            try:
                l3 = list(l2[2])
                email2 = l2[0] + '.' + l3[0] + l2[1] + '@' + email
                txtW.write(email2)
                txtW.write("\n")
            except:
                print("")

    os.system("clear")
    print("a ferramenta foi executado com sucesso!")

except:
    print("")
    print("/////////////////////////////////////////////////////")
    print("/// algo deu errado por favo renicie a ferramenta ///")
    print("/////////////////////////////////////////////////////")