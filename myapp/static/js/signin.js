$("form").submit(function () {
        var username = $("input[name='username']").val();
        var pwd = $("input[name='pwd']").val();

        if (username == "" || username == null || username == undefined) {
            alert("Username can not be empty!");
            return false;
        } else if (pwd == "" || pwd == null || pwd == undefined) {
            alert("Password can not be empty");
            return false;
        } else {
            return true;
        }
    });
$("form").ajaxForm(function (data) {
    if(data == '0'){
        alert('Username is not match password');
    } else{
        alert('Sign in successfully,please refresh the page');
        location.reload();
    }
});
