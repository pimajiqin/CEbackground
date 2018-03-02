/**
 * Created by Administrator on 2017/4/24.
 */
$(document).ready(function(){
    // 设置当前导航标签为高亮
    current_uri = window.location.pathname;
    var current_menu = $(".sidebar-menu a[href='" + current_uri + "']");
    $('.sidebar-menu li').removeClass('active');
    current_menu.parentsUntil('.sidebar-menu').addClass('active');
})

function move_to_right(from, to) {
    $("#" + from + " option").each(function () {
        if ($(this).prop("selected") == true) {
            $("#" + to).append(this);
        }
        $(this).remove();
    });
}

function move_to_left(from, to, from_o, to_o) {
    $("#" + from + " option").each(function () {
        if ($(this).prop("selected") == true) {
            $("#" + to).append(this);
        }
        $(this).remove();
    });
}
