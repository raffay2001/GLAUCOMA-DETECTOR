var preview = document.querySelector("#preview");
preview.style.display = "none";
var submitBtn = document.querySelector("#submit-btn");
submitBtn.style.display = "none";

function previewImage() {
  preview.style.display = "block";
  var file = document.querySelector("input[type=file]").files[0];
  var reader = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
  };

  if (file) {
    reader.readAsDataURL(file);
    submitBtn.style.display = "block";
  } else {
    preview.src = "";
  }
}
