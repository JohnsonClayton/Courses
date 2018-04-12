/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rocketfacadeproject;

/**
 *
 * @author cpjohnson
 */
public class FuelTank {
    private double fuelLevel;
    private String fuelType;
    
    public FuelTank() {
        fuelLevel = 0;
        fuelType = "none";
    }
    public double getFuelLevel() {
        return this.fuelLevel;
    }
    public void setFuelLevel(double newFuelLevel) { //Percentage
        if (newFuelLevel >= 100.0)
            this.fuelLevel = 100.0;
        else
            this.fuelLevel = newFuelLevel;
    }
}
