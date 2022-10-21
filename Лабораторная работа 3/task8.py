money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

delta = money_capital - spend
while delta > 0:
    spend *= 1+increase
    delta += salary
    month += 1
    delta -= spend
print(month)
