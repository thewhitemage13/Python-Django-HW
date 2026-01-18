from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, timedelta


class LoginForm(forms.Form):
    username = forms.CharField(label="Логін", max_length=50)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class ThreeNumbersForm(forms.Form):
    a = forms.FloatField(label="Число 1")
    b = forms.FloatField(label="Число 2")
    c = forms.FloatField(label="Число 3")

    OP_MIN = "min"
    OP_MAX = "max"
    OP_AVG = "avg"
    operation = forms.ChoiceField(
        label="Що знайти",
        widget=forms.RadioSelect,
        choices=[
            (OP_MIN, "Мінімум із трьох"),
            (OP_MAX, "Максимум із трьох"),
            (OP_AVG, "Середнє арифметичне із трьох"),
        ],
    )


class ShopRegistrationForm(forms.Form):
    GENDER_M = "M"
    GENDER_F = "F"
    GENDER_O = "O"

    first_name = forms.CharField(label="Ім'я", max_length=50)
    last_name = forms.CharField(label="Прізвище", max_length=50)
    age = forms.IntegerField(
        label="Вік",
        validators=[MinValueValidator(1), MaxValueValidator(120)],
    )
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(
        label="Стать",
        choices=[
            (GENDER_M, "Чоловіча"),
            (GENDER_F, "Жіноча"),
            (GENDER_O, "Інша / Не вказувати"),
        ],
        widget=forms.RadioSelect,
    )
    address = forms.CharField(
        label="Адреса доставки",
        widget=forms.Textarea(attrs={"rows": 3}),
        max_length=300,
    )
    subscribe = forms.BooleanField(
        label="Бажаєте підписатися на новини нашого інтернет-магазину?",
        required=False,
    )


class ProgrammerDayForm(forms.Form):
    year = forms.IntegerField(
        label="Рік",
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )

    def clean_year(self):
        y = self.cleaned_data["year"]
        if y <= 0:
            raise forms.ValidationError("Рік має бути додатнім числом.")
        return y
