

//////////
lots = driver.find_elements_by_class_name('rate-title')  # берём значение элемента определенного класса

for lot in lots:
    print(lot.text) #печатаем текст из этих элементов, в данном случае выводится название тачек

//////////