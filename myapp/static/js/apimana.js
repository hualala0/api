$("img").click(function () {
    var username = $("#username").text();
    console.log(username);
    window.location.href="/user/" + username + "/apimanagement/addapi";
});
$(".btn").bind("click",function () {
    $.ajax({
        type:"post",
        data:{uname:$(this).parent().prev().prev().text(),pname:$(this).parent().prev().text()},
        success:function (data) {
            if(data == '0') alert("fail to delete");
            else {
                alert("delete successfully");
                location.reload();

            }
        }

    })
});