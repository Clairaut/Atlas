package com.atlas.atlas.model;

public class EclipseData {
    private String timeMax;
    private String celestial;
    private String type;
    private Double magnitude;
    private Double obscuration;
    private Double gamma;

    public EclipseData(String celestial) {
        this.celestial = celestial;
    }

    public void setTimeMax(String timeMax) {
        this.timeMax = timeMax;
    }

    public void setCelestial(String celestial) {
        this.celestial = celestial;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setMagnitude(Double magnitude) {
        this.magnitude = magnitude;
    }

    public void setObscuration(Double obscuration) {
        this.obscuration = obscuration;
    }

    public void setGamma(Double gamma) {
        this.gamma = gamma;
    }

    public String getTimeMax() {
        return timeMax;
    }

    public String getCelestial() {
        return celestial;
    }

    public String getType() {
        return type;
    }

    public Double getMagnitude() {
        return magnitude;
    }

    public Double getObscuration() {
        return obscuration;
    }

    public Double getGamma() {
        return gamma;
    }
}

