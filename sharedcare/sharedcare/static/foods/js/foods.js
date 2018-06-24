$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-food .modal-content").html("");
        $("#modal-food").modal("show");
      },
      success: function (data) {
        $("#modal-food .modal-content").html(data.html_form);
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
          $("#food-table tbody").html(data.html_food_list);
          $("#modal-food").modal("hide");
        }
        else {
          $("#modal-food .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create food
  $(".js-create-food").click(loadForm);
  $("#modal-food").on("submit", ".js-food-create-form", saveForm);

  // Update food
  $("#food-table").on("click", ".js-update-food", loadForm);
  $("#modal-food").on("submit", ".js-food-update-form", saveForm);

  // Delete food
  $("#food-table").on("click", ".js-delete-food", loadForm);
  $("#modal-food").on("submit", ".js-food-delete-form", saveForm);

});
