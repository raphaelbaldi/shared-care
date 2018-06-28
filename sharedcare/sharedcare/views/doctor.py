from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import DoctorForm
from sharedcare.models import Doctor


@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})


@login_required
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
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    else:
        form = DoctorForm()
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_create.html')


@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
    else:
        form = DoctorForm(instance=doctor)
    return save_doctor_form(request, form, 'doctors/includes/partial_doctor_update.html')


@login_required
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
