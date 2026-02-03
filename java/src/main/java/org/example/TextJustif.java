package org.example;

import java.util.ArrayList;
import java.util.List;

public class TextJustif {
    public List<String> fullJustify(String[] words, int maxWidth) {
        StringBuilder sb;
        List<String> result = new ArrayList<>();
        int end = 0, currWord = 0, wordsPerLine = 0;
        String separator = " ";
        while (currWord < words.length) {
            separator = " ";
            wordsPerLine = 0;
            sb = new StringBuilder();
            int remainder = 0;
            while (currWord < words.length && end + words[currWord].length() <= maxWidth) {
                end += words[currWord++].length() + 1;
                wordsPerLine++;
            }
            int additionalSpaces = maxWidth - (end - 1);
            if (currWord != words.length) {
                if (wordsPerLine > 1) remainder = additionalSpaces % (wordsPerLine - 1);
                if (additionalSpaces >= (wordsPerLine - 1) && wordsPerLine > 1) {
                    for (int i = 0; i <= additionalSpaces / (wordsPerLine - 1); i++) {
                        sb.append(separator);
                    }
                    separator = sb.toString();
                    sb = new StringBuilder();
                }
                int i = currWord - wordsPerLine;
                for (; i < currWord - 1; i++) {
                    sb.append(words[i]).append(separator);
                    if (remainder > 0) {
                        sb.append(" ");
                        remainder--;
                    }
                }
                sb.append(words[currWord - 1]);
                if (wordsPerLine == 1) {
                    while (sb.length() != maxWidth) {
                        sb.append(" ");
                    }
                }
            } else {
                // if we are at last line...
                separator = " ";
                int i = currWord - wordsPerLine;
                for (; i < currWord; i++) {
                    sb.append(words[i]).append(separator);
                }
                while (sb.length() != maxWidth) sb.append(" ");
            }
            // how to deal with the last line?
            result.add(sb.toString());
            end = 0;
        }
        return result;
    }


    public List<String> methodTwo(String[] words, int maxWidth) {
        StringBuilder sb = new StringBuilder();
        List<String> line = new ArrayList<>();
        List<String> result = new ArrayList<>();
        int totalChars = 0, currWordIndex = 0, gapIndex = 0;
        String separator = " ";
        String currentWord = "";
        while (currWordIndex < words.length) {
            currentWord = words[currWordIndex];
            if (totalChars + line.size() - 1 + currentWord.length() >= maxWidth) {
                if (line.size()==1) {
                    sb.append(line.removeFirst());
                    sb.append(separator.repeat(Math.max(0, maxWidth - (totalChars))));
                    line.add(sb.toString());
                    sb = new StringBuilder();
                } else {
                    for (int i = 0; totalChars < maxWidth; i++) {
                        sb.append(line.remove(i % (line.size() - 1)));
                        sb.append(separator);
                        line.add(i%(line.size()), sb.toString());
                        sb = new StringBuilder();
                        totalChars++;
                    }
                }
                for(String str: line) {
                    sb.append(str);
                }
                result.add(sb.toString());
                sb = new StringBuilder();
                line = new ArrayList<>();
                totalChars = 0;
            }
            line.add(currentWord);
            if (currWordIndex == words.length) {
                break;
            }
            totalChars += currentWord.length();
            currWordIndex++;
        }
        for (String seg : line) {
            sb.append(seg).append(separator);
        }
        totalChars = sb.length();
        sb.append(separator.repeat(Math.max(0, maxWidth - (totalChars))));
        result.add(sb.toString());
        return result;
    }

    public static void main(String[] args) {
        TextJustif tj = new TextJustif();
        String[] words = new String[]{"Science", "is", "what", "we", "understand", "well",
                "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
                "else", "we", "do"};
        for (String s : tj.methodTwo(words, 20)) {
            System.out.printf("\"%s\"\n", s);
        }
        words = new String[]{"This", "is", "an", "example", "of", "text", "justification"};
        int maxWidth = 16;
        for (String s : tj.methodTwo(words, 16)) {
            System.out.printf("\"%s\"\n", s);
        }
        words = new String[]{"What", "must", "be", "acknowledgment", "shall", "be"};
        for (String s : tj.methodTwo(words, 16)) {
            System.out.printf("\"%s\"\n", s);
        }

    }
}
