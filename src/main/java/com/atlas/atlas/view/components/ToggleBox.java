package com.atlas.atlas.view.components;

import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.geometry.Pos;
import javafx.scene.control.Label;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;

public class ToggleBox extends HBox {
    protected BooleanProperty toggleProperty;
    protected Label toggleLabel;
    protected String trueText;
    protected String falseText;
    protected Color trueColor;
    protected Color falseColor;

    public ToggleBox(String trueText, String falseText, Color trueColor, Color falseColor) {
        this.trueText = trueText;
        this.falseText = falseText;
        this.trueColor = trueColor;
        this.falseColor = falseColor;
        this.toggleProperty = new SimpleBooleanProperty(true);
        this.toggleLabel = new Label();

        setAlignment(Pos.CENTER);
        setId("toggle-box");

        StackPane stackPane = new StackPane();
        stackPane.setAlignment(Pos.CENTER);

        Rectangle rectangle = new Rectangle(50, 25);
        rectangle.setArcWidth(25);
        rectangle.setArcHeight(25);
        rectangle.setFill(Color.LIGHTGRAY);

        Circle trigger = new Circle(12.5);
        trigger.setFill(Color.WHITE);
        trigger.setTranslateX(0);

        toggleProperty.addListener((observable, oldValue, newValue) -> {
            if (newValue) {
                rectangle.setFill(trueColor);
                trigger.setTranslateX(12.5);
                toggleLabel.setText(trueText);
            } else {
                rectangle.setFill(falseColor);
                trigger.setTranslateX(-12.5);
                toggleLabel.setText(falseText);
            }
        });

        // Initial state
        if (toggleProperty.get()) {
            rectangle.setFill(trueColor);
            trigger.setTranslateX(12.5);
            toggleLabel.setText(trueText);
        } else {
            rectangle.setFill(falseColor);
            trigger.setTranslateX(-12.5);
            toggleLabel.setText(falseText);
        }

        stackPane.getChildren().addAll(rectangle, trigger);
        getChildren().addAll(stackPane, toggleLabel);
        setOnMouseClicked(event -> toggleProperty.set(!toggleProperty.get()));
    }

    public BooleanProperty getToggleProperty() {
        return toggleProperty;
    }
}
