zz = input("Введите дату рождение (формат: dd month) (пример: 1 января): ")
year = int(input("Введите год рождения(пример: 2005)"))

#|-------------козерог---------------|
koz = []
koz_1 = 22
koz_2 = 1
for i in range(22, 31, 1):
    koz.append(str(koz_1) + " декабря")#Sar_Vlad
    koz_1 += 1
for i in range(0, 19, 1):
    koz.append(str(koz_2) + " января")
    koz_2 += 1
#Sar_Vlad
#|-------------водолей-#Sar_Vlad--------------|
vod = []
vod_1 = 20
vod_2 = 1
for i in range(20, 31, 1):
    vod.append(str(vod_1) + " января")
    vod_1 += 1
for i in range(0, 18, 1):
    vod.append(str(vod_2) + " февраля")
    vod_2 += 1
#|-------------рыбы---------------|
rib = []
rib_1 = 19
rib_2 = 0#Sar_Vlad
for i in range(19, 28, 1):
    rib.append(str(rib_1) + " февраля")
    rib_1 += 1
for i in range(0, 20, 1):
    rib.append(str(rib_2) + " марта")
    rib_2 += 1
#|--#Sar_Vlad-----------овен---------------|
ov = []
ov_1 = 21
ov_2 = 0
for i in range(21, 31, 1):#Sar_Vlad
    ov.append(str(ov_1) + " марта")
    ov_1 += 1
for i in range(0, 19, 1):
    ov.append(str(ov_2) + " апреля")
    ov_2 += 1
#|-------------телец---------------|
tel = []
tel_1 = 20
tel_2 = 0#Sar_Vlad
for i in range(20, 30, 1):
    tel.append(str(tel_1) + " апреля")
    tel_1 += 1
for i in range(0, 20, 1):
    tel.append(str(tel_2) + " мая")
    tel_2 += 1
#|-------------близнецы----------#Sar_Vlad-----|
bl = []
bl_1 = 21
bl_2 = 0
for i in range(21, 31, 1):
    bl.append(str(bl_1) + " мая")
    bl_1 += 1
for i in range(0, 20, 1):
    bl.append(str(bl_2) + " июня")
    bl_2 += 1
#|-------------рак-----#Sar_Vlad----------|
rak = []
rak_1 = 21
rak_2 = 0
for i in range(21, 30, 1):
    rak.append(str(rak_1) + " июня")#Sar_Vlad
    rak_1 += 1
for i in range(0, 22, 1):
    rak.append(str(rak_2) + " июля")
    rak_2 += 1
#|-------------лев---------------|
lev = []#Sar_Vlad]
lev_1 = 23
lev_2 = 0
for i in range(23, 31, 1):
    lev.append(str(lev_1) + " июля")
    lev_1 += 1
for i in range(0, 22, 1):
    lev.append(str(lev_2) + " августа")
    lev_2 += 1
#|-------------дева---------------|
dev = []
dev_1 = 23
dev_2 = 0
for i in range(23, 31, 1):
    dev.append(str(dev_1) + " августа")
    dev_1 += 1
for i in range(0, 22, 1):
    dev.append(str(dev_2) + " сентября")
    dev_2 += 1
#|-------------ВеСы---------------|
ves = []#Sar_Vlad
ves_1 = 23
ves_2 = 0
for i in range(23, 31, 1):
    ves.append(str(ves_1) + " сентября")
    ves_1 += 1#Sar_Vlad
for i in range(0, 22, 1):
    ves.append(str(ves_2) + " октября")
    ves_2 += 1
#|-------------скорпион---------------|
sk = []
sk_1 = 23
sk_2 = 0
for i in range(23, 30, 1):
    sk.append(str(sk_1) + " октября")
    sk_1 += 1
for i in range(0, 21, 1):
    sk.append(str(sk_2) + " ноября")
    sk_2 += 1
#|---------#Sar_Vlad----стрелец---------------|
st = []
st_1 = 22
st_2 = 0
for i in range(22, 31, 1):
    st.append(str(sk_1) + " ноября")
    sk_1 += 1#Sar_Vlad
for i in range(0, 21, 1):
    st.append(str(st_2) + " декабря")
    st_2 += 1
##Sar_Vlad print(koz,#Sar_Vlad vod, rib, ov,Sar_Vlad tel, bl, rak, lev, dev, ves, sk, st)#Sar_Vlad
if zz in koz:
    print("козерог")
elif zz in vod:
    print("водолей")
elif zz in rib:
    print("рыбы")
elif zz in ov:
    print("овен")
elif zz in tel:
    print("телец")
elif zz in bl:
    print("близнецы")
elif zz in rak:
    print("рак")
elif zz in lev:
    print("лев")
elif zz in dev:
    print("дева")
elif zz in ves:
    print("весы")
elif zz in sk:
    print("скорпион")
elif zz in st:
    print("стрелец")
#|-----------------ГОД----#Sar_Vlad------------|
dragon = [1952 ,1964, 1976, 1988, 2000, 2012] # счет будет в этом диапазоне т.к старые люди и очень #Sar_Vlad молодые в компах не разбираются
zmea = [1953, 1965, 1977, 1989, 2001, 2013]
loshad = [1954, 1966, 1978, 1990, 2002, 2014]
koza = [1955, 1967, 1979, 1991, 2003, 2015]#Sar_Vlad
obez = [1956, 1968, 1980, 1992, 2004, 2016]
petuh = [1957, 1969, 1981, 1993, 2005, 2017]
sobaka = [1958, 1970, 1982, 1994, 2006, 2018]
svin = [1959, 1971, 1983, 1995, 2007, 2019]
krisa = [1960, 1972, 1984, 1996, 2008, 2020]
bik = [1961, 1973, 1985, 1997, 2009, 2021]
tigr = [1962, 1974, 1986, 1998, 2010]
krolik = [1963, 1975, 1987, 1999, 2011]
if year in dragon:
    print("дракон")
elif year in zmea:
    print("змея")
elif year in loshad:
    print("лошадь")
elif year in koza:
    print("коза")
elif year in obez:
    print("обезьяна")
elif year in petuh:
    print("петух")
elif year in sobaka:
    print("собака")
elif year in svin:
    print("свинья")
elif year in krisa:
    print("крыса")
elif year in bik:
    print("бык")
elif year in tigr:
    print("тигр")
elif year in krolik:
    print("кролик")

# Evaluation: OK. Где-то я уже видел точно такой код, с точно такими же блоками комментариев... Хмммм...