$(".gz").click(function () {
    // alert(123);
    if ($(".info").attr("username")) {

        var username = $(".info").attr("username");
        $.ajax({
            url: "/blog/guan_zhu/",
            type: "post",
            data: {
                username:username,
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) {
                console.log(data);


                if (data.state) {
                    $(".gz").html(data.mess);
                    $(".benren").text(data.benrenq);

                    timer = setTimeout(function(){
                        $(".benren").text("");
                    },2000);

                }
                else {    // 重复提交
                        $(".gz").html(data.mess);
                    }

                }
        })
    }
    else {
        location.href = "/login/"
    }
});