package rocketfacadeproject;
import java.time.Instant;
/**
 *
 * @author cpjohnson
 */
public class InternalComputer {
    private float launchTimer;
    private int altitude;
    private boolean astronautsAlive;
    public InternalComputer()
    {
        this.launchTimer = 0;
        this.altitude = 0;
        this.astronautsAlive = true;
    }
    public boolean monitorAstronautVitals()
    {
        return this.astronautsAlive;
    }
    public void communicate(String message)
    {
        System.out.println(Instant.now() + ": " + message);
    }
    public int getAltitude()
    {
        //System.out.println("getAltitude reached");
        return this.altitude;
    }
    public void setAltitude(int newAltitude) {
        //System.out.println("setAltitude reached");
        this.altitude = newAltitude;
    }
    public float getLaunchTimer() {
        return this.launchTimer;
    }
    public void setLaunchTimer(float newTime) {
        this.launchTimer = newTime;
    }
    
}
