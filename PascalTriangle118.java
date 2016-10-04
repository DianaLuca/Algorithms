package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.List;

/**
 * Given numRows, generate the first numRows of Pascal's triangle.
 * For example,
 *
 * given numRows = 5,
 * Return
 * [      [1],
 *      [1,  1],
 *    [1,  2,  1],
 *   [1, 3,  3,  1],
 *  [1, 4, 6,  4,  1]
 * ]
 *
 * Created by dianaluca on 10/4/16.
 */

public class PascalTriangle118 {
    //Dynamic Programming solution:
    public List<List<Integer>> generateDP(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (numRows == 0) return res;

        //Build the 2 base cases: for 1 row: [[1]] and for 2 rows: [[1],[1,1]]
        List<Integer> firstRow = new ArrayList<Integer>();
        firstRow.add(1);
        res.add(firstRow);
        if (numRows == 1) return res;

        List<Integer> secondRow = new ArrayList<Integer>();
        secondRow.add(1);
        secondRow.add(1);
        res.add(secondRow);
        if (numRows == 2) return res;

        //Loop to calculate rows(new ArrayList-s) up to whatever the given argument is:
        for(int i = 2; i < numRows; i++) {
            List<Integer> newList = new ArrayList<Integer>();

            for (int j = 0; j < res.get(i - 1).size() + 1; j++) {
                // force the beginning and the end of the new row to be 1
                if(j == 0 || j == res.get(i - 1).size()) {
                    newList.add(1);
                } else {
                    newList.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
                }
            }

            res.add(newList);
        }

        return res;

    }


//    public List<List<Integer>> generate(int numRows) {
// 		List<List<Integer>> res = new ArrayList<List<Integer>>();
// 		List<Integer> row, pre = null;
// 		for (int i = 0; i < numRows; ++i) {
// 			row = new ArrayList<Integer>();
// 			for (int j = 0; j <= i; ++j)
// 				if (j == 0 || j == i)
// 					row.add(1);
// 				else
// 					row.add(pre.get(j - 1) + pre.get(j));
// 			pre = row;
// 			res.add(row);
// 		}
// 		return res;
// 	}

}
