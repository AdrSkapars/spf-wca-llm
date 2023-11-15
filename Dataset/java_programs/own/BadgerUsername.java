package own;

import gov.nasa.jpf.symbc.Debug;

import java.util.regex.*;

// public class BadgerUsername {

//     public static void algo(String str) {
//         Pattern pattern = Pattern.compile("^[a-z0-9_]{3,15}$");
//         Matcher matcher = pattern.matcher(str);
//         boolean matches = matcher.matches();

//         // final int N = str.length();
//         // if (matches) {
//         //     int aa = 99999;
//         //     for (int i = 0; i < N; i++) {
//         //         aa = aa*aa;
//         //     }
//         // }
//     }

//     public static void main(String[] args) {
//         final int N = Integer.parseInt(args[0]);
//         String str = Debug.makeSymbolicString("in", N);

//         // We only measure the complexity of this function itself.
//         algo(str);
//     }
// }

public class BadgerUsername {

    public static boolean algo(char[] chars) {
        if (chars.length < 3 || chars.length > 15) {
            return false;
        }

        for (char c : chars) {
            if (!(Character.isLowerCase(c) || Character.isDigit(c) || c == '_' || c == '-')) {
                return false;
            }
        }
        return true;

        // boolean fail = false;
        // boolean skip = false;
        // final int N = chars.length;
        // for (int i = 0; i < N; i++) {
        //     if (chars[i] >= 'a' && chars[i] <= 'z'){
        //         // Skip
        //         skip = true;
        //     } else {
        //         fail = true;
        //     }
        // }
        // if (!fail) {
        //     int aa = 99999;
        //     for (int i = 0; i < N; i++) {
        //         aa = aa*aa;
        //     }
        // }
    }

    public static void main(String[] args) {
        final int N = Integer.parseInt(args[0]);

        char[] chars = new char[N];
        for (int i=0;i<N;i++)
            chars[i]=Debug.makeSymbolicChar("in"+i);

        // We only measure the complexity of this function itself.
        boolean out = algo(chars);
    }
}