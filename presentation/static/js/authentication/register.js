const lastname_dictionary_errors = {
        "length_error": "The  last name must be between 3 and 20 characters!",
        "only_letters_error": "The last name must consist of letters only!",
        "empty_field_error": "The last name field cannot be empty as required!"
};

const firstname_dictionary_errors = {
        "length_error": "The first name must be between 3 and 20 characters!",
        "only_letters_error": "The first name must consist of letters only!",
        "empty_field_error": "The first name field cannot be empty as required!"
};

const email_dictionary_errors = {
        "length_error": "The email cannot be longer than 50 characters!",
        "not_valid_error": "The email is invalid!",
        "empty_field_error": "The email field cannot be empty as required!"
};

const password_dictionary_errors = {
        "length_error": "The password must be between 6 and 30 characters!",
        "not_valid_error": "The password must consist of lowercase, uppercase and numbers!",
        "empty_field_error": "The password field cannot be empty as required!",
        "only_spaces_error": "The password field can't just have spaces!",
        "passwords_not_equal_error": "The password must be identical to the confirm password!"
}

const confirm_password_dictionary_errors = {
        "length_error": "The confirm password must be between 6 and 30 characters!",
        "not_valid_error": "The confirm password must consist of lowercase, uppercase and numbers!",
        "empty_field_error": "The confirm password field cannot be empty as required!",
        "only_spaces_error": "The confirm password field can't just have spaces!",
        "passwords_not_equal_error": "The confirm password must be identical to the password!"
}

const lastname = document.getElementById('lastname');
const firstname = document.getElementById('firstname');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirm_password = document.getElementById('confirm_password');
const submit_button = document.getElementById("submit");

const invalid_lastname_div = document.getElementById("invalid-lastname");
const invalid_firstname_div = document.getElementById("invalid-firstname");
const invalid_email_div = document.getElementById("invalid-email");
const invalid_password_div = document.getElementById("invalid-password");
const invalid_confirm_password_div = document.getElementById("invalid-confirm-password");

let flagLastName = false, flagFirstName = false, flagEmail = false, flagPassword = false, flagConfirmPassword = false;

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

function checkLastName(string) {
        flag = true;
        if (string.length === 0) {
                invalid_lastname_div.innerHTML = returnInvalidSpan(lastname_dictionary_errors.empty_field_error);
                flag = false;
        } else if (string.length < 3 || string.length > 20) {
                invalid_lastname_div.innerHTML = returnInvalidSpan(lastname_dictionary_errors.length_error);
                flag = false;
        } else if (string.match(/[^a-zA-Z]/g)) {
                invalid_lastname_div.innerHTML = returnInvalidSpan(lastname_dictionary_errors.only_letters_error);
                flag = false;
        }
        if (flag)
                invalid_lastname_div.innerHTML = "";
        return flag;
}

function checkFirstName(string){
        flag = true;
        if (string.length === 0) {
                invalid_firstname_div.innerHTML = returnInvalidSpan(firstname_dictionary_errors.empty_field_error);
                flag = false;
        }
        else if (string.length < 3 || string.length > 20) {
                invalid_firstname_div.innerHTML = returnInvalidSpan(firstname_dictionary_errors.length_error);
                flag = false;
        }
        else if (string.match(/[^a-zA-Z]/g)) {
                invalid_firstname_div.innerHTML = returnInvalidSpan(firstname_dictionary_errors.only_letters_error);
                flag = false;
        }
        if (flag)
                invalid_firstname_div.innerHTML = "";
        return flag;
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

function checkConfirmPassword(string){
        flag = true;
        if (string.length === 0) {
                invalid_confirm_password_div.innerHTML = returnInvalidSpan(confirm_password_dictionary_errors.empty_field_error);
                flag = false;
        }
        else if (string.length < 6 || string.length > 30) {
                invalid_confirm_password_div.innerHTML = returnInvalidSpan(confirm_password_dictionary_errors.length_error);
                flag = false;
        }
        else if (!string.replace(/\s/g, '').length)
        {
                invalid_confirm_password_div.innerHTML = returnInvalidSpan(confirm_password_dictionary_errors.only_spaces_error);
                flag = false;
        }
        else if (!hasLowerLetter(string) || !hasUpperLetter(string) || !hasDigit(string)) {
                invalid_confirm_password_div.innerHTML = returnInvalidSpan(confirm_password_dictionary_errors.not_valid_error);
                flag = false;
        }
        if (flag)
                invalid_confirm_password_div.innerHTML = "";
        return flag;
}

lastname.addEventListener("keyup", function(){
        flagLastName = checkLastName(this.value);
        if(flagLastName)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagLastName, flagFirstName, flagEmail, flagPassword, flagConfirmPassword)
});
firstname.addEventListener("keyup", function(){
        flagFirstName = checkFirstName(this.value);
        if(flagFirstName)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagLastName, flagFirstName, flagEmail, flagPassword, flagConfirmPassword)
});
email.addEventListener("keyup", function(){
        flagEmail = checkEmail(this.value);
        if(flagEmail)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagLastName, flagFirstName, flagEmail, flagPassword, flagConfirmPassword)
});
password.addEventListener("keyup", function(){
        flagPassword = checkPassword(this.value);
        if(flagPassword)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagLastName, flagFirstName, flagEmail, flagPassword, flagConfirmPassword)
});
confirm_password.addEventListener("keyup", function(){
        flagConfirmPassword = checkConfirmPassword(this.value);
        if(flagConfirmPassword)
                this.style.border = "1.5px solid limegreen";
        else
                this.style.border = "1.5px solid red";
        checkSubmitButton(flagLastName, flagFirstName, flagEmail, flagPassword, flagConfirmPassword)
});

function checkSubmitButton()
{
        if(!flagLastName || !flagFirstName || !flagEmail || !flagPassword || !flagConfirmPassword) {
                submit_button.disabled = true;
        }
        else {
                submit_button.disabled = false;
        }
}

checkSubmitButton();

$('[data-toggle="tooltip"]').tooltip({
            container: 'body'
});

setTimeout(
    function () {
        document.getElementById("toastr-message").style.display = "none";
        },
3000);

