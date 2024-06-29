module com.example.atlas {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;
    requires org.json;

    exports com.atlas.atlas.controller;
    opens com.atlas.atlas.controller to javafx.fxml;
    exports com.atlas.atlas.model;
    opens com.atlas.atlas.model to javafx.fxml;
    exports com.atlas.atlas.service;
    opens com.atlas.atlas.service to javafx.fxml;
    exports com.atlas.atlas.view;
    opens com.atlas.atlas.view to javafx.fxml;
    exports com.atlas.atlas.listener;
    opens com.atlas.atlas.listener to javafx.fxml;
}