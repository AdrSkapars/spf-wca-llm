package own;

import gov.nasa.jpf.symbc.Debug;

public class WeirdLoopMean {

    public static void algo(int[] a) {
        final int N = a.length;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += a[i];
        }
        int mean = (int) (sum/N);
        int aa = 999;
        for (int i = 0; i < mean; i++) {
            aa = aa*aa;
        }
    }

    public static void main(String[] args) {
        final int N = Integer.parseInt(args[0]);

        int a[] = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = Debug.makeSymbolicInteger("in"+i);
        }

        // We only measure the complexity of this function itself.
        algo(a);
    }
}
