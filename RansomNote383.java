package LeetCode;

import java.util.HashMap;

/**
 * Given  an  arbitrary  ransom  note  string
 *  and  another  string  containing  letters from  all  the  magazines, 
 * write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   
 * Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

 * Note:
 * You may assume that both strings contain only lowercase letters.

 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 *
 * Created by dianaluca on 9/14/16.
 */

public class RansomNote383 {

  public static boolean canConstruct(String ransomNote, String magazine) {
    //if ransomNote included in magazine
    HashMap hm = new HashMap<String, Integer>();

    for(int i = 0; i < magazine.length(); i++) {
      //conditional: max = (a > b) ? a : b;
      int val = hm.get(magazine.charAt(i)) == null ? 0 : (Integer)hm.get(magazine.charAt(i));
      hm.put(magazine.charAt(i), val + 1);
    }

    for(int j = 0; j < ransomNote.length(); j++) {
      int val = hm.get(ransomNote.charAt(j)) == null ? 0 : (Integer)hm.get(ransomNote.charAt(j));
      if (val == 0) {
        return false;
      } else
        hm.put(ransomNote.charAt(j), val - 1);
    }
    return true;
  }

  public static void main(String[] args){
    System.out.println(canConstruct("aab", "afgab"));
  }
}
