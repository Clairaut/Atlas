package com.atlas.atlas.view;

import com.atlas.atlas.model.CelestialData;

import javafx.scene.control.Label;

import javafx.scene.layout.GridPane;

public class CelestialPanel extends InfoPanel {
    private final GridPane infoGrid;

    public CelestialPanel() {
        super();
        infoGrid = new GridPane();
        infoGrid.setId("info-grid");
    };

    public void clearData() {
        generalBox.getChildren().clear();
        infoGrid.getChildren().clear();
    }

    public void updateCelestial(CelestialData celestial) {
        clearData();

        Label celestialName = new Label(celestial.getSymbol() + " " + celestial.getName());
        celestialName.setId("celestial-name");
        generalBox.getChildren().addAll(celestialName, infoGrid);

        addProperty(infoGrid, "Right Ascendant", formatRA(celestial.getRa()), 1);
        addProperty(infoGrid, "Declination", formatDouble(celestial.getDec()) + "°", 2);
        addProperty(infoGrid, "Ecliptic Longitude", formatDouble(celestial.getLongitude()) + "°", 3);
        addProperty(infoGrid, "Ecliptic Latitude", formatDouble(celestial.getLatitude()) + "°", 4);
        addProperty(infoGrid, "Zodiac", celestial.getZodiacSymbol() + " " + celestial.getZodiac() + " " + formatDouble(celestial.getZodiacOrb()) + "°", 5);
        addProperty(infoGrid, "Phase", celestial.getPhaseSymbol() + " " + celestial.getPhase(), 6);
        addProperty(infoGrid, "Phase Angle", formatDouble(celestial.getPhaseAngle()) + "°", 7);
    }
}





