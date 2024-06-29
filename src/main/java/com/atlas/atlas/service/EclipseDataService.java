package com.atlas.atlas.service;

import com.atlas.atlas.model.EclipseData;
import com.atlas.atlas.model.LunarEclipseData;
import com.atlas.atlas.model.SolarEclipseData;
import org.json.JSONArray;
import org.json.JSONObject;


public class EclipseDataService {
    private MiddlewareService middlewareService;


    public EclipseData fetchData(String date, String time, String location, Boolean solar) {
        String eclipseJSONResponse = middlewareService.executePythonScript("eclipse_data", date, time, location, solar.toString());
        JSONArray jsonArray = middlewareService.parseResponse(eclipseJSONResponse);
        return parseEclipseData(jsonArray, solar);
    }

    private EclipseData parseEclipseData(JSONArray jsonArray, Boolean solar) {
        EclipseData eclipseData = solar ? new SolarEclipseData() : new LunarEclipseData();

        for (int i = 0; i < jsonArray.length(); i++) {
            JSONObject jsonObject = jsonArray.getJSONObject(i);

            eclipseData.setTimeMax(jsonObject.getString("t_max")); // General Attributes
            eclipseData.setType(jsonObject.getString("type"));
            eclipseData.setMagnitude(jsonObject.getDouble("magnitude"));
            eclipseData.setGamma(jsonObject.getDouble("gamma"));
            eclipseData.setObscuration(jsonObject.getDouble("obscuration"));

            if (solar) {
                SolarEclipseData solarEclipseData = (SolarEclipseData) eclipseData; // Solar attributes
                solarEclipseData.setTimeC1(jsonObject.getString("t_c1"));
                solarEclipseData.setTimeC2(jsonObject.getString("t_c2"));
                solarEclipseData.setTimeC3(jsonObject.getString("t_c3"));
                solarEclipseData.setTimeC4(jsonObject.getString("t_c4"));
                solarEclipseData.setTimeMax(jsonObject.getString("t_max"));
            } else {
                LunarEclipseData lunarEclipseData = (LunarEclipseData) eclipseData; // Lunar attributes
                lunarEclipseData.setTimeP1(jsonObject.getString("t_p1"));
                lunarEclipseData.setTimeU1(jsonObject.getString("t_u1"));
                lunarEclipseData.setTimeU2(jsonObject.getString("t_u2"));
                lunarEclipseData.setTimeU3(jsonObject.getString("t_u3"));
                lunarEclipseData.setTimeU4(jsonObject.getString("t_u4"));
                lunarEclipseData.setTimeP2(jsonObject.getString("t_u5"));

            }
        }

        return eclipseData;
    }
}
