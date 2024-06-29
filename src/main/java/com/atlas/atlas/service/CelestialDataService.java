package com.atlas.atlas.service;

import com.atlas.atlas.model.CelestialData;
import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class CelestialDataService {
    private MiddlewareService middlewareService;

    public CelestialDataService() {
        middlewareService = new MiddlewareService();
    }

    public List<CelestialData> fetchData(String date, String time, String location, String targets, Boolean tropical, String chartType) {
        String jsonResponse = middlewareService.executePythonScript("celestial_data", date, time, location, targets, tropical.toString(), chartType);
        JSONArray jsonArray = middlewareService.parseResponse(jsonResponse);
        return parseCelestialData(jsonArray);
    }

    private List<CelestialData> parseCelestialData(JSONArray jsonArray) {
        List<CelestialData> celestialList = new ArrayList<>();
        for (int i=0; i<jsonArray.length(); i++) {
            JSONObject jsonObject = jsonArray.getJSONObject(i);
            CelestialData celestial = new CelestialData();
            celestial.setSymbol(jsonObject.getString("symbol")); // General
            celestial.setName(jsonObject.getString("name"));

            celestial.setRa(jsonObject.optDouble("ra")); // Equatorial Coords
            celestial.setDec(jsonObject.optDouble("dec"));

            celestial.setLongitude(jsonObject.optDouble("longitude")); // Ecliptic Coords
            celestial.setLatitude(jsonObject.optDouble("latitude"));

            celestial.setZodiacSymbol(jsonObject.getString("zodiac_symbol")); // Zodiac
            celestial.setZodiac(jsonObject.getString("zodiac"));
            celestial.setZodiacOrb(jsonObject.getDouble("zodiac_orb"));

            celestial.setPhase(jsonObject.getString("phase")); // Phase
            celestial.setPhaseSymbol(jsonObject.getString("phase_symbol"));
            celestial.setPhaseAngle(jsonObject.getDouble("phase_angle"));

            celestialList.add(celestial);
        }
        return celestialList;
    }
}
