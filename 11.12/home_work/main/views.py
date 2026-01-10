from django.shortcuts import render

NAV_ITEMS = [
    ("Головна", "home"),
    ("Новини міста", "news"),
    ("Керівництво міста", "management"),
    ("Факти про місто", "facts"),
    ("Контакти служб", "contacts"),
    ("Історія", "history"),
]

def home(request):
    return render(request, "city/home.html", {"title": "Головна", "nav": NAV_ITEMS})

def news(request):
    return render(request, "city/news.html", {"title": "Новини міста", "nav": NAV_ITEMS})

def management(request):
    return render(request, "city/management.html", {"title": "Керівництво міста", "nav": NAV_ITEMS})

def facts(request):
    return render(request, "city/facts.html", {"title": "Факти про місто", "nav": NAV_ITEMS})

def contacts(request):
    return render(request, "city/contacts.html", {"title": "Контактні телефони служб", "nav": NAV_ITEMS})

def history(request):
    return render(request, "city/history.html", {"title": "Історія міста", "nav": NAV_ITEMS})

def history_people(request):
    return render(request, "city/history_people.html", {"title": "Відомі мешканці", "nav": NAV_ITEMS})

def history_photos(request):
    return render(request, "city/history_photos.html", {"title": "Історичні фото", "nav": NAV_ITEMS})
