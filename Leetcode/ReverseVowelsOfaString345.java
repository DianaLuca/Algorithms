package Algorithms.Leetcode;

/**
 * Write a function that takes a string as input and reverse only the vowels of a string.
 * Example 1:
 * Given s = "hello", return "holle".
 *
 * Created by dianaluca on 9/25/16.
 */

public class ReverseVowelsOfaString345 {
  public static boolean isVowel (Character c) {
    return "AEIOUaeiou".indexOf(c) != -1;
  }

  public static void swap(char[] arrS, int i, int j){
    char tmp = arrS[i];
    arrS[i] = arrS[j];
    arrS[j] = tmp;
  }

  public static String reverseVowels(String s) {
    if (s == "") return s;
    int N = s.length();
    char[] arrS = new char[N];
    for(int i = 0; i<N; i++){
      arrS[i] = s.charAt(i);
    }

    int i = 0;
    int j = N - 1;
    while (i < N && j >= 0 && i <= j ) {
      boolean vowelI = isVowel(s.charAt(i));
      boolean vowelJ = isVowel(s.charAt(j));
      if (vowelI && vowelJ) {
        swap(arrS, i, j);
        i++;
        j--;
      } else if (vowelI && !vowelJ) {
        j--;
      } else {
        i++;
      }
    }

    StringBuilder sb = new StringBuilder();
    for(int k = 0; k < N; k++){
      sb.append(arrS[k]);
    }

    return sb.toString();
  }

  public static void main(String[] args) {
    System.out.println(reverseVowels("hello")); //should print "holle"
    System.out.println(reverseVowels("Aa")); // should print "aA"
  }
}
