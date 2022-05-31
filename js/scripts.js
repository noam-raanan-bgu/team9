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

function myUpdateDog() {
  var x = document.getElementById("myUpdateDog");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function myUpdateUser() {
  var x = document.getElementById("myUpdateUser");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

//$("div.toshow").show();

function myProfileDog() {
  var x = document.getElementById("myDog");
  var y = document.getElementById("myUser");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  }
}

function myProfileUser() {
  var x = document.getElementById("myDog");
  var y = document.getElementById("myUser");
  if (y.style.display === "none") {
    y.style.display = "block";
    x.style.display = "none";
  }
}

function newPerson() {
  var newdiv = document.createElement("div");
  newdiv.className += "item";

  var newp = document.createElement("p");
  newp.innerHTML = "TItle";

  newdiv.appendChild(newp);
  document.getElementById("main").appendChild(newdiv);
}

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
