salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months-1, 0, -1):
    need_money = need_money+spend*(1+increase)**i-salary

need_money = need_money+spend-salary

print(round(need_money))
