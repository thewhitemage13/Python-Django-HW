from datetime import datetime
from django.http import Http404
from django.shortcuts import render

SONG = {
    "author": "Queen",
    "title": "We Are the Champions",
    "lines": {
        "en": [
            "We are the champions, my friends",
            "And we'll keep on fighting till the end",
        ],
        "fr": [
            "Nous sommes les champions, mes amis",
            "Et nous continuerons à nous battre jusqu'à la fin",
        ],
        "de": [
            "Wir sind die Champions, meine Freunde",
            "Und wir werden weiterkämpfen bis zum Ende",
        ],
        "es": [
            "Somos los campeones, mis amigos",
            "Y seguiremos luchando hasta el final",
        ],
    }
}

def _render_song(request, lang: str):
    if lang not in SONG["lines"]:
        raise Http404("Language not supported")

    context = {
        "lang": lang,
        "lines": SONG["lines"][lang],
        "author": SONG["author"],
        "title": SONG["title"],
    }
    return render(request, "song.html", context)

def song_en(request): return _render_song(request, "en")
def song_fr(request): return _render_song(request, "fr")
def song_de(request): return _render_song(request, "de")
def song_es(request): return _render_song(request, "es")

def cars_home(request):
    return render(request, "cars/home.html")

def cars_toyota(request):
    return render(request, "cars/brand.html", {"brand": "Toyota", "text": "Надійність, гібриди, практичність."})

def cars_honda(request):
    return render(request, "cars/brand.html", {"brand": "Honda", "text": "Економічні двигуни, технології, комфорт."})

def cars_renault(request):
    return render(request, "cars/brand.html", {"brand": "Renault", "text": "Європейський стиль, міські авто, практичність."})

WEEKDAYS_UA = {
    0: ("Понеділок", "mon"),
    1: ("Вівторок", "tue"),
    2: ("Середа", "wed"),
    3: ("Четвер", "thu"),
    4: ("П'ятниця", "fri"),
    5: ("Субота", "sat"),
    6: ("Неділя", "sun"),
}

def weekday(request):
    now = datetime.now()
    idx = now.weekday()
    name_ua, css_class = WEEKDAYS_UA[idx]

    context = {
        "weekday_name": name_ua,
        "css_class": css_class,
        "date": now.date(),
    }
    return render(request, "weekday.html", context)

HEADPHONES = {
    "budslive": {
        "name": "Samsung Galaxy Buds Live",
        "type": "TWS (true wireless)",
        "features": ["ANC (активне шумозаглушення)", "Комфортна посадка", "Компактний кейс"],
    },
    "airpods": {
        "name": "Apple AirPods",
        "type": "TWS (true wireless)",
        "features": ["Швидке підключення в екосистемі Apple", "Комфорт", "Добрий мікрофон"],
    },
    "sonyxm4": {
        "name": "Sony WH-1000XM4",
        "type": "Повнорозмірні Bluetooth",
        "features": ["Потужне ANC", "Висока автономність", "Якісний звук"],
    },
}

def headphones(request):
    model = (request.GET.get("model") or "").strip().lower()

    if not model:
        return render(request, "headphones.html", {"model": None, "available": sorted(HEADPHONES.keys())})

    info = HEADPHONES.get(model)
    if not info:
        return render(request, "headphones.html", {"model": model, "not_found": True, "available": sorted(HEADPHONES.keys())})

    return render(request, "headphones.html", {"model": model, "info": info})
