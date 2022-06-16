# tutorialdeki genç adam, class yapmanın aslında string, int, Boolean gibi yeni bir datatype yapmak olduğunu söylüyor

# class fonksiyonda çağrılmış gibi yazıldı aşağıda, bunun içine yazılanlar öbür dosyadaki classın içine gidiyor.
# def __init__ li fonksiyonun içine giriyormuş. Bu yüzden alınan parametreleri self.name gibi gibi eşitledik.
# ve mesela Bunu Student1 değişkenine eşitledik, bu Student1'e object deniyormuş.
# template gibi yazılan class, class kullanılarak oluşturulanlara object deniyormuş.

from class_student import Student  # student dosyasından Student classını importladık

Student1 = Student("Jim", "Business", 3.1, False)  # Student1 objectini oluşturduk.

print(Student1.name)
print(Student1) # tek başına değişik  bir şey veriyor.

Student2 = Student("Pam", "Art", 2.5, True)

print(Student2.gpa)






