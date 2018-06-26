from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import FoodForm
from sharedcare.models import Food


def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods})


def save_food_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            foods = Food.objects.all()
            data['html_food_list'] = render_to_string('foods/includes/partial_food_list.html', {
                'foods': foods
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    print(template_name)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
    else:
        form = FoodForm()
    return save_food_form(request, form, 'foods/includes/partial_food_create.html')


def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
    else:
        form = FoodForm(instance=food)
    return save_food_form(request, form, 'foods/includes/partial_food_update.html')


def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    data = dict()
    if request.method == 'POST':
        food.delete()
        data['form_is_valid'] = True
        foods = Food.objects.all()
        data['html_food_list'] = render_to_string('foods/includes/partial_food_list.html', {
            'foods': foods
        })
    else:
        context = {'food': food}
        data['html_form'] = render_to_string('foods/includes/partial_food_delete.html', context, request=request)
    return JsonResponse(data)
