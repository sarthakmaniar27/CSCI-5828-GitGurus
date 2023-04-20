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

// define a function to logout from dashboard
var logout_bool = false;
logout_bool = document.getElementById("logout")
function logout() {
  if (logout_bool){
    window.location.href = "/logout";
  }
}

var report_boolean = false
report_boolean = document.getElementById("report")

function reportCrime(){
  if(report_boolean){
    // open a google form containing important fields
    window.open('https://docs.google.com/forms/d/e/1FAIpQLSeKAMrw-Dk0qmwiqdoCuxCoGMOLWSBH0rPN7T5maERFcZUVEQ/viewform')
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


// ----- Area Chart ----
var areaChartOptions = {
  series: [{
  name: 'TEAM A',
  type: 'area',
  data: [44, 55, 31, 47, 31, 43, 26, 41, 31, 47, 33]
}, {
  name: 'TEAM B',
  type: 'line',
  data: [55, 69, 45, 61, 43, 54, 37, 52, 44, 61, 43]
}],
  chart: {
  height: 350,
  type: 'line',
},
stroke: {
  curve: 'smooth'
},
fill: {
  type:'solid',
  opacity: [0.35, 1],
},
labels: ['Dec 01', 'Dec 02','Dec 03','Dec 04','Dec 05','Dec 06','Dec 07','Dec 08','Dec 09 ','Dec 10','Dec 11'],
markers: {
  size: 0
},
yaxis: [
  {
    title: {
      text: 'Series A',
    },
  },
  {
    opposite: true,
    title: {
      text: 'Series B',
    },
  },
],
tooltip: {
  shared: true,
  intersect: false,
  y: {
    formatter: function (y) {
      if(typeof y !== "undefined") {
        return  y.toFixed(0) + " points";
      }
      return y;
    }
  }
}
};

var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
areaChart.render();