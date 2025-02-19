// Use D3 to select the table
let table = d3.select("#table_data");
let tbody = table.select("tbody");

// Make Table Interactive
let dt_table = new DataTable('#table_data');

// Event Listener
d3.select("#filter-btn").on("click", function () {
  doWork();
});

// On Page Load
doWork();

// Helper Functions
function doWork() {
  // Fetch the JSON data and console log it

  // get value
  let Country_Visited = d3.select("#countryInput").property("value"); // user input
  console.log(Country_Visited)
  let url1 = `/api/v1.0/bar_data/`;
  let url2 = `/api/v1.0/table_data/${Country_Visited}`;
  d3.json(url1).then(function (data) {
    // Make Plot
    makeBarPlot(data);
  }).catch(function (error) {
    console.error('Error fetching bar data:', error);
  });

  // Make Request
  if (Country_Visited !== "" || Country_Visited !== null) {

    d3.json(url2).then(function (data) {
      // Make Table
      makeTable(data);
    }).catch(function (error) {
      console.error('Error fetching table data:', error);
    });
  }
}

function makeTable(data) {
  // Clear Table
  tbody.html("");
  dt_table.clear().destroy();

  // Create Table
  data.forEach((row) => {
    let table_row = tbody.append("tr");
    table_row.append("td").text(row.City_Visited);
    table_row.append("td").text(row.Country_Visited);
    table_row.append("td").text(row.Travel_Duration_Days);
    table_row.append("td").text(row.Accommodation_Type);
    table_row.append("td").text(row.Main_Purpose);
    table_row.append("td").text(row.Season_of_Visit);

  });

  // Make Table Interactive (again)
  dt_table = new DataTable('#table_data', {
    order: [[0, 'desc']] // Sort by column 1 desc
  });
}

function makeBarPlot(data) {
  // Create Trace
  let trace = {
    x: data.map(row => row.Country_Visited),
    y: data.map(row => row.num_),
    type: 'bar',
    marker: {
      color: 'firebrick'
    }
  }

  // Data trace array
  let traces = [trace];

  // Apply a title to the layout
  let layout = {
    title: {
      text: `Comparison of Total Travel Cost by Main Purpose`
    },
    yaxis: {
      title: {
        text: 'Main Purpose'
      }
    },
    xaxis: {
      title: {
        text: 'Total Travel Cost'
      }
    },
    height: 600
  }

  // Render the plot to the div tag with id "plot"
  Plotly.newPlot('plot', traces, layout);
}


