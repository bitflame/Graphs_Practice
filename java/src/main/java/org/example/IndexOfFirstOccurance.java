package org.example;

public class IndexOfFirstOccurance {
    public int strStr(String haystack, String needle) {

        return -1;
    }
    public static void main(String[] args) {
        String hay = "sadbutsad";
        String ndl = "sad";
        IndexOfFirstOccurance io = new IndexOfFirstOccurance();
        System.out.printf("Test 1 - expected output: 0, actual: %d\n",io.strStr(hay, ndl));
        hay = "leetcode";
        ndl = "leeto";
        System.out.printf("Test 2 - expected output: -1, actual: %d\n",io.strStr(hay, ndl));
    }
}
