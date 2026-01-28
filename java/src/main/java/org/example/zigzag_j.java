package org.example;

import java.util.ArrayList;
import java.util.List;

public class zigzag_j {
    public String zigzag(String s, int numRows) {
        if (numRows == 1) return s;
        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }
        int i = 0;
        int d = 1;
        for (char c : s.toCharArray()) {
            rows.get(i).append(c);
            if (i == 0) d = 1;
            else if (i == numRows - 1) d = -1;
            i += d;
        }
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }
        return result.toString();
    }

    public static void main(String[] args) {

    }
}
