from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from sharedcare.forms import MedicineForm
from sharedcare.models import Medicine


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicines/medicine_list.html', {'medicines': medicines})


def save_medicine_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            medicines = Medicine.objects.all()
            data['html_medicine_list'] = render_to_string('medicines/includes/partial_medicine_list.html', {
                'medicines': medicines
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
    else:
        form = MedicineForm()
    return save_medicine_form(request, form, 'medicines/includes/partial_medicine_create.html')


def medicine_update(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
    else:
        form = MedicineForm(instance=medicine)
    return save_medicine_form(request, form, 'medicines/includes/partial_medicine_update.html')


def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    data = dict()
    if request.method == 'POST':
        medicine.delete()
        data['form_is_valid'] = True
        medicines = Medicine.objects.all()
        data['html_medicine_list'] = render_to_string('medicines/includes/partial_medicine_list.html', {
            'medicines': medicines
        })
    else:
        context = {'medicine': medicine}
        data['html_form'] = render_to_string('medicines/includes/partial_medicine_delete.html', context,
                                             request=request)
    return JsonResponse(data)
