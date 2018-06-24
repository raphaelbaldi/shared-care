from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Allergy, Doctor
from .forms import AllergyForm, DoctorForm


# ALLERGIES
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


# DOCTORS
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})


def save_doctor_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            doctors = Doctor.objects.all()
            data['html_doctor_list'] = render_to_string('doctors/includes/partial_doctor_list.html', {
                'doctors': doctors
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    print(template_name)
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    else:
        form = DoctorForm()
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_create.html')


def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
    else:
        form = DoctorForm(instance=doctor)
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_update.html')


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    data = dict()
    if request.method == 'POST':
        doctor.delete()
        data['form_is_valid'] = True
        doctors = Doctor.objects.all()
        data['html_doctor_list'] = render_to_string('doctors/includes/partial_doctor_list.html', {
            'doctors': doctors
        })
    else:
        context = {'doctor': doctor}
        data['html_form'] = render_to_string('doctors/includes/partial_doctor_delete.html', context, request=request)
    return JsonResponse(data)