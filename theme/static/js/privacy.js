/* 
Code for the privacy page
*/

function togglePrivacy() {
    var x = document.getElementById("privacy");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function GetAgreement() {
    var cookie = document.cookie;
    if (cookie.indexOf("hasConsent=True") != -1) {
        return true;
    } else if (cookie.indexOf("hasConsent=False") != -1) {
        return false;
    } else {
        togglePrivacy();
        return null;
    }
}

function Agree(){
    var expire = new Date();
    expire = new Date(expire.getTime());
    expire.setMonth(expire.getMonth() + 1);
    document.cookie = "hasConsent=True;expires=" + expire.toGMTString();
    togglePrivacy();
}

function Desagree(){
    var expire = new Date();
    expire = new Date(expire.getTime());
    expire.setMonth(expire.getMonth() + 1);
    document.cookie = "hasConsent=False;expires=" + expire.toGMTString();
    togglePrivacy();
}

function SetTracking(){
    var script = document.createElement('script');

    if(GetAgreement() != true){
        script.setAttribute('data-no-cookie', '');
    }

    script.async = true;
    script.src = 'https://cdn.splitbee.io/sb.js'; 

    document.head.appendChild(script);
}

SetTracking();