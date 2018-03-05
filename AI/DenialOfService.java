/*
 * @author Clayton Johnson
 *   using code originally made by Warren MacEvoy for a Dr. Strange optimization problem
 *      This code is meant to optimize using Gradient Descent
 *      I am optimizing the best theoretical time to conduct a distributed attack on a 
 *    by attempting to locate when the server is busiest and has the fewest number of 
 *    administrators working. 
 *    Traffic is mimicked by T(x) = 6 * sin((x-6)/2.4pi) + 1
 *  and Admin Hours are mimicked by H(y) = cos(2y/2.4pi)^2
 *
 */   
package gradientdescent;

import java.util.Arrays;
import java.util.HashMap;

public class DenialOfServiceRealMin implements RealMin {

    double[] values = new double[2];
    private static final String[] names = new String[]{"TRAFFIC", "ADMINHOURS"};
    private static final HashMap< String, Integer> indexes = new HashMap< String, Integer>();

    static {
        for (int i = 0; i < names.length; ++i) {
            indexes.put(names[i], i);
        }
    }
    public static final int ITRAFFIC = indexes.get("TRAFFIC"); // Represents the time at which traffic is busiest
    public static final int IADMINHOURS = indexes.get("ADMINHOURS"); // Represents how many hours are put in by SysAdmins during this hour

    @Override
    public int getRealParameterSize() {
        return names.length;
    }

    @Override
    public String getRealParameterName(int i) {
        return names[i];
    }

    @Override
    public int getRealParameterIndex(String name) {
        return indexes.get(name);
    }

    @Override
    public double getRealParameterValue(int index) {
        return values[index];
    }

    @Override
    public void setRealParameterValue(int index, double value) {
        values[index] = value;
    }

    public DenialOfServiceRealMin() {
    }

    public DenialOfServiceMin(DrStrangeRealMin copy) {
        System.arraycopy(copy.values, 0, copy.values, 0, values.length);
    }

    @Override
    public RealMin copy() {
        return new DrStrangeRealMin(this);
    }

    @Override
    public double getValue() {  //This is where we mess with our equations and stuff of the like
        double TRAFFIC = values[ITRAFFIC]; //These are just keeping track of the variables, not discrete steps
        double ADMINHOURS = values[IADMINHOURS]; //
        double d2 = 0; //Penalty
        boolean constrained = true;
        if (constrained) {

            if (TRAFFIC < 0.0) {
                d2 += TRAFFIC * TRAFFIC;
                TRAFFIC = 0.0;
            }

            if (ADMINHOURS < 0.0) {
                d2 += ADMINHOURS * ADMINHOURS;
                ADMINHOURS = 0.0;
            }
            if (ADMINHOURS > 24.0) {
                d2 += ADMINHOURS * ADMINHOURS;
                ADMINHOURS = 24.0;
            }
            if (TRAFFIC > 24.0) {
                d2 += TRAFFIC * TRAFFIC;
                TRAFFIC = 24.0;
            }
        }
        return (-6 * Math.sin((TRAFFIC-6)/(2.4 * Math.PI))) + Math.pow(Math.cos((2 * ADMINHOURS)/(2.4 * Math.PI)), 2) + 1 + d2;  //Return the equation here that you're minimizing
    }
}
