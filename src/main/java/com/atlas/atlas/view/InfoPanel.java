package com.atlas.atlas.view;

import com.atlas.atlas.model.CelestialData;

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
    protected GridPane infoGrid;

    public InfoPanel() {
        this.setId("info-panel");

        // View components
        this.generalBox = new VBox();
        this.chartBox = new HBox();
        this.infoGrid = new GridPane();

        generalBox.setId("general-box");
        infoGrid.setId("info-grid");
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

        // Ensure chartBox does not resize beyond its content
        chartBox.getChildren().add(chartView);

        // Set generalBox in the center and chartBox on the right
        this.setCenter(generalBox);
        this.setRight(chartBox);
    };

    public void clearData() {
        generalBox.getChildren().clear();
        infoGrid.getChildren().clear();
        chartView.setImage(null);
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
        return String.format("%.2f", value);
    }

    protected void addProperty(String label, String value, int row) {
        Label propertyLabel = new Label(label);
        Label valueLabel = new Label(value);

        propertyLabel.setId("property-label");
        valueLabel.setId("value-label");

        infoGrid.add(propertyLabel, 0, row);
        infoGrid.add(valueLabel, 1, row);
    }
}





