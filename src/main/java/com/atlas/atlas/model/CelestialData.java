package com.atlas.atlas.model;

public class CelestialData {
    private String symbol;
    private String name;
    private Double ra;
    private Double dec;
    private Double longitude;
    private Double latitude;
    private String zodiac;
    private String zodiacSymbol;
    private Double zodiacOrb;
    private String phase;
    private String phaseSymbol;
    private Double phaseAngle;

    // Setters
    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public void setName(String name) {
        this.name = name;
    }

    public void setRa(Double ra) {
        this.ra = ra;
    }
    public void setDec(Double dec) {
        this.dec = dec;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }
    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public void setZodiac(String zodiac) {
        this.zodiac = zodiac;
    }
    public void setZodiacSymbol(String zodiacSymbol) {
        this.zodiacSymbol = zodiacSymbol;
    }
    public void setZodiacOrb(Double zodiacOrb) {this.zodiacOrb = zodiacOrb;}

    public void setPhase(String phase) {this.phase = phase;}
    public void setPhaseSymbol(String phaseSymbol) {this.phaseSymbol = phaseSymbol;}
    public void setPhaseAngle(Double phaseAngle) {this.phaseAngle = phaseAngle;}

    // Getters
    public String getSymbol() {
        return symbol;
    }
    public String getName() {
        return name;
    }

    public Double getRa() {
        return ra;
    }
    public Double getDec() {
        return dec;
    }

    public Double getLongitude() {
        return longitude;
    }
    public Double getLatitude() {
        return latitude;
    }

    public String getZodiac() {
        return zodiac;
    }
    public String getZodiacSymbol() {
        return zodiacSymbol;
    }
    public Double getZodiacOrb() {return zodiacOrb;}

    public String getPhase() {return phase;}
    public String getPhaseSymbol() {return phaseSymbol;}
    public Double getPhaseAngle() {return phaseAngle;}
}
