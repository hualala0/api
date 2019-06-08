$("form").submit(function () {
        var username = $("input[name='username']").val();
        var pwd = $("input[name='pwd']").val();
        var conf = $("input[name='conf']").val();

        if (username == "" || username == null || username == undefined) {
            alert("Username can not be empty!");
            return false;
        } else if (pwd == "" || pwd == null || pwd == undefined) {
            alert("Password can not be empty");
            return false;

        }else if (pwd != conf) {
            alert("Passwords are different");
            return false;
        } else {
            return true;
        }
    });
$("form").ajaxForm(function (data) {
    if(data == '0'){
        alert('Username is not exist');
    } else{
        alert('Sign up successfully,please sign in');
        location.reload();
    }
});