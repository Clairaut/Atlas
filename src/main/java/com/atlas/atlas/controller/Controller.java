package com.atlas.atlas.controller;

import com.atlas.atlas.view.InputToolbar;
import com.atlas.atlas.view.ModuleToolbar;
import javafx.scene.layout.AnchorPane;

public class Controller {
    private AnchorPane modulePane;
    private InputToolbar inputToolbar;
    private ModuleToolbar moduleToolbar;
    private String currentModule;
    private CelestialModuleController celestialController;
    private EclipseModuleController eclipseController;

    public Controller(AnchorPane root) {
        this.modulePane = new AnchorPane();
        this.modulePane.setId("module-pane");
        this.inputToolbar = new InputToolbar(this);
        this.moduleToolbar = new ModuleToolbar(this);

        root.getChildren().addAll(moduleToolbar, inputToolbar, modulePane);

        // Set anchors for the input toolbar
        AnchorPane.setBottomAnchor(inputToolbar, 0.0);
        AnchorPane.setLeftAnchor(inputToolbar, 0.0);
        AnchorPane.setRightAnchor(inputToolbar, 0.0);

        // Set anchors for the module toolbar
        AnchorPane.setTopAnchor(moduleToolbar, 0.0);
        AnchorPane.setLeftAnchor(moduleToolbar, 0.0);
        AnchorPane.setBottomAnchor(moduleToolbar, inputToolbar.getPrefHeight());

        // Set anchors for the module pane
        AnchorPane.setTopAnchor(modulePane, 0.0);
        AnchorPane.setLeftAnchor(modulePane, moduleToolbar.getPrefWidth());
        AnchorPane.setRightAnchor(modulePane, 0.0);
        AnchorPane.setBottomAnchor(modulePane, inputToolbar.getPrefHeight());

        switchToCelestialModule();
    }

    public void switchToCelestialModule() {
        currentModule = "celestial";
        inputToolbar.disableSolarMode();
        if (celestialController == null) {
            celestialController = new CelestialModuleController(modulePane, this);
            celestialController.showCelestialView();
        }
        celestialController.showCelestialView();
    }

    public void switchToEclipseModule() {
        currentModule = "eclipse";
        inputToolbar.enableSolarMode();
        if (eclipseController == null) {
            eclipseController = new EclipseModuleController(modulePane, this);
            eclipseController.showEclipseView();
        }
        eclipseController.showEclipseView();
    }

    public void handleSubmit(String date, String time, String location, Boolean tropical, Boolean solar) {
        if (currentModule.equals("celestial")) {
            celestialController.handleSubmit(date, time, location, tropical);
        } else if (currentModule.equals("eclipse")) {
            eclipseController.handleSubmit(date, time, location, tropical, solar);
        }

    }

    public InputToolbar getInputToolbar() {
        return inputToolbar;
    }
}


