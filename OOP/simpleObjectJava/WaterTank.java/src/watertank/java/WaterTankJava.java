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
public class WaterTankJava { 
    final private int maxQuantity = 1000;
    private double quantity = 0.0;
    private String liquid = "none";
    
    public double getQuantity() {
        return quantity;
    }
    public String getLiquid() {
        return liquid;
    }
    public void addLiquid(double amt,String liquid) {
        if (this.quantity + amt > this.maxQuantity || amt <= 0 || (!this.liquid.equals(liquid) && !"none".equals(this.liquid))) { 
            //throw new IllegalArgumentException("Error adding additional " + liquid);
            if (this.quantity + amt > this.maxQuantity)
                throw new IllegalArgumentException("Adding " + amt + "liters will exceed the maximum quantity of the container, which is " + this.maxQuantity);
            if (amt <= 0)
                throw new IllegalArgumentException("Cannot add " + amt + " as that it is less than or equal to 0. Don't waste my precious computing power!");
            if (!this.liquid.equals(liquid))
                throw new IllegalArgumentException("Cannot mix " + liquid + " with " + " this.liquid!");
            else
                throw new IllegalArgumentException("I don't know why I'm throwing an error here!");
        }
            //Error
        else {
            this.quantity += amt;
            this.liquid = liquid;
        }
    }
    public void removeLiquid(double amt) {
        if (this.quantity - amt < 0)
            throw new IllegalArgumentException("Cannot remove more than the total quantity, which is " + this.quantity);
            //Error
        else
            if(this.quantity == amt) {
                this.liquid = "none";
                this.quantity=0;
            }
        else
            this.quantity -= amt;
    }
}
