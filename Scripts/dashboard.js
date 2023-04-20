console.log("JavaScript code is being executed!");


// Sidebar Toggle

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

// define open side bar function
function openSidebar(){
    if(!sidebarOpen){
        sidebar.classList.add("sidebar-responsive");
        sidebarOpen = true;
    }
}

// define a close sidebar function
function closeSidebar(){
    if(sidebarOpen){
        sidebar.classList.remove("sidebar-responsive");
        sidebarOpen = false;
    }
}


// ---------- CHARTS ------------


// Bar chart
var barChartOptions = {
    series: [{
    data: [10,8,6,4,2]
  }],
    chart: {
    type: 'bar',
    height: 350,
    toolbar: {
        show:false
    },
  },
  colors : [
    "#246dec",
    "#cc3c43",
    "#367952",
    "#f5b74f",
    "#4f35a1"
  ],
  plotOptions: {
    bar: {
      distributed: true,  
      borderRadius: 4,
      horizontal: false,
      columnWidth : '40%',
    }
  },
  dataLabels: {
    enabled: false
  },
  xaxis: {
    categories: ["Laptop", "Phone", "Monitor", "Headphones", "Camera"
    ],
  },
  yaxis : {
    title: "Count"
  }
  };

var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
barChart.render();