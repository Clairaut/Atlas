package com.atlas.atlas.view;

import com.atlas.atlas.controller.Controller;
import com.atlas.atlas.view.components.DateTimeBox;
import com.atlas.atlas.view.components.LocationBox;
import com.atlas.atlas.view.components.ToggleBox;

import javafx.geometry.Pos;
import javafx.scene.control.*;

import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;

public class InputToolbar extends HBox {
    private Controller mainController;
    private DateTimeBox dateTimeBox;
    private LocationBox locationBox;
    private ToggleBox tropicalToggleBox;
    private ToggleBox solarToggleBox;

    public InputToolbar(Controller mainController) {
        this.setId("input-toolbar");
        this.setPrefHeight(50);
        this.setAlignment(Pos.BOTTOM_CENTER);
        this.mainController = mainController;

        // Location and datetime input boxes
        dateTimeBox = new DateTimeBox(); // Date and time Input
        locationBox = new LocationBox();
        tropicalToggleBox = new ToggleBox("Tropical", "Sidereal", Color.LAVENDER, Color.SILVER); // Tropical/Sidereal toggle

        Button submitButton = new Button("Submit");
        submitButton.setOnAction(event -> handleSubmitButton()); // Submit button listener

        getChildren().addAll(locationBox, dateTimeBox, tropicalToggleBox, submitButton);
    }

    public void enableSolarMode() {
        if (solarToggleBox == null) {
            solarToggleBox = new ToggleBox("Solar", "Lunar", Color.LIGHTGOLDENRODYELLOW, Color.SILVER); // Tropical/Sidereal toggle
        }

        getChildren().add(getChildren().size() - 1, solarToggleBox); // Add before the submit button
    }

    public void disableSolarMode() {
        if (solarToggleBox != null) {
            getChildren().remove(solarToggleBox);
            solarToggleBox = null;
        }
    }

    private void handleSubmitButton() {

        String date = dateTimeBox.getDate(); // Receiving input data
        String time = dateTimeBox.getTime();
        String location;
        Boolean tropical = tropicalToggleBox.getToggleProperty().get();
        Boolean solar = (solarToggleBox != null && solarToggleBox.getToggleProperty().get());

        if (locationBox.isUsingCoords()) {
            location = "(" + locationBox.getLongitude() + "," + locationBox.getLatitude() + ")";
        } else {
            location = locationBox.getCity();
        }

        mainController.handleSubmit(date, time, location, tropical, solar);
    }
}