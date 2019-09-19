$("#div_digg .fa").click(function () {
    if ($(".info").attr("username")) {

        var article_id = $(".info").attr("article_id");
        $.ajax({
            url: "/blog/zhuan_fa/",
            type: "post",
            data: {
                article_id: article_id,
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) {
                console.log(data);


                if (data.state) {
                    if (data.ji){
                        $("#zhuan1").html("转发成功")
                    }
                    else{
                      $("#zhuan1").html("你不能转发")
                    }

                }
                else {    // 重复提交
                        $("#zhuan1").html("您已经转发过了");
                    }
                    setTimeout(function () {
                        $("#zhuan1").html("")
                    }, 1000)

                }
        })
    }
    else {
        location.href = "/login/"
    }
});