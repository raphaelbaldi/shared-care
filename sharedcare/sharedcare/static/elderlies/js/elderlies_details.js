$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-elderly .modal-content").html("");
                $("#modal-elderly").modal("show");
            },
            success: function (data) {
                $("#modal-elderly .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function(table_element, data_element, form) {
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $(table_element).html(data[data_element]);
                    $("#modal-elderly").modal("hide");
                }
                else {
                    $("#modal-elderly .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    var saveAllergyForm = function () {
        return saveForm("#elderly-allergy-table tbody", "html_elderly_allergy_list", $(this));
    };

    var saveMealForm = function () {
        return saveForm("#elderly-meal-table tbody", "html_elderly_meal_list", $(this));
    };

    var saveMedicalAppointmentForm = function () {
        return saveForm("#elderly-medical-appointment-table tbody", "html_elderly_medical_appointment_list", $(this));
    };

    var savePrescriptionForm = function () {
        return saveForm("#elderly-prescription-table tbody", "html_elderly_prescription_list", $(this));
    };

    var saveMedicineForm = function () {
        return saveForm("#elderly-medicine-table tbody", "html_elderly_medicine_list", $(this));
    };


    /* Binding */
    // Allergy
    $(".js-elderly-add-allergy").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-allergy-form", saveAllergyForm);

    $("#elderly-allergy-table").on("click", ".js-delete-elderly-allergy", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-allergy-form", saveAllergyForm);

    // Meal
    $(".js-elderly-add-meal").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-meal-form", saveMealForm);

    $("#elderly-meal-table").on("click", ".js-delete-elderly-meal", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-meal-form", saveMealForm);

    // Medical Appointment
    $(".js-elderly-add-medical_appointment").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-medical_appointment-form", saveMedicalAppointmentForm);

    $("#elderly-medical-appointment-table").on("click", ".js-delete-elderly-medical_appointment", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-medical_appointment-form", saveMedicalAppointmentForm);

    // Prescription
    $(".js-elderly-add-prescription").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-prescription-form", savePrescriptionForm);

    $("#elderly-prescription-table").on("click", ".js-delete-elderly-prescription", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-prescription-form", savePrescriptionForm);

    // Medicine
    $(".js-elderly-add-medicine").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-medicine-form", saveMedicineForm);

    $("#elderly-medicine-table").on("click", ".js-delete-elderly-medicine", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-medicine-form", saveMedicineForm);
});
