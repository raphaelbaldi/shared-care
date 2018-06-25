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

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#elderly-table tbody").html(data.html_elderly_list);
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

  // Create elderly
  $(".js-create-elderly").click(loadForm);
  $("#modal-elderly").on("submit", ".js-elderly-create-form", saveForm);

  // Update elderly
  $("#elderly-table").on("click", ".js-update-elderly", loadForm);
  $("#modal-elderly").on("submit", ".js-elderly-update-form", saveForm);

  // Delete elderly
  $("#elderly-table").on("click", ".js-delete-elderly", loadForm);
  $("#modal-elderly").on("submit", ".js-elderly-delete-form", saveForm);

});
