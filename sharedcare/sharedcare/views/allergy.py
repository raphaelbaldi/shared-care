from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import AllergyForm
from sharedcare.models import Allergy


def allergy_list(request):
    allergies = Allergy.objects.all()
    return render(request, 'allergies/allergy_list.html', {'allergies': allergies})


def save_allergy_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            allergies = Allergy.objects.all()
            data['html_allergy_list'] = render_to_string('allergies/includes/partial_allergy_list.html', {
                'allergies': allergies
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    print(template_name)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def allergy_create(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
    else:
        form = AllergyForm()
    return save_allergy_form(request, form, 'allergies/includes/partial_allergy_create.html')


def allergy_update(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    if request.method == 'POST':
        form = AllergyForm(request.POST, instance=allergy)
    else:
        form = AllergyForm(instance=allergy)
    return save_allergy_form(request, form, 'allergies/includes/partial_allergy_update.html')


def allergy_delete(request, pk):
    allergy = get_object_or_404(Allergy, pk=pk)
    data = dict()
    if request.method == 'POST':
        allergy.delete()
        data['form_is_valid'] = True
        allergies = Allergy.objects.all()
        data['html_allergy_list'] = render_to_string('allergies/includes/partial_allergy_list.html', {
            'allergies': allergies
        })
    else:
        context = {'allergy': allergy}
        data['html_form'] = render_to_string('allergies/includes/partial_allergy_delete.html', context, request=request)
    return JsonResponse(data)