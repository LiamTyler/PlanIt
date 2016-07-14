$(document).ready(function () {
    $("#confirmPassword").keyup(checkPasswordMatch);
    $('#Username').keyup(function() {
        console.log("in check username js");  // sanity check
        var username = $("#Username").val();
        $.ajaxSetup({ 
             beforeSend: function(xhr, settings) {
                 function getCookie(name) {
                     var cookieValue = null;
                     if (document.cookie && document.cookie != '') {
                         var cookies = document.cookie.split(';');
                         for (var i = 0; i < cookies.length; i++) {
                             var cookie = jQuery.trim(cookies[i]);
                             // Does this cookie string begin with the name we want?
                             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                 break;
                             }
                         }
                     }
                     return cookieValue;
                 }
                 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                     // Only send the token to relative URLs i.e. locally.
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 }
             } 
        });
        $.ajax({
            url: "/accounts/check_username/",
            type: "POST",
            cache:false,
            data : { username : $('#Username').val() },
            dataType: "json",
            success: function(resp){
                console.log(resp);
                if (resp.available) {
                    $("#username_available").text("Available");
                    $("#username_available").css({"display":"block", "color":"green"});
                } else {
                    $("#username_available").text("Unavailable");
                    $("#username_available").css({"display":"block", "color":"red"});
                }
            }
        });
    });
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