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
public class NoseCone {
    private boolean chuteDeployed;
    private boolean antennaDeployed;
    public NoseCone()
    {
        this.chuteDeployed = false;
        this.antennaDeployed = false;
    }
    public void deployParachute() {
        this.chuteDeployed = true;
    }
    public void retractParachute() {
        this.chuteDeployed = false;
    }
    public void deployAntenna() {
        this.antennaDeployed = true;
    }
    public void retractAntenna() {
        this.antennaDeployed = false;
    }
    public boolean isChuteDeployed() {
        return this.chuteDeployed;
    }
    public boolean isAntennaDeployed() {
        return this.antennaDeployed;
    }
}
