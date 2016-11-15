package Algorithms.related;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 *  Try running this program with the command:
 *  java Freq if it is to be it is up to me to delegate
 *
 * Created by dianaluca on 11/4/16.
 */

public class FrequencyMapWordToOccurence {

  public static void main(String[] args) {

    /** Solution 1: HashMap<>() </> unordered
     * The program yields the following output:
     * 8 distinct words:
     * {to=3, delegate=1, be=1, it=2, up=1, if=1, me=1, is=2}
     */
    //Map<String, Integer> map = new HashMap<String, Integer>();

    /** Solution 2: TreeMap<>() </> alphabetical order (since keys are Strings)
     * Suppose you'd prefer to see the frequency table in alphabetical order.
     * All you have to do is change the implementation type of the Map from HashMap to TreeMap.
     *
     * The program will generate the following output from the same command line.
     * 8 distinct words:
     * {be=1, delegate=1, if=1, is=2, it=2, me=1, to=3, up=1}
     */
    //Map<String, Integer> map = new TreeMap<String, Integer>();

    /** Solution 3: LinkedHashMap<>() </> in the order of its arguments in lexicographic (alphabetical) order.
     * Similarly, you could make the program print the frequency table in the order the words first appear on the command line
     * simply by changing the implementation type of the map to LinkedHashMap.
     *
     * Doing so results in the following output.
     * 8 distinct words:
     * {if=1, it=2, is=2, to=3, be=1, up=1, me=1, delegate=1}
     */
    Map<String, Integer> map = new LinkedHashMap<String, Integer>();


    //Initialize frequency table from command line
    for (String a : args) {
      Integer freq = map.get(a);
      map.put(a, (freq == null) ? 1 : freq + 1);
    }

    System.out.println(map.size() + " distinct words.");
    System.out.println(map);
  }
}
