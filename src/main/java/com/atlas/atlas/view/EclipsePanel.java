package com.atlas.atlas.view;

import com.atlas.atlas.model.CelestialData;
import com.atlas.atlas.model.EclipseData;
import com.atlas.atlas.model.LunarEclipseData;
import com.atlas.atlas.model.SolarEclipseData;
import javafx.geometry.Pos;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;

import java.util.List;

public class EclipsePanel extends InfoPanel {
    private final HBox eclipseBox;
    private final HBox celestialBox;
    private final HBox celestialOneBox;
    private final HBox celestialTwoBox;
    private final GridPane eclipseGrid;
    private final GridPane phaseGrid;
    private final GridPane celestialOneGrid;
    private final GridPane celestialTwoGrid;

    public EclipsePanel() {
        super();
        eclipseBox = new HBox();
        celestialBox = new HBox();
        celestialOneBox = new HBox();
        celestialTwoBox = new HBox();

        eclipseGrid = new GridPane();
        phaseGrid = new GridPane();
        celestialOneGrid = new GridPane();
        celestialTwoGrid = new GridPane();

        eclipseGrid.setId("info-grid");
        phaseGrid.setId("info-grid");
        celestialOneGrid.setId("info-grid");
        celestialTwoGrid.setId("info-grid");
    }

    public void clearEclipseData() {
        generalBox.getChildren().clear();
        eclipseBox.getChildren().clear();
        eclipseGrid.getChildren().clear();
        phaseGrid.getChildren().clear();
    }

    public void clearCelestialData() {
        celestialOneBox.getChildren().clear();
        celestialTwoBox.getChildren().clear();
        celestialOneGrid.getChildren().clear();
        celestialTwoGrid.getChildren().clear();
    }

    public void updateEclipse(EclipseData eclipse) {
        clearEclipseData();

        Label eclipseCelestial = new Label(eclipse.getCelestial() + " Eclipse");
        eclipseCelestial.setId("celestial-name");

        generalBox.getChildren().addAll(eclipseCelestial, eclipseBox);

        eclipseBox.getChildren().addAll(eclipseGrid, phaseGrid);
        eclipseCelestial.setAlignment(Pos.CENTER);
        eclipseGrid.setAlignment(Pos.BOTTOM_LEFT);
        phaseGrid.setAlignment(Pos.BOTTOM_RIGHT);
        eclipseBox.setAlignment(Pos.CENTER);

        addProperty(eclipseGrid, "Type", eclipse.getType(), 1);
        addProperty(eclipseGrid, "Magnitude", formatDouble(eclipse.getMagnitude()), 2);
        addProperty(eclipseGrid, "Obscuration", formatDouble(eclipse.getObscuration()), 3);
        addProperty(eclipseGrid, "Gamma", formatDouble(eclipse.getGamma()), 4);

        // Display phase times based on the type of eclipse
        if (eclipse instanceof SolarEclipseData solarEclipse) {
            addProperty(phaseGrid, "Contact 1", solarEclipse.getTimeC1(), 1);
            addProperty(phaseGrid, "Contact 2", solarEclipse.getTimeC2(), 2);
            addProperty(phaseGrid, "Maximum", solarEclipse.getTimeMax(), 3);
            addProperty(phaseGrid, "Contact 3", solarEclipse.getTimeC3(), 4);
            addProperty(phaseGrid, "Contact 4", solarEclipse.getTimeC4(), 5);
        } else if (eclipse instanceof LunarEclipseData lunarEclipse) {
            addProperty(phaseGrid, "Penumbral Contact 1", lunarEclipse.getTimeP1(), 1);
            addProperty(phaseGrid, "Umbral Contact 1", lunarEclipse.getTimeU1(), 2);
            addProperty(phaseGrid, "Umbral Contact 2", lunarEclipse.getTimeU2(), 3);
            addProperty(phaseGrid, "Maximum", lunarEclipse.getTimeMax(), 4);
            addProperty(phaseGrid, "Umbral Contact 3", lunarEclipse.getTimeU3(), 5);
            addProperty(phaseGrid, "Umbral Contact 4", lunarEclipse.getTimeU4(), 6);
            addProperty(phaseGrid, "Penumbral Contact 2", lunarEclipse.getTimeP2(), 7);
        }
    }

    public void updateCelestials(List<CelestialData> celestials) {
        clearCelestialData();

        generalBox.getChildren().add(celestialBox);
        celestialBox.getChildren().addAll(celestialOneBox, celestialTwoBox);

        CelestialData celestialOne = celestials.get(0);
        CelestialData celestialTwo = celestials.get(1);

        // Celestial Labels
        Label celestialOneName = new Label(celestialOne.getSymbol() + " " + celestialOne.getName());
        Label celestialTwoName = new Label(celestialTwo.getSymbol() + " " + celestialTwo.getName());

        celestialOneBox.getChildren().addAll(celestialOneName, celestialOneGrid);
        celestialTwoBox.getChildren().addAll(celestialTwoName, celestialTwoGrid);

        celestialOneBox.setAlignment(Pos.CENTER);
        celestialTwoBox.setAlignment(Pos.CENTER);
        celestialOneGrid.setAlignment(Pos.CENTER);
        celestialTwoGrid.setAlignment(Pos.CENTER);

        addProperty(celestialOneGrid, "Right Ascension", formatRA(celestialOne.getRa()), 0);
        addProperty(celestialOneGrid, "Declination", formatDouble(celestialOne.getDec()), 1);
        addProperty(celestialOneGrid, "Ecliptic Longitude", formatDouble(celestialOne.getLongitude()), 2);
        addProperty(celestialOneGrid, "Ecliptic Latitude", formatDouble(celestialOne.getLatitude()), 3);


        addProperty(celestialTwoGrid, "Right Ascension", formatDouble(celestialTwo.getRa()), 0);
        addProperty(celestialTwoGrid, "Declination", formatDouble(celestialTwo.getDec()), 1);
        addProperty(celestialTwoGrid, "Ecliptic Longitude", formatDouble(celestialTwo.getLongitude()), 2);
        addProperty(celestialTwoGrid, "Ecliptic Latitude", formatDouble(celestialTwo.getLatitude()), 3);


        System.out.println("Added celestial properties to grids.");
    }
}
