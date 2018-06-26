$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-medicine .modal-content").html("");
                $("#modal-medicine").modal("show");
            },
            success: function (data) {
                $("#modal-medicine .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#medicine-table tbody").html(data.html_medicine_list);
                    $("#modal-medicine").modal("hide");
                }
                else {
                    $("#modal-medicine .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create medicine
    $(".js-create-medicine").click(loadForm);
    $("#modal-medicine").on("submit", ".js-medicine-create-form", saveForm);

    // Update medicine
    $("#medicine-table").on("click", ".js-update-medicine", loadForm);
    $("#modal-medicine").on("submit", ".js-medicine-update-form", saveForm);

    // Delete medicine
    $("#medicine-table").on("click", ".js-delete-medicine", loadForm);
    $("#modal-medicine").on("submit", ".js-medicine-delete-form", saveForm);

});
