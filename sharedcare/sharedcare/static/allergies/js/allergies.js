$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-allergy .modal-content").html("");
        $("#modal-allergy").modal("show");
      },
      success: function (data) {
        $("#modal-allergy .modal-content").html(data.html_form);
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
          $("#allergy-table tbody").html(data.html_allergy_list);
          $("#modal-allergy").modal("hide");
        }
        else {
          $("#modal-allergy .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create allergy
  $(".js-create-allergy").click(loadForm);
  $("#modal-allergy").on("submit", ".js-allergy-create-form", saveForm);

  // Update allergy
  $("#allergy-table").on("click", ".js-update-allergy", loadForm);
  $("#modal-allergy").on("submit", ".js-allergy-update-form", saveForm);

  // Delete allergy
  $("#allergy-table").on("click", ".js-delete-allergy", loadForm);
  $("#modal-allergy").on("submit", ".js-allergy-delete-form", saveForm);

});
