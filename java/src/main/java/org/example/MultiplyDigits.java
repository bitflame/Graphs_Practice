package org.example;


public class MultiplyDigits {
    public static int mult(int value) {
        if (value==0) return 1;
        int digit = value % 10;
        int quotient = value / 10;
        return digit * mult(quotient);
    }
    // this is the tail recursive version of this method
    public static int tail_rec_mult(int value, int acc) {
        if (value==0) return acc;
        return tail_rec_mult(value/10,value%10*acc);
    }
    public static void main(String[] args) {
        System.out.printf("%d\n", mult(257));
        System.out.printf("%d\n", tail_rec_mult(257,1));
    }
}
