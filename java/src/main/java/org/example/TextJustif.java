package org.example;

import java.util.ArrayList;
import java.util.List;

public class TextJustif {
    public List<String> methodTwo(String[] words, int maxWidth) {
        List<String> line = new ArrayList<>();
        List<String> result = new ArrayList<>();
        int totalChars = 0, curr = 0;
        while (curr < words.length) {
            String word = words[curr];
            // check if adding this word exceeds width
            if (totalChars + word.length() + line.size() > maxWidth) {
                result.add(justify(line, totalChars, maxWidth));
                line = new ArrayList<>();
                totalChars = 0;
            }
            line.add(word);
            totalChars += word.length();
            curr++;
        }
        // last line -> left justify
        result.add(leftJustify(line, maxWidth));
        return result;
    }

    private String justify(List<String> line, int totalChar, int maxWidth) {
        if (line.size() == 1) return leftJustify(line, maxWidth);
        int gaps = line.size() - 1;
        int spaces = maxWidth - totalChar;
        int even = spaces / gaps;
        int extra = spaces % gaps;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < line.size(); i++) {
            // It looks like you do not have to remove the string from the list to update it - Good to know
            // todo - watch it do this in debug
            sb.append(line.get(i));
            if (i<gaps){
                int count = even + (extra-- > 0? 1:0);
                sb.append(" ".repeat(count));
            }
        }
        return sb.toString();
    }

    private String leftJustify(List<String>line, int maxWidth) {
        StringBuilder sb = new StringBuilder();

        while(sb.length()<maxWidth) sb.append(" ");
        return sb.toString();
    }

    public List<String> optimized_AI_generated(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int curr = 0;

        while (curr < words.length) {
            int start = curr;
            int totalChars = words[curr].length();
            curr++;

            // Collect as many words as fit
            while (curr < words.length &&
                    totalChars + 1 + words[curr].length() <= maxWidth) {
                totalChars += 1 + words[curr].length();
                curr++;
            }

            int end = curr - 1;
            int numWords = end - start + 1;

            StringBuilder sb = new StringBuilder();

            // Last line or single word → left justify
            if (curr == words.length || numWords == 1) {
                for (int i = start; i <= end; i++) {
                    sb.append(words[i]);
                    if (i < end) sb.append(' ');
                }
                while (sb.length() < maxWidth) sb.append(' ');
                result.add(sb.toString());
                continue;
            }

            // Fully justify
            int totalWordLength = 0;
            for (int i = start; i <= end; i++) totalWordLength += words[i].length();

            int spaces = maxWidth - totalWordLength;
            int gaps = numWords - 1;

            int even = spaces / gaps;
            int extra = spaces % gaps;

            for (int i = start; i <= end; i++) {
                sb.append(words[i]);
                if (i < end) {
                    int count = even + (extra-- > 0 ? 1 : 0);
                    sb.append(" ".repeat(count));
                }
            }

            result.add(sb.toString());
        }

        return result;

    }

    public static void main(String[] args) {
        TextJustif tj = new TextJustif();
        List<String> test = new ArrayList<>();
        test.add("Test");
        System.out.printf("List size is: %d when there is 1 segment in the list.\n", test.size());
        String[] words = new String[]{"Science", "is", "what", "we", "understand", "well",
                "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
                "else", "we", "do"};
        System.out.println("Test 1 result: ");
        for (String s : tj.methodTwo(words, 20)) {
            System.out.printf("\"%s\"\n", s);
        }
        System.out.println("Test 2 result: ");
        words = new String[]{"This", "is", "an", "example", "of", "text", "justification"};
        int maxWidth = 16;
        for (String s : tj.methodTwo(words, 16)) {
            System.out.printf("\"%s\"\n", s);
        }
        System.out.println("Test 3 result: ");
        words = new String[]{"What", "must", "be", "acknowledgment", "shall", "be"};
        for (String s : tj.methodTwo(words, 16)) {
            System.out.printf("\"%s\"\n", s);
        }
        words = new String[]{"ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask",
                "what", "you", "can", "do", "for", "your", "country"};
        System.out.println("Test 4 result: ");
        for (String s : tj.methodTwo(words, 16)) {
            System.out.printf("\"%s\"\n", s);
        }
        words = new String[]{"a"};
        System.out.println("Test 5 result: ");
        for (String s : tj.methodTwo(words, 1)) {
            System.out.printf("\"%s\"\n", s);
        }
    }
}
