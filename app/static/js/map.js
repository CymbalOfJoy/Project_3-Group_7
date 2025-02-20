function createMap(City_Visited) {
  // Delete Map
  let map_container = d3.select("#map_container");
  map_container.html(""); // empties it
  map_container.append("div").attr("id", "map"); // recreate it

  // Step 1: CREATE THE BASE LAYERS
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Assemble the API query URL.
  let url = `/api/v1.0/map_data/`;
  console.log(url);

  d3.json(url).then(function (data) {
    // Step 2: CREATE THE DATA/OVERLAY LAYERS
    console.log(data);

    // If a city is selected, filter the data based on that city
    if (City_Visited) {
      data = data.filter(row => row.City_Visited === City_Visited);
    }

    // Initialize the Cluster Group
    let heatArray = [];
    let markers = L.markerClusterGroup();

    // Loop and create marker
    for (let i = 0; i < data.length; i++) {
      let row = data[i];

      let marker = L.marker([row.lat, row.long]).bindPopup(`<h1>${row.City_Visited}</h1><h3>${row.min_cv}</h3><h4>${row.sum_nc}</h4>`);
      markers.addLayer(marker);

      // Heatmap point
      heatArray.push([row.latitude, row.longitude]);
    }

    // Create Heatmap Layer
    let heatLayer = L.heatLayer(heatArray, {
      radius: 25,
      blur: 10
    });

    // Step 3: CREATE THE LAYER CONTROL
    let baseMaps = {
      Street: street,
      Topography: topo
    };

    let overlayMaps = {
      HeatMap: heatLayer,
      City_Visited: markers
    };

    // Step 4: INITIALIZE THE MAP
    let myMap = L.map("map", {
      center: [47.8014, 13.0448],
      zoom: 5,
      layers: [street, markers]
    });

    // Step 5: Add the Layer Control, Legend, Annotations as needed
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
  });
}

function init() {
  // Initialize the map without any filter (show all cities initially)
  createMap("");

  // Event Listener for filter button
  d3.select("#filter-btn").on("click", function () {
    let City_Visited = d3.select("#City_Visited").property("value");
    createMap(City_Visited);
  });

  // Event Listener for reset button
  d3.select("#reset-btn").on("click", function () {
    resetMap();
  });
}

// Reset map to show all cities
function resetMap() {
  // Clear the city filter selection
  d3.select("#City_Visited").property("value", "");

  // Reinitialize the map without any city filter
  createMap("");
}

// on page load, initialize map
init();
