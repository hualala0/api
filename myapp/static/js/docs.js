$("#docs").attr("class","active");
$("#button").on("click", function () {
    var formData = new FormData();
    var user = $("#user").val();
    formData.append("file", $("#file")[0].files[0]);
    formData.append("user", user);
    $.ajax({
        url: "/apis/"+$("#api").val(),
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log(response);
        }
    });
});