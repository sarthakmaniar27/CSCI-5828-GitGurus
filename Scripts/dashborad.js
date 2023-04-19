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