package com.atlas.atlas.controller;

import com.atlas.atlas.listener.CelestialSelectionListener;
import com.atlas.atlas.model.CelestialData;
import com.atlas.atlas.service.CelestialDataService;
import com.atlas.atlas.view.CelestialPanel;
import com.atlas.atlas.view.CelestialTab;
import javafx.scene.layout.AnchorPane;

import java.util.List;

public class CelestialModuleController implements CelestialSelectionListener {
    private AnchorPane modulePane;
    private Controller controller;
    private CelestialPanel celestialPanel;
    private CelestialTab celestialTab;
    private CelestialDataService celestialDataService;

    public CelestialModuleController(AnchorPane modulePane, Controller controller) {
        this.modulePane = modulePane;
        this.controller = controller;
        this.celestialPanel = new CelestialPanel();
        this.celestialTab = new CelestialTab();
        this.celestialDataService = new CelestialDataService();
        this.celestialTab.setSelectionListener(this);
    }

    public void showCelestialView() {
        modulePane.getChildren().clear();
        modulePane.getChildren().addAll(celestialTab, celestialPanel);

        // Set anchors for celestial info panel
        AnchorPane.setTopAnchor(celestialPanel, 0.0);
        AnchorPane.setLeftAnchor(celestialPanel, celestialTab.getPrefWidth());
        AnchorPane.setRightAnchor(celestialPanel, 0.0);
        AnchorPane.setBottomAnchor(celestialPanel, 0.0);

        // Set anchors for celestial tab
        AnchorPane.setTopAnchor(celestialTab, 0.0);
        AnchorPane.setLeftAnchor(celestialTab, 0.0);
        AnchorPane.setBottomAnchor(celestialTab, controller.getInputToolbar().getPrefHeight());
    }

    public void handleSubmit(String date, String time, String location, Boolean tropical) {
        celestialTab.clearCelestials();
        String targets = "Sun,Moon,Mercury,Venus,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto,Chiron,Ceres,Pallas,Juno,Vesta";
        List<CelestialData> celestialList = celestialDataService.fetchData(date, time, location, targets, tropical, "individual");
        for (CelestialData celestial : celestialList) {
            celestialTab.addCelestial(celestial);
        }

        onCelestialSelected(celestialList.get(0));
    }

    @Override
    public void onCelestialSelected(CelestialData celestial) {
        celestialPanel.updateCelestial(celestial);
        celestialPanel.updateChart(celestial.getName());
    }
}
