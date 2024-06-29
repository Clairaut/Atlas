package com.atlas.atlas.model;

public class SolarEclipseData extends EclipseData {
    private String timeC1;
    private String timeC2;
    private String timeC3;
    private String timeC4;

    public SolarEclipseData() {
        super("Solar");
    }

    public void setTimeC1(String timeC1) {
        this.timeC1 = timeC1;
    }

    public String getTimeC1() {
        return timeC1;
    }

    public void setTimeC2(String timeC2) {
        this.timeC2 = timeC2;
    }

    public String getTimeC2() {
        return timeC2;
    }

    public void setTimeC3(String timeC3) {
        this.timeC3 = timeC3;
    }

    public String getTimeC3() {
        return timeC3;
    }

    public void setTimeC4(String timeC4) {
        this.timeC4 = timeC4;
    }

    public String getTimeC4() {
        return timeC4;
    }
}
