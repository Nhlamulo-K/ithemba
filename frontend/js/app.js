// TODO: quick-exit handler, load directory, distance calculation in the browser
document.getElementById("quick-exit").addEventListener("click", function () {
    window.location.replace("https://www.google.com");
});

fetch("../data/directory/services.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (entries) {
        var container = document.getElementById("helplines");
        entries.forEach(function (entry) {
            var item = document.createElement("p");
            item.textContent = entry.name + " - " + entry.phone;
            container.appendChild(item);
        });
    });
