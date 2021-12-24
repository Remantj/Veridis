function checkTheme(theme){
    if(theme.value == "sombre"){
        document.cookie = "sombre";
        SetTheme("sombre");
    }
    if (theme.value == "rose"){
        document.cookie = "rose";
        SetTheme("rose");
    }
    if (theme.value == "clair"){
        document.cookie = "clair"; 
        SetTheme("clair");
    }
    return ;
}

function InitTheme(){
    if(document.cookie == "sombre"){
        SetTheme("sombre");
    }
    if(document.cookie == "rose"){
        SetTheme("rose");
    }
    if(document.cookie == "clair"){
        SetTheme("clair");
    }
}

function SetTheme(theme_name){
    if(theme_name == "sombre"){
        document.body.style.background = "-webkit-gradient(linear, left top, left bottom, from(rgb(34, 34, 34)), to(#000000)) fixed";
        document.body.style.background = "null";
        if(document.getElementById("theme_select") != null){
            document.getElementById("theme_select").value = "sombre";
        }
        document.getElementById("left_menu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        document.getElementById("right_menu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        document.getElementById("main_window").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        if(document.getElementById("logo_img") != null){
            document.getElementById("logo_img").style.top = "-100%";
            document.getElementById("logo_white_img").style.top = "0%";
        }
        var all = document.getElementsByClassName('text');
        for (var i = 0; i < all.length; i++) {
            all[i].style.color = 'white';
        }
    }
    if(theme_name == "rose"){
        document.body.style.background = "-webkit-gradient(linear, left top, left bottom, from(rgb(255, 210, 218)), to(rgb(255, 182, 194))) fixed";
        document.body.style.background = "null";
        if(document.getElementById("theme_select") != null){
            document.getElementById("theme_select").value = "rose";
        }
        let menu_colors = "rgba(212, 129, 143, 0.6)";
        document.getElementById("left_menu").style.backgroundColor = menu_colors;
        document.getElementById("right_menu").style.backgroundColor = menu_colors;
        document.getElementById("main_window").style.backgroundColor = menu_colors;
        if(document.getElementById("logo_img") != null){
            document.getElementById("logo_img").style.top = "0%";
            document.getElementById("logo_white_img").style.top = "-100%";
        }
        var all = document.getElementsByClassName('text');
        for (var i = 0; i < all.length; i++) {
            all[i].style.color = 'black';
        }
    }
    if(theme_name == "clair"){
        document.body.style.background = "-webkit-gradient(linear, left top, left bottom, from(rgb(255, 255, 255)), to(#a2a3a0)) fixed";
        document.body.style.background = "null";
        if(document.getElementById("theme_select") != null){
            document.getElementById("theme_select").value = "clair";
        }
        document.getElementById("left_menu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        document.getElementById("right_menu").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        document.getElementById("main_window").style.backgroundColor = "rgba(0, 0, 0, 0.6)";
        if(document.getElementById("logo_img") != null){
            document.getElementById("logo_img").style.top = "0%";
            document.getElementById("logo_white_img").style.top = "-100%";
        }
        var all = document.getElementsByClassName('text');
        for (var i = 0; i < all.length; i++) {
            all[i].style.color = 'white';
        }
    }
    
}

window.onload = InitTheme;