$(document).ready(function () {
    $("#confirmPassword").keyup(checkPasswordMatch);
});

function checkPasswordMatch () {
    console.log("in checkpassmatch");
    var password = $("#newPassword").val();
    var confirmPassword = $("#confirmPassword").val();
    var msg_box = $("#pass_match");
    if (password != confirmPassword) {
        msg_box.text("Passwords do not match");
        msg_box.css({"display":"block", "color":"red"});
    } else {
        msg_box.text("Passwords match");
        msg_box.css({"display":"block", "color":"green"});
    }
}