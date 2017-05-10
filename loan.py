# coding
# -*- coding: utf-8 -*-


def loan(rate, money, year):
    need_repay = money # 要还的钱


    repay_remaining = money
    month_count = year * 12
    payment = []

    for month in range(month_count):
        payment.append(
            need_repay / month_count +
            repay_remaining * rate / 12
        )

        repay_remaining -= need_repay / month_count

    return payment

s = loan(3.3e-2, 134e4, 13)
print( sum(s))
print( sum(s)-134e4)
print( sum(s)/12/13)