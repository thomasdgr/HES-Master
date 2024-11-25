let jQuery = $(document).ready(function () {
    M.Tabs.init($('#ms-tab-result'), {});
    const parts = window.location.href.split("/");
    root_url = parts[0] + "/";
    for (let i = 1; i < parts.length - 1; i++) {
        if (parts[i].length !== 0) {
            root_url += "/" + parts[i];
        }
    }
    reset();
});

function fetch(){
    $("#result-tab").html("");
    let url = root_url + "/" + "compute";
    const req = new XMLHttpRequest();
    req.open("POST", url);
    req.setRequestHeader(
        "Content-Type",
        "application/json"
    );
    req.responseType = "json";
    req.onload = () => {
        if (req.status != 200) {
            M.toast(
                { html: "Error " + req.status + " when retrieving results"}
            );
        } else {
            let div = document.createElement('div');
            div.innerHTML += req.response["response"];
            document.getElementById("result-tab").appendChild(div);
            $("#result-tab").css("white-space", "pre-wrap");
        }
    };
    param = {
        "query": document.getElementById("chat").value
    }
    req.send(JSON.stringify(param));
    let command = "curl "
        + "-H \"Content-Type: application/json\" "
        + "-H \"accept: application/json\" "
        + "-d '" + JSON.stringify(param)
        + "' -X POST " + url;
    $("#ms-id-curl").text(command);
    M.toast({ html: "Request sent successfully !"});
}

function reset() {
    $("#result-tab").html("");
    $("#result-tab").css("white-space", "nowrap");
    $("#ms-id-curl").text("");
    $('html,body').scrollTop(0);
    document.getElementById("chat").value = "";
}
