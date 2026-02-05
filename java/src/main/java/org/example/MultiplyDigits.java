package org.example;


public class MultiplyDigits {
    public static int mult(int value) {
        if (value==0) return 1;
        int digit = value % 10;
        int quotient = value / 10;
        return digit * mult(quotient);
    }

    public static void main(String[] args) {
        System.out.printf("%d\n", mult(257));
    }
}
