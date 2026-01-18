from django.shortcuts import render
from datetime import date, timedelta

from .forms import LoginForm, ThreeNumbersForm, ShopRegistrationForm, ProgrammerDayForm


USERS = {
    "admin": ("admin123", "Адміністратор"),
    "olena": ("qwerty", "Користувач"),
    "ivan": ("12345", "Користувач"),
}


def task1_login(request):
    result = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = USERS.get(username)
            if user and user[0] == password:
                role = user[1]
                result = {"ok": True, "message": f"Вітаємо, {username}! Рівень доступу: {role}."}
            else:
                result = {"ok": False, "message": "Неправильний логін або пароль."}
    else:
        form = LoginForm()

    return render(request, "hw_forms/task1_login.html", {"form": form, "result": result})


def task2_three_numbers(request):
    answer = None

    if request.method == "POST":
        form = ThreeNumbersForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            c = form.cleaned_data["c"]
            op = form.cleaned_data["operation"]

            nums = [a, b, c]
            if op == ThreeNumbersForm.OP_MIN:
                answer = min(nums)
            elif op == ThreeNumbersForm.OP_MAX:
                answer = max(nums)
            else:
                answer = (a + b + c) / 3
    else:
        form = ThreeNumbersForm()

    return render(request, "hw_forms/task2_three_numbers.html", {"form": form, "answer": answer})


def task3_shop_register(request):
    data = None

    if request.method == "POST":
        form = ShopRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form = ShopRegistrationForm()

    return render(request, "hw_forms/task3_register.html", {"form": form, "data": data})


UA_WEEKDAYS = {
    0: "понеділок",
    1: "вівторок",
    2: "середа",
    3: "четвер",
    4: "п’ятниця",
    5: "субота",
    6: "неділя",
}

UA_MONTHS_GEN = {
    1: "січня",
    2: "лютого",
    3: "березня",
    4: "квітня",
    5: "травня",
    6: "червня",
    7: "липня",
    8: "серпня",
    9: "вересня",
    10: "жовтня",
    11: "листопада",
    12: "грудня",
}


def task4_programmer_day(request):
    result = None

    if request.method == "POST":
        form = ProgrammerDayForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]

            d = date(year, 1, 1) + timedelta(days=255)

            weekday = UA_WEEKDAYS[d.weekday()]
            month = UA_MONTHS_GEN[d.month]
            result = f"{d.day} {month} ({weekday})"
    else:
        form = ProgrammerDayForm()

    return render(request, "hw_forms/task4_programmer_day.html", {"form": form, "result": result})
