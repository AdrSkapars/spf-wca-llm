package own;

import gov.nasa.jpf.symbc.Debug;

public class BadgerPassword {

    public static boolean algo(char[] chars) {
        boolean hasDigit = false;
        boolean hasLowercase = false;
        boolean hasUppercase = false;
        boolean hasSpecialChar = false;

        if (chars.length < 3 || chars.length > 10) {
            return false;
        }

        for (int i=0; i<chars.length; i++) {
            if (Character.isDigit(chars[i])) {
                hasDigit = true;
            } else if (Character.isLowerCase(chars[i])) {
                hasLowercase = true;
            } else if (Character.isUpperCase(chars[i])) {
                hasUppercase = true;
            } else if (chars[i] == '@' || chars[i] == '#' || chars[i] == '$' || chars[i] == '%') {
                hasSpecialChar = true;
            }
            // if (hasDigit && hasLowercase && hasUppercase && hasSpecialChar){
            //     int aa = 99999;
            //     for (int j = 0; j < chars.length; j++) {
            //         aa = aa*aa;
            //     }
            //     return true;
            // }
        }

        return hasDigit && hasLowercase && hasUppercase && hasSpecialChar;

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