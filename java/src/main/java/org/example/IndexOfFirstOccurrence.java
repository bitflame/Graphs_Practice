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

    public static void main(String[] args) {
        String hay = "sadbutsad";
        String ndl = "sad";
        IndexOfFirstOccurrence io = new IndexOfFirstOccurrence();
        System.out.printf("Test 1 - expected output: 0, actual: %d\n", io.strStr(hay, ndl));
        hay = "leetcode";
        ndl = "leeto";
        System.out.printf("Test 2 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
        hay = "mississippi";
        ndl = "issip";
        System.out.printf("Test 3 - expected output: 4, actual: %d\n", io.strStr(hay, ndl));
        ndl = "issipi"; // hay is the same for this test
        System.out.printf("Test 4 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
        hay = "aaa";
        ndl = "aaaa";
        System.out.printf("Test 5 - expected output: -1, actual: %d\n", io.strStr(hay, ndl));
    }
}
