//fuction to hide a button after clicked
function HideButton() {
  var x = document.getElementById("signinbtn");
  var y = document.getElementById("signupbtn");
  var z = document.getElementById("user");

  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "block";
    z.style.visibility = "hidden";
  } else {
    x.style.display = "none";
    y.style.display = "none";
    z.style.visibility = "visible";
  }
}

//counter

$(document).ready(function () {
  $(".counter").each(function () {
    $(this)
      .prop("Counter", 0)
      .animate(
        {
          Counter: $(this).text(),
        },
        {
          duration: 4000,
          easing: "swing",
          step: function (now) {
            $(this).text(Math.ceil(now));
          },
        }
      );
  });
});

//used for creation of market place posts to view image.
function preview() {
  frame.src = URL.createObjectURL(event.target.files[0]);
}
function clearImage() {
  document.getElementById("formFile").value = null;
  frame.src = "";
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

(() => {
  "use strict";
  const tooltipTriggerList = Array.from(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach((tooltipTriggerEl) => {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
})();

function EnableDisableTextBox() {
  var chkYes = document.getElementById("chkYes");
  var txtPrice = document.getElementById("txtPrice");
  txtPrice.disabled = chkNo.checked ? false : true;
  if (!txtPrice.disabled) {
    txtPrice.focus();
  }
}

function resetForm() {
  document.getElementById("create-post").value = null;
}
