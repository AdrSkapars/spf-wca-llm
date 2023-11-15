package own;

import gov.nasa.jpf.symbc.Debug;

public class SimpleTrueFalse {

    public static void algo(boolean[] a) {
        boolean fail = false;
        boolean skip = false;
        final int N = a.length;
        for (int i = 0; i < N; i++) {
            if (i % 2 == 0) {
                if (a[i] == true){
                    // Skip
                    skip = true;
                } else {
                    fail = true;
                }
            } else {
                if (a[i] == false){
                    // Skip
                    skip = true;
                } else {
                    fail = true;
                }
            }
        }
        if (!fail) {
            int aa = 99999;
            for (int i = 0; i < N; i++) {
                aa = aa*aa;
            }
        }
    }

    public static void main(String[] args) {
        final int N = Integer.parseInt(args[0]);

        boolean a[] = new boolean[N];
        for (int i = 0; i < N; i++) {
            a[i] = Debug.makeSymbolicBoolean("in"+i);
        }

        // We only measure the complexity of this function itself.
        algo(a);
    }
}