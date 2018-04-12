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
public class Engine {
    private double throttlePercentage;
    private boolean active;
    
    public Engine() {
        throttlePercentage = 0;
        active = false;
    }
    public double getThrottle() {
        return this.throttlePercentage;
    }
    public void setThrottle(double newThrottle) {
        this.throttlePercentage = newThrottle;
    }
    public void warmUp() {
        this.active = true;
    }
    public void shutdown() {
        this.active = false;
    }
    public boolean isActive() {
        return this.active;
    }
}
