package org.example;
import java.util.*;

public class MergeIntervals {
    Map<int[], List<int[]>> graph;
    Map<Integer, List<int[]>> cc;

    public void buildGraph(int[][] intervals) {
        graph = new HashMap<>();
        int n = intervals.length;
        for (int[] node : intervals) {
            graph.put(node, new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && overlaps(intervals[i], intervals[j])) {
                    graph.get(intervals[i]).add(intervals[j]);
                }
            }
        }
    }

    private boolean overlaps(int[] a, int[] b) {
        return a[0] <= b[1] && b[0] <= a[1];
    }

    public int[][] mergeIntervals(int[][] intervals) {
        int[][] result = new int[graph.size()][];
        int rowCounter = 0;
        for (int[] node : graph.keySet()) {
            for (int[] child : graph.get(node)) {
                result[rowCounter] = new int[2];
                result[rowCounter][0] = Math.min(node[0], child[0]);
                result[rowCounter][1] = Math.max(node[1], child[1]);
                rowCounter++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        MergeIntervals mi = new MergeIntervals();
        int[][] ints = new int[][]{{2, 5}, {1, 4}, {9, 10}, {6, 9}};
        int[] a = new int[]{2, 5};
        int[] b = new int[]{1, 4};
        System.out.println(mi.overlaps(a, b));
        mi.buildGraph(ints);
        for(int[] merged: mi.mergeIntervals(ints)){
            System.out.println(Arrays.toString(merged));
        }
    }
}
