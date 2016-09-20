package LeetCode;

/**Write a function that takes a string as input and returns the string reversed.

 Example:
 Given s = "hello", return "olleh".

 * Created by dianaluca on 9/15/16.
 */


public class ReverseString344 {
  public String reverseString(String s) {

    return new StringBuilder(s).reverse().toString();
  }
}
