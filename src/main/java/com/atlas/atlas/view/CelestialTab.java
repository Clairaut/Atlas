package com.atlas.atlas.view;

import com.atlas.atlas.listener.CelestialSelectionListener;
import com.atlas.atlas.model.CelestialData;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;

import java.util.HashMap;

public class CelestialTab extends VBox {
    private final ListView<String> listView;
    private final HashMap<String, CelestialData> celestialMap;
    private CelestialSelectionListener selectionListener;

    public CelestialTab() {
        this.setId("left-tab");
        this.setPrefWidth(300);
        this.celestialMap = new HashMap<>();
        listView = new ListView<>(); // Initializing list view
        Label celestialTitleLabel = new Label("\uD83E\uDE90 Celestials \uD83E\uDE90");

        // Set VBox to grow vertically
        VBox.setVgrow(listView, Priority.ALWAYS); // Listview expands entire vertical distance

        this.getChildren().addAll(celestialTitleLabel, listView);

        // Listview listener
        listView.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue != null && selectionListener != null) {
                selectionListener.onCelestialSelected(celestialMap.get(newValue));
            }
        });
    }

    public void clearCelestials() {
        listView.getItems().clear();
    }

    public void addCelestial(CelestialData celestial) {
        String celestialName = celestial.getSymbol() + " " + celestial.getName();
        listView.getItems().add(celestialName);
        celestialMap.put(celestialName, celestial);
    }

    public void setSelectionListener(CelestialSelectionListener selectionListener) {
        this.selectionListener = selectionListener;
    }

}
