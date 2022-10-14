money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital > 0:
    money_capital = money_capital-spend
    if money_capital > 0:
        spend = spend*(1+increase)
        money_capital = money_capital + salary
        month += 1

print(month)
