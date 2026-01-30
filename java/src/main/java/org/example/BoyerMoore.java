package org.example;

public class BoyerMoore {
    // Boyer More from Sedgewick and Wayne
    public int indexOf(String haystack, String needle) {
        int M = needle.length();
        int N = haystack.length();
        int R = 256;
        int[] right = new int[R];
        for (int c = 0; c < R; c++) {
            right[c] = -1;
        }
        for (int j = 0; j < M; j++) {
            right[needle.charAt(j)] = j;
        }
        int skip;
        for (int i = 0; i <=N-M ; i++) {
            skip=0;
            for (int j = M-1; j >=0 ; j--) {
                if (needle.charAt(j)!= haystack.charAt(i+j)){
                    skip = j - right[haystack.charAt(i+j)];
                    if (skip<1) skip = 1;
                    break;
                }
            }
            if (skip==0) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        String hay = "sadbutsad";
        String ndl = "sad";
        BoyerMoore bm = new BoyerMoore();
        System.out.printf("Test 1 - expected output: 0, actual: %d\n", bm.indexOf(hay, ndl));
        hay = "leetcode";
        ndl = "leeto";
        System.out.printf("Test 2 - expected output: -1, actual: %d\n", bm.indexOf(hay, ndl));
        hay = "mississippi";
        ndl = "issip";
        System.out.printf("Test 3 - expected output: 4, actual: %d\n", bm.indexOf(hay, ndl));
        ndl = "issipi"; // hay is the same for this test
        System.out.printf("Test 4 - expected output: -1, actual: %d\n", bm.indexOf(hay, ndl));
        hay = "aaa";
        ndl = "aaaa";
        System.out.printf("Test 5 - expected output: -1, actual: %d\n", bm.indexOf(hay, ndl));
    }
}
