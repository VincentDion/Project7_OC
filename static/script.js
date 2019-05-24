$(function() {
    $('#submit').on('click', function() {
        var userInput = $('input[name="question"]').val();
        if (userInput == "") {
            null;
        }
        else {
            addMsg("user", userInput);
            $(".loader").css({display:"block"});
            $(".test").css({display:"none"});
            
            $.getJSON(
                // documentation : https://api.jquery.com/jquery.getjson/

                //url
                '/_get_json',               
                //data
                {question: userInput},      
                //func
                function (data) {                           

                    if (data.error) {
                        addMsg("grandpy", data.message1);
                    }
                    else {
                        addMsg("grandpy", data.message1 + data.message5);
                        var latitude = data.latitude;
                        var longitude = data.longitude;

                        addMsg("grandpy", data.message2 + data.message3);
                        addMsg("grandpy", data.message4);
                        $('#map').css({display:"block"});
                        initMap(latitude, longitude);
                    }
                    $(".loader").css({display:"none"});
                    $(".test").css({display:"block"});
                }
            );
        }
    });
});

function addMsg(speaker, message) {
    var chatElt = document.createElement("strong");

    if (speaker == "user"){
        chatElt.appendChild(document.createTextNode('Vous: '));
    }
    else{
        chatElt.appendChild(document.createTextNode('Grandpy: '));
    }
    

    var messageElt = document.createElement("p");
    messageElt.appendChild(chatElt);
    messageElt.appendChild(document.createTextNode(message));

    div = document.createElement('div');
    div.classList.add("msg");
    div.appendChild(messageElt);

    document.getElementById("dialog_box").append(div);
}


function initMap(latitude, longitude) {
    // The location of searching place
    var pos = {lat: parseFloat(latitude), lng: parseFloat(longitude)};
    // The map, centered at searching place
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 14, center: pos});
    // The marker, positioned at searching place
    var marker = new google.maps.Marker({position: pos, map: map});
}

