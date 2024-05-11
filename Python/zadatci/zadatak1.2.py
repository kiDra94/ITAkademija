a = 5
b = 3
zbir = a + b
razlika = a - b
proizvod = a * b
djeljenje = a / b
print(zbir, razlika, proizvod, djeljenje)
print("zbir", zbir, "razlika",razlika,"proizvod", proizvod,"djeljenje", djeljenje, '\n')
print("zbir {} razlika {} proizvod {} djeljenje {}" .format(zbir , razlika , proizvod , djeljenje))
print("zbir {0} razlika {1} proizvod {2} djeljenje {3}" .format(zbir, razlika, proizvod, djeljenje))
print("zbir {0:d} razlika {1:d} proizvod {2:d}" .format(zbir, razlika, proizvod))
print("zbir %d razlika %d prozvod%d djeljenje %f"%(zbir,razlika,proizvod,djeljenje))
print("zbir {0:d} razlika {1:d} proizvod {2:d} djeljenje {3:f}" .format(zbir, razlika, proizvod, djeljenje))
#zasto ne radi print("zbir {0:d} razlika {1:d} proizvod {2:d} djeljenje {3:d}" .format(zbir, razlika, proizvod, djeljenje)) dobijam error
# print("zbir {0:d} razlika {1:d} proizvod {2:d}  djeljenje {3:d}" .format(zbir, razlika, proizvod, djeljenje))
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ValueError: Unknown format code 'd' for object of type 'float'
