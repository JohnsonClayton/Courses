/*
author: Clayton Johnson
*/
package rocketfacadeproject;
import java.util.logging.Level;
import java.util.logging.Logger;


public class RocketFacade {
    private InternalComputer computer;
    private FuelTank fueltank;
    private Engine engine;
    private NoseCone nose;
    
    public RocketFacade() {
        //System.out.println("RocketFacade() reached");
        this.computer = new InternalComputer();
        this.fueltank = new FuelTank();
        this.engine = new Engine();
        this.nose = new NoseCone();
    }
    public boolean test() 
    {
        boolean successful = true;
        this.computer.communicate("Aircraft Testing has Begun");
        //Test Computer
        if (!(this.computer.monitorAstronautVitals() && this.computer.getAltitude() == 0 && this.computer.getLaunchTimer() == 0.0)) {
            this.computer.communicate("An issue with the onboard computer was detected. Check the astronaut vitals.");
            successful = false;
        }
        else
            this.computer.communicate("Computer Testing Passed");
        //Test FuelTank
        if(!(this.fueltank.getFuelLevel() == 0)) {
            this.computer.communicate("A malfunction on the fuel tank was detected.");
            successful = false;
        }
        else
            this.computer.communicate("Fuel Tank Testing Passed");
        //Test Engine
        if(!(this.engine.getThrottle() == 0 && !this.engine.isActive()))
        {
            this.computer.communicate("A malfunction with the engine was detected. Check its status.");
            successful = false;
        }
        else this.computer.communicate("Engine Testing Passed");
        //Test NoseCone
        if(this.nose.isAntennaDeployed() || this.nose.isChuteDeployed()) {
            this.computer.communicate("Error with Nose Cone. Check if Antenna or Chute are deployed.");
            successful = false;
        }
        else this.computer.communicate("Nose Cone Testing Passed");
        
        return successful;
    }
    public void fuelUp() 
    {
        //System.out.println("fuelUp() reached");
        this.fueltank.setFuelLevel(100.0);
    }
    public void countdownStart()
    {
        int timeUntilLaunch = 120;
        //System.out.println("countdownStart() reached");
        this.computer.communicate("Countdown sequence initiated");
        while(timeUntilLaunch > 0) {
            try { //This is just telling the system to wait a second (1000ms) and then execute the next statement
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            this.computer.setLaunchTimer(timeUntilLaunch);
            if(timeUntilLaunch >= 4)
                if (timeUntilLaunch % 10 == 0)
                    System.out.println("Launch in " + timeUntilLaunch + " seconds...");
                else {
                    timeUntilLaunch--;
                    timeUntilLaunch++;
                }
            else
                System.out.println("Launch in " + timeUntilLaunch + " seconds...");
            timeUntilLaunch--;
        }
        this.computer.communicate("Launch sequence initiated");
        launch();
        
    }
    public void launch() 
    {
        System.out.println("        |");
        System.out.println("       / \\"); 
        System.out.println("      / _ \\");
        System.out.println("     |.o '.|");
        System.out.println("     |'._.'|");
        System.out.println("     |     |");
        System.out.println("   ,'|  |  |`.");
        System.out.println("  /  |  |  |  \\");
        System.out.println("  |,-'--|--'-.|"); 
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("      |   |      ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("     /     \\      ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("    / /   \\ \\      ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("    | |   | |    ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("     \\ \\ / /     ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("       \\ /     ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("                      ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("                      ");
        try {
            Thread.sleep(500);
        } catch (InterruptedException ex) {
            Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println("                      ");
        
        System.out.println("Aircraft Launch Successful");
    }
    public void abort() 
    {
        this.computer.communicate("An error has been detected and the abort sequence will initialize");
        this.computer.setLaunchTimer(0);
        this.engine.shutdown();
        int alt1 = this.computer.getAltitude();
        try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(RocketFacade.class.getName()).log(Level.SEVERE, null, ex);
            }
        int alt2 = this.computer.getAltitude();
        if (alt1 - alt2 < 0)
            this.nose.deployParachute();
        this.computer.communicate("Aborting mission");
        this.nose.retractAntenna();
        //System.out.println("abort() reached");
    }
    
    public static void main(String[] args) {
        RocketFacade rocket = new RocketFacade();
        if(rocket.test())
            rocket.countdownStart();
        else
            rocket.abort();
        
    }
}