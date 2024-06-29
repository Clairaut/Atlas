package com.atlas.atlas.controller;

import com.atlas.atlas.model.CelestialData;
import com.atlas.atlas.model.EclipseData;
import com.atlas.atlas.service.CelestialDataService;
import com.atlas.atlas.view.EclipsePanel;
import com.atlas.atlas.service.EclipseDataService;

import javafx.scene.layout.AnchorPane;

import java.util.List;

public class EclipseModuleController {
    private AnchorPane modulePane;
    private Controller controller;
    private EclipsePanel eclipsePanel;
    private EclipseDataService eclipseDataService;
    private CelestialDataService celestialDataService;

    public EclipseModuleController(AnchorPane modulePane, Controller controller) {
        this.modulePane = modulePane;
        this.controller = controller;
        this.eclipsePanel = new EclipsePanel();
        this.eclipseDataService = new EclipseDataService();
        this.celestialDataService = new CelestialDataService();
    }

    public void showEclipseView() {
        modulePane.getChildren().clear();
        modulePane.getChildren().addAll(eclipsePanel);

        // Set anchors for celestial info panel
        AnchorPane.setTopAnchor(eclipsePanel, 0.0);
        AnchorPane.setLeftAnchor(eclipsePanel, 0.0);
        AnchorPane.setRightAnchor(eclipsePanel, 0.0);
        AnchorPane.setBottomAnchor(eclipsePanel, 0.0);
    }

    public void handleSubmit(String date, String time, String location, Boolean tropical, Boolean solar) {
        EclipseData eclipse = eclipseDataService.fetchData(date, time, location, solar);
        String eclipseDateTime = eclipse.getTimeMax();

        String[] dateTimeParts = eclipseDateTime.split(" ");
        String eclipseDate = dateTimeParts[0];
        String eclipseTime = dateTimeParts[1];

        List <CelestialData> celestials = celestialDataService.fetchData(eclipseDate, eclipseTime, location, "Sun,Moon", tropical, "combined");

        eclipsePanel.updateEclipse(eclipse);
        eclipsePanel.updateCelestials(celestials);

        StringBuilder combinedName = new StringBuilder();
        for (CelestialData celestial : celestials) {
            combinedName.append(celestial.getName());
        }
        eclipsePanel.updateChart(combinedName.toString());
    }

}
