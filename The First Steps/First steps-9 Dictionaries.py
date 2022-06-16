monthConversions  = {  #dictionary ler bu süslü parantezle tanımlanıyormuş.
    "Jan":"January",
    "Feb": "Februaty",  #Soldakiler "key" sağdakiler "value" olarak adlandırılıyor.
    "Apr" : "April",    #Aynı sözlükteki kelime ve anlamı gibi.
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
    0 : "deneme"    # Key ler string olmak zorunda değil.
}

print(monthConversions["Nov"]) #novemver verecek.
# print(monthConversions["nov"]) #compile error veriyor.
print(monthConversions.get("Dec"))
print(monthConversions.get("dec")) # case sensetive get içine yazılanlar. Bu yüzden none verdi.
print(monthConversions.get("dec", "Its not a valid key")) #none yerine yazılan yazı çıkabiliyor key bulamayınca

print(monthConversions[0])
print(monthConversions.get(0))
print(monthConversions.get(0,"ooo hello there"))
print(monthConversions.get(1,"ooo hello there"))
