let allCrimeRows = [];

fetch("../data/insights/insights.json")
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        allCrimeRows = data.list;
        renderTable(data.list, "list-view");
        renderTable(data.summary, "summary-view");
        renderTable(data.trend, "trend-view");
    })

function renderTable(data, containerId) {
    var container = document.getElementById(containerId);
    container.innerHTML = ""
    var table = document.createElement("table");
    var keys = Object.keys(data[0]);
    var headerRow = document.createElement("tr");

    for (var i = 0; i < keys.length; i++) {
        var th = document.createElement("th");
        th.textContent = keys[i];
        headerRow.appendChild(th);
    }

    table.appendChild(headerRow);

    for (var row = 0; row < data.length; row++) {
        var bodyRow = document.createElement("tr");
        var values = Object.values(data[row]);
        for (var col = 0; col < values.length; col++) {
            var td = document.createElement("td");
            td.textContent = values[col];
            bodyRow.appendChild(td);
        }
        table.appendChild(bodyRow);
    }

    container.appendChild(table)
}

function showView(viewId) {
    const views = document.querySelectorAll(".view");
    const crime_category = document.getElementById("crime-filter");

    views.forEach(view => {
        view.style.display = "none"
    })

    document.getElementById(viewId).style.display = "block"

    if (viewId === "list-view") {
        crime_category.style.display = "block"
    }
    else{
        crime_category.style.display = "none"
    }
}

function setActiveTab(clicked)  {
    const tabs = document.querySelectorAll(".tabs button");

    tabs.forEach(tab => {
        tab.classList.remove("active")
    })

    clicked.classList.add("active");
}

const listButton = document.getElementById("list-btn");
const summaryButton = document.getElementById("summary-btn");
const trendButton = document.getElementById("trend-btn");

const crimeFilter = document.getElementById("crime-filter");
crimeFilter.addEventListener("change", () => {
    var selected = crimeFilter.value;
    if (selected === "all") {
        renderTable(allCrimeRows, "list-view");
    }
    else {
        const filtered = allCrimeRows.filter(function (data) {
            return data.crime_category === selected;
        });
        renderTable(filtered, "list-view")
    }
});

listButton.addEventListener("click", () => {
    showView("list-view");
    setActiveTab(listButton);
});
summaryButton.addEventListener("click", () => {
    showView("summary-view");
    setActiveTab(summaryButton);
});
trendButton.addEventListener("click", () => {
    showView("trend-view");
    setActiveTab(trendButton);
});

showView("list-view");
setActiveTab(listButton);