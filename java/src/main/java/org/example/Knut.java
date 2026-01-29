package org.example;

import java.nio.charset.StandardCharsets;

public class Knut {
    // this is kmp
    private String pat;
    private int[][] dfa;

    public Knut(String pat) {
        this.pat = pat;
        int M = pat.length();
        int R = 256;
        dfa = new int[R][M];
        dfa[pat.charAt(0)][0] = 1;
        for (int X = 0, j = 1; j < M; j++) {
            for (int c = 0; c < R; c++)
                dfa[c][j] = dfa[c][X];
            dfa[pat.charAt(j)][j] = j + 1;
            X = dfa[pat.charAt(j)][X];
        }
        System.out.println("end");
    }

    public int search(String txt) {
        int i, j, N = txt.length(), M = pat.length();
        for (i = 0, j = 0; i < N && j < M; i++)
            j = dfa[txt.charAt(i)][j];
        if (j == M) return i - M;
        else return N;
    }

    public int combined(String haystack, String needle) {
        int M = needle.length();
        int R = 256;
        int[][] dfa = new int[R][M];
        dfa[needle.charAt(0)][0] = 1;
        for (int X = 0, j = 1; j < M; j++) {
            for (int c = 0; c < R; c++)
                dfa[c][j] = dfa[c][X];
            dfa[needle.charAt(j)][j] = j + 1;
            X = dfa[needle.charAt(j)][X];
        }
        int i, j, N = haystack.length();
        for (i = 0, j = 0; i < N && j < M; i++)
            j = dfa[haystack.charAt(i)][j];
        if (j == M) return i - M;
        else return -1;
    }

    public static void main(String[] args) {
        Knut k = new Knut("ABABAC");
        String hay = "sadbutsad";
        String ndl = "sad";
        System.out.printf("Test 1 - expected output: 0, actual: %d\n", k.combined(hay, ndl));
        hay = "leetcode";
        ndl = "leeto";
        System.out.printf("Test 2 - expected output: -1, actual: %d\n", k.combined(hay, ndl));
        hay = "mississippi";
        ndl = "issip";
        System.out.printf("Test 3 - expected output: 4, actual: %d\n", k.combined(hay, ndl));
        ndl = "issipi"; // hay is the same for this test
        System.out.printf("Test 4 - expected output: -1, actual: %d\n", k.combined(hay, ndl));
        hay = "aaa";
        ndl = "aaaa";
        System.out.printf("Test 5 - expected output: -1, actual: %d\n", k.combined(hay, ndl));
    }
}
