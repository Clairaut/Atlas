package com.atlas.atlas.view;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.layout.BorderPane;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

public class InfoPanel extends BorderPane {
    protected final VBox generalBox;
    protected final HBox chartBox;
    protected final ImageView chartView = new ImageView();

    public InfoPanel() {
        this.setId("info-panel");

        // View components
        this.generalBox = new VBox();
        this.chartBox = new HBox();

        generalBox.setId("general-box");
        chartBox.setId("chart-box");
        chartView.setId("chart-view");

        // Configure ImageView to fill space and maintain aspect ratio
        chartView.setPreserveRatio(true);
        chartView.fitWidthProperty().bind(chartBox.widthProperty());
        chartView.fitHeightProperty().bind(chartBox.heightProperty());

        // Ensure chartBox is square
        chartBox.widthProperty().addListener((obs, oldVal, newVal) -> {
            chartBox.setPrefHeight(newVal.doubleValue());
        });
        chartBox.heightProperty().addListener((obs, oldVal, newVal) -> {
            chartBox.setPrefWidth(newVal.doubleValue());
        });

        chartBox.getChildren().add(chartView);

        // Set generalBox in the center and chartBox on the right
        this.setCenter(generalBox);
        this.setRight(chartBox);
    }

    public void updateChart(String chartName) {
        try {
            System.out.println("Updating chart for: " + chartName);
            String imagePath = "src/main/resources/com/atlas/atlas/charts/temp/" + chartName + ".png";

            // Ensure the old image is cleared
            chartView.setImage(null);

            File imageFile = new File(imagePath);
            if (imageFile.exists()) {
                InputStream imageStream = new FileInputStream(imageFile);
                Image image = new Image(imageStream);
                chartView.setImage(image);
                chartView.setCache(false);
            } else {
                System.out.println("Image file does not exist: " + imagePath);
            }
        } catch (Exception e) {
            System.out.println("Failed to load chart image: " + e.getMessage());
        }
    }

    protected String formatDouble(double value) {
        return String.format("%.4f", value);
    }

    protected String formatRA (double ra) {
        double raHours = ra / 15;
        int hours = (int) raHours;
        int minutes = (int) ((raHours - hours) * 60);
        int seconds = (int) (((((raHours - hours) * 60) - minutes) * 60));

        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }

    protected void addProperty(GridPane grid, String label, String value, int row) {
        Label propertyLabel = new Label(label);
        Label valueLabel = new Label(value);

        propertyLabel.setId("property-label");
        valueLabel.setId("value-label");

        grid.add(propertyLabel, 0, row);
        grid.add(valueLabel, 1, row);
    }
}
