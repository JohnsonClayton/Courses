/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package watertank.java;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author cpjohnson
 */
public class WaterTankTempSensorTest {
    public WaterTankTempSensorTest() {
        WaterTankTempSensor Tank = new WaterTankTempSensor();
        assertTrue(Tank._maxTemp == 90);
        assertTrue(Tank.getTemp() < Tank._maxTemp);
    }
    
    @Test
    public void TestgetTemp() {
        WaterTankTempSensor Tank = new WaterTankTempSensor();
        Tank.addLiquidT(25, "water", 30.0);
        assertTrue(Tank.getTemp() == 30.0);
    }
    
    @Test
    public void TestaddLiquidT() {
        WaterTankTempSensor Tank = new WaterTankTempSensor();
        Tank.addLiquidT(50, "chloride", 20);
        Tank.addLiquidT(50, "chloride", 22);
        try {
            Tank.addLiquidT(50, "chloride", 29);
        }
            catch(IllegalArgumentException nfe)
            {
                assertTrue(Tank.getTemp() == 25);
            }
    }
}
