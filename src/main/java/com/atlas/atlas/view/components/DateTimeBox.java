package com.atlas.atlas.view.components;

import javafx.geometry.Pos;
import javafx.scene.control.CheckBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class DateTimeBox extends HBox {
    private CheckBox presentCheckBox;
    private DatePicker dateInput;
    private TextField timeInput;

    public DateTimeBox() {
        this.setAlignment(Pos.BOTTOM_CENTER);
        this.setId("date-time-box");

        // Current Time Toggle
        presentCheckBox = new CheckBox("Current DateTime");
        presentCheckBox.setId("current-time-toggle");

        // Date Input
        dateInput = new DatePicker();
        dateInput.setId("date-input");
        dateInput.setPromptText("MM/dd/yyyy");

        // Time Input
        timeInput = new TextField();
        timeInput.setId("time-input");
        timeInput.setPromptText("hh:mm");

        presentCheckBox.setOnAction(event -> updateDateTimeFields());

        this.getChildren().addAll(presentCheckBox, dateInput, timeInput);
    }

    private void updateDateTimeFields() {
        boolean useCurrentTime = presentCheckBox.isSelected();
        dateInput.setDisable(useCurrentTime);
        timeInput.setDisable(useCurrentTime);

        if (useCurrentTime) {
            LocalDate currentDate = LocalDate.now();
            LocalTime currentTime = LocalTime.now();

            dateInput.setValue(currentDate);
            DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("HH:mm");
            timeInput.setText(timeFormatter.format(currentTime));
        } else {
            dateInput.setValue(null);
            timeInput.clear();
        }
    }

    public String getDate() {
        return dateInput.getValue() != null ? dateInput.getValue().toString() : "";
    }

    public String getTime() {
        return timeInput.getText();
    }
}
