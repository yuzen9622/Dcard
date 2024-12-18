let emailInput = document.getElementById("email");
let emailError = document.getElementById("email_error");
let passwordEl = document.querySelectorAll("input[type='password']");
let checkboxEl = document.getElementById("show");

const validateEmail = (email) => {
  return String(email)
    .toLowerCase()
    .match(
      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};
emailInput &&
  emailInput.addEventListener("focusout", () => {
    if (!validateEmail(emailInput.value)) {
      console.log("error");
      emailError.innerText = "信箱格式不正確。";
    } else {
      emailError.innerText = "";
    }
  });
checkboxEl &&
  checkboxEl.addEventListener("change", () => {
    passwordEl.forEach((el) => {
      el.type = checkboxEl.checked ? "text" : "password";
    });
  });

console.log("get script");
