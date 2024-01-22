function toggleLocation() {
    var checkbox = document.getElementById("coords-checkbox");
    var location = document.getElementById("location-input");
    var longitude = document.getElementById("longitude-input");
    var latitude = document.getElementById("latitude-input");

    if (checkbox.checked == true) {
        location.disabled = true;
        longitude.disabled = false;
        latitude.disabled = false;
    } else {
        location.disabled = false;
        longitude.disabled = true;
        latitude.disabled = true;
    }

}

