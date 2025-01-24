const yourCoffees = document.getElementById("yourCoffees");
if (window.location.href.endsWith("mylistings/" || "mylistings")) {
    yourCoffees.checked = true;
}
else {
    yourCoffees.checked = false;
}