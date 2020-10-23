const email_dictionary_errors = {
        "only_letters_error": "The email cannot be longer than 50 characters!",
        "not_valid_error": "The email is invalid!",
        "empty_field_error": "The email field cannot be empty as required!"
};

const password_dictionary_errors = {
        "length_error": "The password must be between 6 and 30 characters!",
        "not_valid_error": "The password must consist of lowercase, uppercase and numbers!",
        "empty_field_error": "The password field cannot be empty as required!",
        "only_spaces_error": "The password field can't just have spaces!"
}

const email = document.getElementById('email');
const password = document.getElementById('password');
const submit_button = document.getElementById('submit');

const invalid_email_div = document.getElementById("invalid-email");
const invalid_password_div = document.getElementById("invalid-password");

let flagEmail = false, flagPassword = false;

email.value = "";

function returnInvalidSpan(message){
        return "<span class=\"invalid\">" + message + "</span>";
}

function hasLowerLetter(string){
        return string.toUpperCase() != string;
}

function hasUpperLetter(string){
        return string.toLowerCase() != string;
}

function hasDigit(string){
        return /\d/.test(string);
}

function checkEmail(string){
        flag = true;
        if (string.length === 0) {
                invalid_email_div.innerHTML = returnInvalidSpan(email_dictionary_errors.empty_field_error);
                flag = false;
        }
        else if (string.length > 50) {
                invalid_email_div.innerHTML = returnInvalidSpan(email_dictionary_errors.length_error);
                flag = false;
        }
        else if (!string.includes('@') || !string.includes('.')) {
                invalid_email_div.innerHTML = returnInvalidSpan(email_dictionary_errors.not_valid_error);
                flag = false;
        }
        if (flag)
                invalid_email_div.innerHTML = "";
        return flag;
}

function checkPassword(string){
        flag = true;
        if (string.length === 0) {
                invalid_password_div.innerHTML = returnInvalidSpan(password_dictionary_errors.empty_field_error);
                flag = false;
        }
        else if (string.length < 6 || string.length > 30) {
                invalid_password_div.innerHTML = returnInvalidSpan(password_dictionary_errors.length_error);
                flag = false;
        }
        else if (!string.replace(/\s/g, '').length)
        {
                invalid_password_div.innerHTML = returnInvalidSpan(password_dictionary_errors.only_spaces_error);
                flag = false;
        }
        else if (!hasLowerLetter(string) || !hasUpperLetter(string) || !hasDigit(string)) {
                invalid_password_div.innerHTML = returnInvalidSpan(password_dictionary_errors.not_valid_error);
                flag = false;
        }
        if (flag)
                invalid_password_div.innerHTML = "";
        return flag;
}
email.addEventListener("keyup", function(){
        flagEmail = checkEmail(this.value);
        if(flagEmail)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagEmail, flagPassword);
});
password.addEventListener("keyup", function(){
        flagPassword = checkPassword(this.value);
        if(flagPassword)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagEmail, flagPassword);
});

function checkSubmitButton()
{
        if(!flagEmail || !flagPassword) {
                submit_button.disabled = true;
        }
        else {
                submit_button.disabled = false;
        }
}

checkSubmitButton();

setTimeout(
    function () {
        document.getElementById("toastr-message").style.display = "none";
        },
3000);
