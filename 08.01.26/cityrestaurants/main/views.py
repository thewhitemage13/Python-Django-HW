from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import RestaurantForm

def restaurant_list(request):
    spec = request.GET.get('spec', '').strip()

    restaurants = Restaurant.objects.all()
    if spec:
        restaurants = restaurants.filter(specialization__icontains=spec)

    return render(request, 'restaurants/list.html', {
        'restaurants': restaurants,
        'spec': spec,
    })

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()

    return render(request, 'restaurants/form.html', {
        'form': form,
        'title': 'Добавить ресторан',
    })

def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'restaurants/form.html', {
        'form': form,
        'title': 'Редактировать ресторан',
    })

def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')

    return render(request, 'restaurants/confirm_delete.html', {
        'restaurant': restaurant,
    })
