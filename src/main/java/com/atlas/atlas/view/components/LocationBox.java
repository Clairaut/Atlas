package com.atlas.atlas.view.components;

import javafx.geometry.Pos;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;

public class LocationBox extends HBox {
    private CheckBox coordsCheckBox;
    private TextField longitudeInput;
    private TextField latitudeInput;
    private TextField cityInput;

    public LocationBox() {
        this.setAlignment(Pos.BOTTOM_CENTER);
        this.setId("location-box");

        // Coords toggle checkbox
        coordsCheckBox = new CheckBox("Lon/Lat");
        coordsCheckBox.setId("coords-toggle");

        // Coordinate box
        HBox coordsBox = new HBox();
        coordsBox.setAlignment(Pos.BOTTOM_CENTER);
        coordsBox.setId("coords-box");

        // Longitude and latitude
        longitudeInput = new TextField();
        longitudeInput.setDisable(true);
        longitudeInput.setPromptText("Lon");
        longitudeInput.setId("longitude-input");
        latitudeInput = new TextField();
        latitudeInput.setDisable(true);
        latitudeInput.setPromptText("Lat");
        latitudeInput.setId("latitude-input");

        // Coord Box
        coordsBox.getChildren().addAll(longitudeInput, latitudeInput);

        // City Input
        cityInput = new TextField();
        cityInput.setPromptText("City");

        coordsCheckBox.setOnAction(event -> updateLocationFields()); // Lon/lat coords checkbox listener

        this.getChildren().addAll(coordsCheckBox, coordsBox, cityInput);
    }

    private void updateLocationFields() {
        boolean useCoords = coordsCheckBox.isSelected();
        cityInput.setDisable(useCoords);
        longitudeInput.setDisable(!useCoords);
        latitudeInput.setDisable(!useCoords);
    }

    public boolean isUsingCoords() {
        return coordsCheckBox.isSelected();
    }

    public String getLongitude() {
        return longitudeInput.getText();
    }

    public String getLatitude() {
        return latitudeInput.getText();
    }

    public String getCity() {
        return cityInput.getText();
    }
}


