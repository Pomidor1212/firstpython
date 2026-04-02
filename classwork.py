#Знайти найкоротше та найдовше слова

text = "mclaren, mercedes, ferrari, bmw"

cars = text.split()

for car in cars:
    print(car)
    current_length = len(car)
    print(current_length)

