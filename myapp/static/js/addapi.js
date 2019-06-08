var text = $("#text");
var username = $("#username").text();
$(".product").bind("click",function () {
    var value = $(this).text();
    text.text(value);
});
$("#btn1").click(function () {
    if(text.text() == "")
        alert("please choose");
    else
        $.ajax({
            type:"post",
            data:{data:text.text()},
            success:function (data) {
                if(data == '0') alert("fail to add");
                else {
                    alert("add successfully");
                    window.location.href="/user/" + username + "/apimanagement";
                }
            }

        })
});