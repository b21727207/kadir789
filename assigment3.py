import time
from threading import Thread
import random
with open("correct_words.txt","r",encoding="utf-8")as file:
    liste=[]
    for satır in file:
        liste.append(satır)
liste1=[]
def ayırma():
    for satır in liste:
        liste_elemanları=satır.split(":")
        liste1.append(liste_elemanları)
ayırma()
liste2=[]
for i in range(len(liste1)):
    liste2.append(liste1[i][1])
with open("liste2.txt","w",encoding="utf-8")as file1:
    for i in liste2:
        file1.writelines(i)
liste3=[]
def ayırma2():
    for satır in liste2:
        liste2_elemanları=satır.split(",")
        liste3.append(liste2_elemanları)
ayırma2()
with open("letter_values.txt","r",encoding="utf-8")as file2:
    liste4=[]
    for satır in file2:
        liste4.append(satır)
liste5=[]
def ayırma3():
    for satır in liste4:
        liste1_elemanları=satır.split(":")
        liste5.append(liste1_elemanları)
ayırma3()
dict_2={}
dict_2[liste5[0][0]]=int(liste5[0][1])
dict_2[liste5[1][0]]=int(liste5[1][1])
dict_2[liste5[2][0]]=int(liste5[2][1])
dict_2[liste5[3][0]]=int(liste5[3][1])
dict_2[liste5[4][0]]=int(liste5[4][1])
dict_2[liste5[5][0]]=int(liste5[5][1])
dict_2[liste5[6][0]]=int(liste5[6][1])
dict_2[liste5[7][0]]=int(liste5[7][1])
dict_2[liste5[8][0]]=int(liste5[8][1])
dict_2[liste5[9][0]]=int(liste5[9][1])
dict_2[liste5[10][0]]=int(liste5[10][1])
dict_2[liste5[11][0]]=int(liste5[11][1])
dict_2[liste5[12][0]]=int(liste5[12][1])
dict_2[liste5[13][0]]=int(liste5[13][1])
dict_2[liste5[14][0]]=int(liste5[14][1])
dict_2[liste5[15][0]]=int(liste5[15][1])
dict_2[liste5[16][0]]=int(liste5[16][1])
dict_2[liste5[17][0]]=int(liste5[17][1])
dict_2[liste5[18][0]]=int(liste5[18][1])
dict_2[liste5[19][0]]=int(liste5[19][1])
dict_2[liste5[20][0]]=int(liste5[20][1])
dict_2[liste5[21][0]]=int(liste5[21][1])
dict_2[liste5[22][0]]=int(liste5[22][1])
dict_2[liste5[23][0]]=int(liste5[23][1])
dict_2[liste5[24][0]]=int(liste5[24][1])
dict_2[liste5[25][0]]=int(liste5[25][1])
dict_2[liste5[26][0]]=int(liste5[26][1])
dict_2[liste5[27][0]]=int(liste5[27][1])
dict_2[liste5[28][0]]=int(liste5[28][1])
dict_2[liste5[29][0]]=int(liste5[29][1])
dict_2[liste5[30][0]]=int(liste5[30][1])
dict_2[liste5[31][0]]=int(liste5[31][1])
dict_1= {}
dict_1[liste1[0][0]]=[liste3[0]]
dict_1[liste1[1][0]]=[liste3[1]]
dict_1[liste1[2][0]]=[liste3[2]]
dict_1[liste1[3][0]]=[liste3[3]]
dict_1[liste1[4][0]]=[liste3[4]]
dict_1[liste1[5][0]]=[liste3[5]]
dict_1[liste1[6][0]]=[liste3[6]]
dict_1[liste1[7][0]]=[liste3[7]]
dict_1[liste1[8][0]]=[liste3[8]]
dict_1[liste1[9][0]]=[liste3[9]]
dict_1[liste1[10][0]]=[liste3[10]]
dict_1[liste1[11][0]]=[liste3[11]]
dict_1[liste1[12][0]]=[liste3[12]]
dict_1[liste1[13][0]]=[liste3[13]]
dict_1[liste1[14][0]]=[liste3[14]]
dict_1[liste1[15][0]]=[liste3[15]]
dict_1[liste1[16][0]]=[liste3[16]]
dict_1[liste1[17][0]]=[liste3[17]]
dict_1[liste1[18][0]]=[liste3[18]]
dict_1[liste1[19][0]]=[liste3[19]]
dict_1[liste1[20][0]]=[liste3[20]]
dict_1[liste1[21][0]]=[liste3[21]]
dict_1[liste1[22][0]]=[liste3[22]]
dict_1[liste1[23][0]]=[liste3[23]]
dict_1[liste1[24][0]]=[liste3[24]]
dict_1[liste1[25][0]]=[liste3[25]]
dict_1[liste1[26][0]]=[liste3[26]]
dict_1[liste1[27][0]]=[liste3[27]]
liste12=[]
for i in range(27):
    liste12.append(liste1[i][0])
liste10=[]
toplam=0
liste11=["HASET","ERMİŞ","İNKAR","BANKO","DOST","İMTİNA","TAKLA","EKİNOKS","DİZİM","TÜMCE","REİS","İSTİNAF","KARLI","İZİN","AŞK","KESİN","KIRAAT",
         "PERVA","BACA","KAŞE","ERİME","İRİCE","İLKEL","ETRAF","OKUMUŞ","İPTAL","UTAN","MOR"]
t=30
def hesaplama():
    toplam = 0
    print(random.choice(liste12),",Harflerinden Oluşan Bir Kelime Girin(Lütfen Tamamen Büyük Harf Kullanın!)")
    liste15=[]
    while t>0:
        kelime = input("Enter a word:")
        if kelime in liste15:
            print("Daha önce girildi.")
            break
        j=0
        while j!=27:
            j+=1
            if kelime in liste3[j] or kelime in liste11[j]:
                liste15.append(kelime)
                break
            elif  kelime in liste3[j] or kelime in liste11[j]:
                pass
            else:

                print("Geçersiz Kelime")
                break
        toplam=0
        for i in kelime:
            liste10.append(i)
            if i in dict_2.keys():
                for j in liste10:
                    toplam+=int(dict_2[j])

            else:
                print("LÜTFEN BÜYÜK HARFLE GİRİNİZ:")
                break
        for j in range(0,28):
            if kelime in liste3[j] or kelime in liste11[j]:
                total_puan=0

                total_puan+=(len(kelime)*toplam)
                break
            else:
                pass
        try:
            print(total_puan)
        except UnboundLocalError:
            break
hesaplama()








