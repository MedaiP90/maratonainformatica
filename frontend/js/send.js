// server address
const myurl = "server.php";

// envelope
const cont1 = '<div class="w3-container w3-light-gray w3-round-large w3-margin w3-padding-16 w3-border w3-border-deep-orange">';
const cont2 = '</div>' 

function sendRequest(pr, p) {
    $.ajax({
        // parameters to comunicate with the server
        url: myurl,
        type:"GET",
        dataType: "json",
        data: { problem : pr, pp : p },
        crossDomain: true,
        ContentType: "application/json",
        
      // access data
      success: function(data, textStatus, jqXHR){
          var json = JSON.parse(JSON.stringify(data));
          if(json.status == 400) {
            $('#solutions').text('Richiesta non corretta: compila tutti i campi');
          } else if(json.status == 404) {
            $('#solutions').text('Nessuna soluzione trovata');
          } else {
            var t = json.type, s = json.solutions;
            $('#type').text(t);
            var sstring = "";
            for(var element in s) {
                sstring = sstring + cont1 + s[element] + cont2;
            }
            $('#solutions').html(sstring);
          }
      },
      
      // connection error
      error :function(jqXHR, textStatus, errorThrown){
          // errors
      },
      
      // complete connection
      complete :function(qXHR, textStatus){
          // complete
      }
    });
}