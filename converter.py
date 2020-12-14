# заданные курсы валют
usd_to_rub = 71.40
eur_tu_rub = 90.01
rub_amount = float(input("Введите количество рублей: ")) # ввод количество исходной валюты
# расчет валюты по курсу
usd_amount = rub_amount / usd_to_rub 
eur_amount = rub_amount / eur_tu_rub
# выводим результат, округляем значения до 2 знаков после запятой
print(round(rub_amount, 2),"Рублей равно -",round(usd_amount, 2),"USD;",round(eur_amount, 2),"EUR.")