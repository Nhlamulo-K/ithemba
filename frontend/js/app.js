// TODO: quick-exit handler, load directory, distance calculation in the browser
document.getElementById("quick-exit").addEventListener("click", function () {
    window.location.replace("https://www.google.com");
});

let allEntries = [];

fetch("../data/directory/services.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (entries) {
        allEntries = entries;
        renderServices(entries);
    });

function renderServices (entries) {
    var container = document.getElementById("helplines");
    container.innerHTML = "";
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
}
const provinceFilter = document.getElementById("province-filter");
provinceFilter.addEventListener("change", () => {
    var selected = provinceFilter.value;
    if (selected === "all") {
        renderServices(allEntries);
    }
    else {
        const filtered = allEntries.filter(function (entry) {
            return entry.province === selected || entry.province === "national"
        });
        renderServices(filtered)
    }
});
