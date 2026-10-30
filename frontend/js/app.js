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
            var item = document.createElement("div");

            item.textContent = entry.name
            container.appendChild(item);

            if (entry.phone !== undefined) {
                const phone = document.createElement("p");
                phone.textContent = `phone: ${entry.phone}`;
                container.appendChild(phone);
            }

            if (entry.address !== undefined) {
                const address = document.createElement("p");
                address.textContent = `address: ${entry.address}`;
                container.appendChild(address);
            }
        });
    });
