package com.atlas.atlas.service;

import com.atlas.atlas.model.EclipseData;
import com.atlas.atlas.model.LunarEclipseData;
import com.atlas.atlas.model.SolarEclipseData;
import org.json.JSONObject;

public class EclipseDataService {
    private MiddlewareService middlewareService;

    public EclipseDataService() {
        this.middlewareService = new MiddlewareService();
    }

    public EclipseData fetchData(String date, String time, String location, Boolean solar) {
        String jsonResponse = middlewareService.executePythonScript("eclipse_data", date, time, location, solar.toString());
        JSONObject jsonObject = new JSONObject(jsonResponse);
        return parseEclipseData(jsonObject, solar);
    }

    private EclipseData parseEclipseData(JSONObject jsonObject, Boolean solar) {
        EclipseData eclipseData = solar ? new SolarEclipseData() : new LunarEclipseData();

        eclipseData.setTimeMax(jsonObject.optString("t_max", null)); // General Attributes
        eclipseData.setType(jsonObject.optString("type", null));
        eclipseData.setMagnitude(jsonObject.optDouble("magnitude", 0));
        eclipseData.setGamma(jsonObject.optDouble("gamma", 0));
        eclipseData.setObscuration(jsonObject.optDouble("obscuration", 0));

        if (solar) {
            SolarEclipseData solarEclipseData = (SolarEclipseData) eclipseData; // Solar attributes
            solarEclipseData.setTimeC1(jsonObject.optString("t_c1", null));
            solarEclipseData.setTimeC2(jsonObject.optString("t_c2", null));
            solarEclipseData.setTimeC3(jsonObject.optString("t_c3", null));
            solarEclipseData.setTimeC4(jsonObject.optString("t_c4", null));
        } else {
            LunarEclipseData lunarEclipseData = (LunarEclipseData) eclipseData; // Lunar attributes
            lunarEclipseData.setTimeP1(jsonObject.optString("t_p1", null));
            lunarEclipseData.setTimeU1(jsonObject.optString("t_u1", null));
            lunarEclipseData.setTimeU2(jsonObject.optString("t_u2", null));
            lunarEclipseData.setTimeU3(jsonObject.optString("t_u3", null));
            lunarEclipseData.setTimeU4(jsonObject.optString("t_u4", null));
            lunarEclipseData.setTimeP2(jsonObject.optString("t_u5", null));
        }

        return eclipseData;
    }
}
