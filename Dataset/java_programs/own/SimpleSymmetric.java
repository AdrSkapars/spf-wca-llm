package own;

import gov.nasa.jpf.symbc.Debug;

public class SimpleSymmetric {

    public static void algo(int[][] A) {
        boolean fail = false;
        boolean skip = false;
        final int N = A.length;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i][j] == A[j][i]){
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
        final int A[][] = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = Debug.makeSymbolicInteger("in"+i+"x"+j);
            }
        }

        // We only measure the complexity of this function itself.
        algo(A);
    }
}