salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
while months:
    spend = spend + (0 if months == 10 else spend / 100 * 3)
    need_money += spend
    months -= 1
    #print(months, spend)
else:
    print(round(need_money - salary * 10))