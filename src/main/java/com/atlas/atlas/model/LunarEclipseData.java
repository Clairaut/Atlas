package com.atlas.atlas.model;

public class LunarEclipseData extends EclipseData {
    private String timeP1;
    private String timeU1;
    private String timeU2;
    private String timeU3;
    private String timeU4;
    private String timeP2;

    public LunarEclipseData() {
        super("Lunar");
    }

    public String getTimeP1() {
        return timeP1;
    }

    public void setTimeP1(String timeP1) {
        this.timeP1 = timeP1;
    }

    public String getTimeU1() {
        return timeU1;
    }

    public void setTimeU1(String timeU1) {
        this.timeU1 = timeU1;
    }

    public String getTimeU2() {
        return timeU2;
    }

    public void setTimeU2(String timeU2) {
        this.timeU2 = timeU2;
    }

    public String getTimeU3() {
        return timeU3;
    }

    public void setTimeU3(String timeU3) {
        this.timeU3 = timeU3;
    }

    public String getTimeU4() {
        return timeU4;
    }

    public void setTimeU4(String timeU4) {
        this.timeU4 = timeU4;
    }

    public String getTimeP2() {
        return timeP2;
    }

    public void setTimeP2(String timeP2) {
        this.timeP2 = timeP2;
    }

}
