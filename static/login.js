$(document).ready(() => {
    $("#login_form button").addClass('hidden');
    $("#password").on("change paste keyup", (e) => {
        var password = e.target.value;
        if (password !== "") {
            $("#login_form button").removeClass('hidden');
        } else {
            $("#login_form button").addClass('hidden');
        }
    });
});