package com.atlas.atlas.view;

import com.atlas.atlas.model.CelestialData;
import com.atlas.atlas.model.EclipseData;
import javafx.scene.control.Label;

import java.util.List;


public class EclipsePanel extends InfoPanel {
    public EclipsePanel() {
        super();
    };


    public void updateEclipse(EclipseData eclipse) {
        clearData();

        Label eclipseType = new Label(eclipse.getType());

    }

    public void updateCelestials(List<CelestialData> celestials) {
        clearData();

        Label celestialOneName = new Label(celestials.get(0).getSymbol() + " " + celestials.get(0).getName());
        Label celestialTwoName = new Label(celestials.get(1).getSymbol() + " " + celestials.get(1).getName());

    }
}





