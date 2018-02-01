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
public class WaterTankJavaTest {
    
    public WaterTankJavaTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @Before
    public void setUp() {
    }

    @Test
    public void testGetQuantity() {
        
    }

    @Test
    public void testGetLiquid() {
       WaterTankJava Tank = new WaterTankJava();
       assertEquals(Tank.getLiquid(), "none");
       Tank.addLiquid(30, "water");
       assertEquals(Tank.getLiquid(), "water");
    }

    @Test
    public void testAddLiquid() {
        WaterTankJava Tank = new WaterTankJava();
        assertEquals(Tank.getLiquid(), "none");
        Tank.addLiquid(50, "chloride");
        assertEquals(Tank.getLiquid(), "chloride");
        try {
            Tank.addLiquid(40, "extrastuff") ;
            }
        catch (IllegalArgumentException nfe) {
            assertEquals(Tank.getLiquid(), "chloride");
        }
        try {
            Tank.addLiquid(1000, "chloride") ;
            }
        catch (IllegalArgumentException nfe) {
            double quantity = Tank.getQuantity();
            assertEquals(50, quantity, 0); //Not sure why it is throwing errors here or scratching out "assertEquals"
        }
        
    }

    @Test
    public void testRemoveLiquid() {
        WaterTankJava Tank = new WaterTankJava();
        Tank.addLiquid(100, "agua");
        Tank.removeLiquid(45);
        assertEquals(Tank.getQuantity(), 55, 0);
        try {
            Tank.removeLiquid(60);
        } catch (IllegalArgumentException iae) {
            
        }
        Tank.removeLiquid(55);
        assertEquals(Tank.getLiquid(), "none");
    } 
}
