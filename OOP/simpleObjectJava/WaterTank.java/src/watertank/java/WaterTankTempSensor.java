/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package watertank.java;

/**
 *
 * @author cpjohnson
 */

//I am making a WaterTank that has a thermometer/temperature warning sensor

public class WaterTankTempSensor extends WaterTankJava{
    private double _temp;
    public final double _maxTemp;

    public WaterTankTempSensor() {
        this._temp = 0.0;
        this._maxTemp = 90.0;
    }
    
    
    public double getTemp() {
        return _temp;
    }
    
    public void addLiquidT(double amt, String liquid, double temperature)
    {
        this.addLiquid(amt, liquid);
        if (_temp == 0) {
            _temp = temperature;
        }
        else if((temperature >= _temp -5) && (temperature <= _temp+5) && (temperature <= _maxTemp)) {
            _temp = (_temp + temperature) / 2.0;
        }
    }
    
}
