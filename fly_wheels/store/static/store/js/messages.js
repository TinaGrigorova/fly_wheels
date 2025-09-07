
ocument.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.toast').forEach(function (el) {

    new bootstrap.Toast(el).show();
  });
});
