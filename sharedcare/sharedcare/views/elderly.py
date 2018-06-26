from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import ElderlyForm, ElderlyAllergyForm
from sharedcare.models import Elderly, Allergy, Meal, ConsumedMedicine, Prescription


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
    elderly = get_object_or_404(Elderly, pk=pk)
    data = dict()

    form = ElderlyAllergyForm()
    if request.method == 'POST':
        form = ElderlyAllergyForm(request.POST)
        if form.is_valid:
            data['form_is_valid'] = True

            allergy_pk = form.data.get('allergies')
            if allergy_pk != -1:
                allergy = Allergy.objects.get(pk=allergy_pk)
                elderly.allergies.add(allergy)
                elderly.save()

            data['html_elderly_allergy_list'] = render_to_string('elderlies/includes/allergy/partial_elderly_allergy_list.html', {
                'elderly': elderly
            })

    context = {'form': form, 'elderly': elderly}
    data['html_form'] = render_to_string('elderlies/includes/allergy/partial_elderly_allergy_form.html', context, request=request)
    return JsonResponse(data)


def elderly_delete_allergy(request, pk, apk):
    elderly = get_object_or_404(Elderly, pk=pk)
    allergy = get_object_or_404(Allergy, pk=apk)
    data = dict()
    if request.method == 'POST':
        elderly.allergies.remove(allergy)
        data['form_is_valid'] = True

        data['html_elderly_allergy_list'] = render_to_string(
            'elderlies/includes/allergy/partial_elderly_allergy_list.html', {
                'elderly': elderly
        })
    else:
        context = {'elderly': elderly, 'allergy': allergy}
        data['html_form'] = render_to_string('elderlies/includes/allergy/partial_elderly_allergy_delete.html', context, request=request)
    return JsonResponse(data)


def elderly_add_meal(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)


def elderly_delete_meal(request, pk, mpk):
    elderly = get_object_or_404(Elderly, pk=pk)
    meal = get_object_or_404(Meal, pk=mpk)
    data = dict()
    if request.method == 'POST':
        elderly.meals.remove(meal)
        meal.delete()

        data['form_is_valid'] = True

        data['html_elderly_meal_list'] = render_to_string(
            'elderlies/includes/meal/partial_elderly_meal_list.html', {
                'elderly': elderly
            })
    else:
        context = {'elderly': elderly, 'meal': meal}
        data['html_form'] = render_to_string('elderlies/includes/meal/partial_elderly_meal_delete.html', context,
                                             request=request)
    return JsonResponse(data)


def elderly_add_medicine(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)


def elderly_delete_medicine(request, pk, mpk):
    elderly = get_object_or_404(Elderly, pk=pk)
    medicine = get_object_or_404(ConsumedMedicine, pk=mpk)
    data = dict()
    if request.method == 'POST':
        elderly.medicine.remove(medicine)
        medicine.delete()

        data['form_is_valid'] = True

        data['html_elderly_medicine_list'] = render_to_string(
            'elderlies/includes/medicine/partial_elderly_medicine_list.html', {
                'elderly': elderly
            })
    else:
        context = {'elderly': elderly, 'medicine': medicine}
        data['html_form'] = render_to_string('elderlies/includes/medicine/partial_elderly_medicine_delete.html', context,
                                             request=request)
    return JsonResponse(data)


def elderly_add_prescription(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)


def elderly_delete_prescription(request, pk, ppk):
    elderly = get_object_or_404(Elderly, pk=pk)
    prescription = get_object_or_404(Prescription, pk=ppk)
    data = dict()
    if request.method == 'POST':
        elderly.prescribed_medicine.remove(prescription)
        prescription.delete()
        data['form_is_valid'] = True

        data['html_elderly_prescription_list'] = render_to_string(
            'elderlies/includes/prescription/partial_elderly_prescription_list.html', {
                'elderly': elderly
            })
    else:
        context = {'elderly': elderly, 'prescription': prescription}
        data['html_form'] = render_to_string('elderlies/includes/prescription/partial_elderly_prescription_delete.html',
                                             context,
                                             request=request)
    return JsonResponse(data)


def elderly_add_medical_appointment(request, pk):
    elderly = get_object_or_404(Elderly, pk=pk)


def elderly_delete_medical_appointment(request, pk, mapk):
    pass
