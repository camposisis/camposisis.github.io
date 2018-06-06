authors = {"Ana Rossetti": 1875, "Julia de Burgos": 1914, "Anfolsina Storni": 1878, "Concha Mendez": 1922}
nineteenth_cent = 0
twenty_cent = 0
for author, date in authors.items():
    if date < 1900:
        nineteenth_cent += 1
    else:
        twenty_cent += 1
print("19th= " + str(nineteenth_cent) + " 20th= " + str (twenty_cent))
