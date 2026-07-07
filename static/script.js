function send(){
    let msg = document.getElementById("msg").value;
    let box = document.getElementById("box");

    box.innerHTML += "<p><b>You:</b> " + msg + "</p>";

    fetch("/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    })
    .then(r => r.json())
    .then(d => {
        box.innerHTML += "<p><b>Bot:</b> " + d.reply + "</p>";
    });

    document.getElementById("msg").value = "";
}