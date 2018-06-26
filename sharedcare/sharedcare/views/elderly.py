from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import ElderlyForm
from sharedcare.models import Elderly


def elderly_list(request):
    elderlies = Elderly.objects.all()
    return render(request, 'elderlies/elderly_list.html', {'elderlies': elderlies})


def save_elderly_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            elderlies = Elderly.objects.all()
            data['html_elderly_list'] = render_to_string('elderlies/includes/partial_elderly_list.html', {
                'elderlies': elderlies
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    print(template_name)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def elderly_create(request):
    if request.method == 'POST':
        form = ElderlyForm(request.POST)
    else:
        form = ElderlyForm()
    return save_elderly_form(request, form, 'elderlies/includes/partial_elderly_create.html')


def elderly_update(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)
    if request.method == 'POST':
        form = ElderlyForm(request.POST, instance=elderly)
    else:
        form = ElderlyForm(instance=elderly)
    return save_elderly_form(request, form, 'elderlies/includes/partial_elderly_update.html')


def elderly_delete(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)
    data = dict()
    if request.method == 'POST':
        elderly.delete()
        data['form_is_valid'] = True
        elderlies = Elderly.objects.all()
        data['html_elderly_list'] = render_to_string('elderlies/includes/partial_elderly_list.html', {
            'elderlies': elderlies
        })
    else:
        context = {'elderly': elderly}
        data['html_form'] = render_to_string('elderlies/includes/partial_elderly_delete.html', context, request=request)
    return JsonResponse(data)


def elderly_details(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)
    return render(request, 'elderlies/elderly_details.html', {'elderly': elderly})


def elderly_add_allergy(request, pk):
    pass


def elderly_add_meal(request, pk):
    pass


def elderly_add_medicine(request, pk):
    pass


def elderly_add_prescription(request, pk):
    pass


def elderly_add_medical_appointment(request, pk):
    pass
