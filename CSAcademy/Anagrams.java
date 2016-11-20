package Algorithms.CSAcademy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

/**
 * You are given a list of NN words (strings containing only lower case letters of the English alphabet).
 * We consider two words to be equivalent if they contain the same letters,
 * i.e. we can rearrange the letters of one word in order to obtain the other word.
 * Compute the size of the largest subset of equivalent words.
 *
 * Desired solution
 * You should assume the input is quite large (there are about 10^5 letters in total).
 *
 * https://csacademy.com/contest/interview-archive/#task/anagrams/
 *
 * Created by dianaluca on 11/12/16.
 */
public class Anagrams {
  /**
   * 2 approaches:
   *
   * 1) Use hash. O(input), but chance of failing in case of hash function collision
   * 2) Use sorted form of a word as the key. No chance of failing, but complexity goes up to O(MAX_LENGTH log MAX_LENGTH)
   *
   */

  public static int hashWord(String word) {
    int len = word.length();
    int sum = 0;
    int xor = 0;
    int sqSum = 0;

    for(int i = 0; i < len; i++) {
      int val = Character.getNumericValue(word.charAt(i));
      sum += val;
      xor ^= val;
      sqSum += val * val;
    }
    return sum * 11111 + xor * 11 + sqSum * 24213;
    //return sqSum;
  }

  public static String sortWord(String word) {
    char[] chars = word.toCharArray();
    Arrays.sort(chars);
    return new String(chars);
  }

  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>(N);
    HashMap<String, Integer> hmSorted = new HashMap<String, Integer>(N);

    for (int i = 0; i < N; ++i) {
      String currWord = sc.next();

      int hashW = hashWord(currWord);
      int val = hm.get(hashW) == null ? 0 : (Integer) hm.get(hashW);
      hm.put(hashW, ++val);

      String sortedW = sortWord(currWord);

      int valSort = hmSorted.get(sortedW) == null ? 0 : (Integer) hmSorted.get(sortedW);
      hmSorted.put(sortedW, ++valSort);
    }

    Set<Integer> keys = hm.keySet();
    int maxVal = Integer.MIN_VALUE;
    for(Integer key : keys) {
      maxVal = Math.max(maxVal, hm.get(key));
    }

//         Set<String> sortedKeys = hmSorted.keySet();
// 		int maxAn = Integer.MIN_VALUE;
//         for(String key : sortedKeys) {
//             maxAn = Math.max(maxAn, hm.get(key));
//         }

    // int maxVal = 0;
    // for (String key : hmSorted.keySet()) {
    //     maxVal = Math.max(maxVal, hmSorted.get(key));
    // }
    System.out.println(maxVal);

  }
}
