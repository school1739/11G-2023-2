



zz = input("Введите дату рождение (формат: dd month) (пример: 1 января): ")
year = int(input("Введите год рождения(пример: 2000)"))

#|-------------козерог---------------|
koz = []
koz_1 = 22
koz_2 = 1
for i in range(22, 31, 1):
    koz.append(str(koz_1) + " декабря")
    koz_1 += 1
for i in range(0, 19, 1):
    koz.append(str(koz_2) + " января")
    koz_2 += 1
#Grach_Fe
#|-------------водолей---------------|
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
rib_2 = 0
for i in range(19, 28, 1):
    rib.append(str(rib_1) + " февраля")
    rib_1 += 1
for i in range(0, 20, 1):
    rib.append(str(rib_2) + " марта")
    rib_2 += 1
#|-------------овен---------------|
ov = []
ov_1 = 21
ov_2 = 0
for i in range(21, 31, 1):
    ov.append(str(ov_1) + " марта")
    ov_1 += 1
for i in range(0, 19, 1):
    ov.append(str(ov_2) + " апреля")
    ov_2 += 1
#|-------------телец---------------|
tel = []
tel_1 = 20
tel_2 = 0
for i in range(20, 30, 1):
    tel.append(str(tel_1) + " апреля")
    tel_1 += 1
for i in range(0, 20, 1):
    tel.append(str(tel_2) + " мая")
    tel_2 += 1
#|-------------близнецы---------------|
bl = []
bl_1 = 21
bl_2 = 0
for i in range(21, 31, 1):
    bl.append(str(bl_1) + " мая")
    bl_1 += 1
for i in range(0, 20, 1):
    bl.append(str(bl_2) + " июня")
    bl_2 += 1
#|-------------рак---------------|
rak = []
rak_1 = 21
rak_2 = 0
for i in range(21, 30, 1):
    rak.append(str(rak_1) + " июня")
    rak_1 += 1
for i in range(0, 22, 1):
    rak.append(str(rak_2) + " июля")
    rak_2 += 1
#|-------------лев---------------|
lev = []
lev_1 = 23
lev_2 = 0
for i in range(23, 31, 1):
    lev.append(str(lev_1) + " июля")
    lev_1 += 1
for i in range(0, 22, 1):
    lev.append(str(lev_2) + " августа")
    lev_2 += 1
#|-------------дева---------------|
#Grach_Fe
dev = []
dev_1 = 23
dev_2 = 0
for i in range(23, 31, 1):
    dev.append(str(dev_1) + " августа")
    dev_1 += 1
for i in range(0, 22, 1):
    dev.append(str(dev_2) + " сентября")
    dev_2 += 1
#|-------------Веcы---------------|
#Grach_Fe
ves = []
ves_1 = 23
ves_2 = 0
for i in range(23, 31, 1):
    ves.append(str(ves_1) + " сентября")
    ves_1 += 1
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
#|-------------стрелец---------------|
st = []
st_1 = 22
st_2 = 0
for i in range(22, 31, 1):
    st.append(str(sk_1) + " ноября")
    sk_1 += 1
for i in range(0, 21, 1):
    st.append(str(st_2) + " декабря")
    st_2 += 1
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
#|-----------------ГОД----------------|
#Grach_Fe
dragon = [1952 ,1964, 1976, 1988, 2000, 2012]
snake = [1953, 1965, 1977, 1989, 2001, 2013]
horse = [1954, 1966, 1978, 1990, 2002, 2014]
goat = [1955, 1967, 1979, 1991, 2003, 2015]
monke = [1956, 1968, 1980, 1992, 2004, 2016]
cock = [1957, 1969, 1981, 1993, 2005, 2017]
dog = [1958, 1970, 1982, 1994, 2006, 2018]
whore = [1959, 1971, 1983, 1995, 2007, 2019]
rat = [1960, 1972, 1984, 1996, 2008, 2020]
bull = [1961, 1973, 1985, 1997, 2009, 2021]
tiger = [1962, 1974, 1986, 1998, 2010]
rabbit = [1963, 1975, 1987, 1999, 2011]
if year in dragon:
    print("дракон")
elif year in snake:
    print("змея")
elif year in horse:
    print("лошадь")
elif year in goat:
    print("коза")
elif year in monke:
    print("обезьяна")
elif year in cock:
    print("петух")
elif year in dog:
    print("собака")
elif year in whore:
    print("свинья")
elif year in rat:
    print("крыса")
elif year in bull:
    print("бык")
elif year in tiger:
    print("тигр")
elif year in rabbit:
    print("кролик")

