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
            while (end + words[currWord].length() <= maxWidth) {
                end += words[currWord++].length() + 1;
                wordsPerLine++;
            }
            int additionalSpaces = maxWidth - (end - 1);
            if (currWord != words.length) {
                int remainder = additionalSpaces % wordsPerLine;
                for (int i = 0; i <= additionalSpaces / (wordsPerLine - 1); i++) {
                    sb.append(separator);
                }
                separator = sb.toString();
                sb = new StringBuilder();
                int i = 0;
                for (; i < wordsPerLine - 1; i++) {
                    sb.append(words[i]).append(separator);
                    if (remainder > 0) {
                        sb.append(" ");
                        remainder--;
                    }
                }
                sb.append(words[i]);
            } else {
                // if we are at last line...
                separator = " ";
                for (int i = 0; i < wordsPerLine; i++) {
                    sb.append(words[i]).append(separator);
                }
                while (sb.length() < maxWidth) sb.append(separator);
            }
            // how to deal with the last line?
            result.add(sb.toString());
            end = 0;
        }
        return result;
    }

    public static void main(String[] args) {
        TextJustif tj = new TextJustif();
        String[] words = {"This", "is", "an", "example", "of", "text", "justification"};
        int maxWidth = 16;
        for (String s : tj.fullJustify(words, 16)) {
            System.out.printf("%s\n", s);
        }
    }
}
