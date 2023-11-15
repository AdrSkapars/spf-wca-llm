package own;

import gov.nasa.jpf.symbc.Debug;

public class WeirdNotFactor {
    // public static int binaryModulo(int dividend, int divisor) {
    //     // Won't handle negatives right but just need to check if output is 0
    //     dividend = Math.abs(dividend);
    //     divisor = Math.abs(divisor);

    //     int result = 0;

    //     while (dividend >= divisor) {
    //         int tempDivisor = divisor;
    //         int multiple = 1;

    //         while (dividend >= tempDivisor) {
    //             dividend -= tempDivisor;
    //             result += multiple;

    //             tempDivisor <<= 1;
    //             multiple <<= 1;
    //         }
    //     }

    //     return dividend;
    // }


    // public static int manualModulo(int dividend, int divisor) {
    //     dividend = Math.abs(dividend);
    //     divisor = Math.abs(divisor);

    //     while (dividend >= divisor) {
    //         dividend -= divisor;
    //     }

    //     return dividend;
    // }

    public static void algo(int[] a) {
        boolean fail = false;
        boolean skip = false;
        final int N = a.length;
        for (int i = 0; i < N; i++) {
            // if (i != 0 && a[i] % a[i-1] != 0){
            // if (i != 0 && manualModulo(a[i],a[i-1]) != 0){
            // if (i != 0 && binaryModulo(a[i],a[i-1]) != 0){
            if (i != 0 && Math.floor(a[i]/a[i-1]) == Math.ceil(a[i]/a[i-1])){
                // Skip
                skip = true;
            } else {
                fail = true;
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

        int a[] = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = Debug.makeSymbolicInteger("in"+i);
        }

        // We only measure the complexity of this function itself.
        algo(a);
    }
}
