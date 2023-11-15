package own;

import gov.nasa.jpf.symbc.Debug;

// public class SameChar {

//     public static void algo(String str) {
//         boolean fail = false;
//         boolean skip = false;
//         final int N = str.length();
//         for (int i = 0; i < N; i++) {
//             if (str.charAt(i) == 'x'){
//                 // Skip
//                 skip = true;
//             } else {
//                 fail = true;
//             }
//         }
//         if (!fail) {
//             int aa = 99999;
//             for (int i = 0; i < N; i++) {
//                 aa = aa*aa;
//             }
//         }
//     }

//     public static void main(String[] args) {
//         final int N = Integer.parseInt(args[0]);

//         char[] chars = new char[N];
//         for (int i=0;i<N;i++)
//             chars[i]=Debug.makeSymbolicChar("in"+i);
//         String str = new String(chars);

//         // We only measure the complexity of this function itself.
//         algo(str);
//     }
// }

public class SameLowercase {

    public static void algo(char[] chars) {
        boolean fail = false;
        boolean skip = false;
        final int N = chars.length;
        for (int i = 0; i < N; i++) {
            if (chars[i] >= 'a' && chars[i] <= 'z'){
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

        char[] chars = new char[N];
        for (int i=0;i<N;i++)
            chars[i]=Debug.makeSymbolicChar("in"+i);

        // We only measure the complexity of this function itself.
        algo(chars);
    }
}