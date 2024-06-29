package com.atlas.atlas.view;

import com.atlas.atlas.model.CelestialData;

import javafx.scene.control.Label;

public class CelestialPanel extends InfoPanel {
    public CelestialPanel() {
        super();
    };


    public void updateCelestial(CelestialData celestial) {
        clearData();

        Label celestialName = new Label(celestial.getSymbol() + " " + celestial.getName());
        celestialName.setId("celestial-name");
        generalBox.getChildren().addAll(celestialName, infoGrid);

        addProperty("Right Ascension    ", formatRA(celestial.getRa()), 1);
        addProperty("Declination    ", formatDouble(celestial.getDec()) + "°", 2);
        addProperty("Ecliptic Longitude ", formatDouble(celestial.getLongitude()) + "°", 3);
        addProperty("Ecliptic Latitude  ", formatDouble(celestial.getLatitude()) + "°", 4);
        addProperty("Zodiac ", celestial.getZodiacSymbol() + " " + celestial.getZodiac() + " " + formatDouble(celestial.getZodiacOrb()) + "°", 5);
        addProperty("Phase  ", celestial.getPhaseSymbol() + " " + celestial.getPhase(), 6);
        addProperty("Phase Angle    ", formatDouble(celestial.getPhaseAngle()), 7);
    }

    public String formatRA (double ra) {
        double raHours = ra / 15;
        int hours = (int) raHours;
        int minutes = (int) ((raHours - hours) * 60);
        int seconds = (int) (((((raHours - hours) * 60) - minutes) * 60));

        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }
}





