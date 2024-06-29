package com.atlas.atlas.view;

import com.atlas.atlas.controller.Controller;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;

public class ModuleToolbar extends VBox {
    public ModuleToolbar(Controller controller) {
        this.setId("module-toolbar");
        this.setPrefWidth(100);

        Button celestialButton = new Button("\uD83E\uDE90");
        celestialButton.setId("celestial-module-button");
        celestialButton.setOnAction(event -> controller.switchToCelestialModule());
        Button eclipseButton = new Button("\uD83D\uDF76");
        eclipseButton.setOnAction(event -> controller.switchToEclipseModule());
        eclipseButton.setId("eclipse-module-button");
        Button chartButton = new Button("\uD83D\uDF28\uFE0E");
        chartButton.setId("chart-module-button");


        this.getChildren().addAll(celestialButton, eclipseButton, chartButton);
    }
}
