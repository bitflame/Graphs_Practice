package org.example;

public class IndexOfFirstOccurrence {
    public int strStr(String haystack, String needle) {
        int n = needle.length(), pattern = 0, text = 0, m = haystack.length(), startOfMatch = 0;
        if (n > m) return -1;
        while (text < m && pattern < n) {
            if (needle.charAt(pattern) == haystack.charAt(text)) {
                startOfMatch = text;
                while (text < m && pattern < n && needle.charAt(pattern) == haystack.charAt(text)) {
                    text++;
                    pattern++;
                }
                if (pattern == n) return text - n;
                else {
                    pattern = 0;
                    text = startOfMatch + 1;
                }
            }
            while (text < m && needle.charAt(pattern) != haystack.charAt(text)) {
                text++;
            }
        }
        return pattern == n ? text - n : -1;
    }

    public int sidgwickBruteForce(String haystack, String needle) {
        int j, M = needle.length();
        int i, N = haystack.length();
        for (i = 0, j = 0; i < N && j < M; i++) {
            if (haystack.charAt(i) == needle.charAt(j)) j++;
            else {
                i -= j;
                j = 0;
            }

        }
        if (j == M) return i - M;
        else return -1;
    }

    public static void main(String[] args) {
        String hay = "sadbutsad";
        String ndl = "sad";
        IndexOfFirstOccurrence io = new IndexOfFirstOccurrence();
        System.out.printf("Test 1 - expected output: 0, actual: %d\n", io.strStr(hay, ndl));
        System.out.printf("Test 1 - Sidgwick expected output: 0, actual: %d\n", io.sidgwickBruteForce(hay, ndl));
        hay = "leetcode";
        ndl = "leeto";
        System.out.printf("Test 2 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
        System.out.printf("Test 2 - Sidgwick expected output: -1, actual: %d\n", io.sidgwickBruteForce(hay, ndl));
        hay = "mississippi";
        ndl = "issip";
        System.out.printf("Test 3 - expected output: 4, actual: %d\n", io.strStr(hay, ndl));
        System.out.printf("Test 3 - Sidgwick expected output: 4, actual: %d\n", io.sidgwickBruteForce(hay, ndl));
        ndl = "issipi"; // hay is the same for this test
        System.out.printf("Test 4 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
        System.out.printf("Test 4 - Sidgwick expected output: -1, actual: %d\n", io.sidgwickBruteForce(hay, ndl));
        hay = "aaa";
        ndl = "aaaa";
        System.out.printf("Test 5 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
        System.out.printf("Test 5 - Sidgwick expected output: -1, actual: %d\n", io.sidgwickBruteForce(hay, ndl));
    }
}
