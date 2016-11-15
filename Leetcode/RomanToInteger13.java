package Algorithms.Leetcode;

import java.util.HashMap;

/**
 * Given a roman numeral, convert it to an integer.
 *
 * http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
 *
 * Input is guaranteed to be within the range from 1 to 3999
 * Created by dianaluca on 9/16/16.
 */

public class RomanToInteger13 {
  public static int romanToInt(String s) {
    int N = s.length();

    HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
    hm.put('I', 1);
    hm.put('V', 5);
    hm.put('X', 10);
    hm.put('L', 50);
    hm.put('C', 100);
    hm.put('D', 500);
    hm.put('M', 1000);

    int nr = 0;
    int pos = 0;
    if(N == 1) return (Integer) hm.get(s.charAt(pos));
    while(pos < N-1){
      int vali = hm.get(s.charAt(pos)) == null ? 0 : (Integer) hm.get(s.charAt(pos));
      int valb = hm.get(s.charAt(++pos)) == null ? 0 : (Integer) hm.get(s.charAt(pos));
      if (vali >= valb && pos == N-1) {
        nr += vali + valb;
      } else if(vali >= valb && pos != N-1) {
        nr += vali;
      } else{
        nr += valb - vali;
        pos++;
        if(pos == N-1) nr+= (Integer) hm.get(s.charAt(pos));
      }
    }
    return nr;

  }

  public static void main(String[] args) {
    int N = romanToInt("XLCIII");
    System.out.println(N);
  }

}
