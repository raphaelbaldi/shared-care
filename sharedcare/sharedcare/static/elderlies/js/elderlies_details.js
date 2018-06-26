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

    var saveAllergyForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#elderly-allergy-table tbody").html(data.html_elderly_allergy_list);
                    $("#modal-elderly").modal("hide");
                }
                else {
                    $("#modal-elderly .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */
    $(".js-elderly-add-allergy").click(loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-add-allergy-form", saveAllergyForm);

    $("#elderly-allergy-table").on("click", ".js-delete-elderly-allergy", loadForm);
    $("#modal-elderly").on("submit", ".js-elderly-delete-allergy-form", saveAllergyForm);

    $(".js-elderly-add-meal").click(loadForm);
    $(".js-elderly-add-medical_appointment").click(loadForm);
    $(".js-elderly-add-prescription").click(loadForm);
    $(".js-elderly-add-medicine").click(loadForm);
});
