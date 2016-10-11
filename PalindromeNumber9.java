package LeetCodeAlgorithms;

/**
 * Determine if an integer is a palindrome.
 * Do this without extra-space.
 *
 * You could also try reversing an integer.
 * However, if you have solved the problem "reverse integer", you know that the reversed integer might overflow.
 * How would you handle such case?
 *
 * Created by dianaluca on 10/11/16.
 */

public class PalindromeNumber9 {
  public static boolean isPalindrome(int x) {
    if (x < 0) return false;

    int p, q;
    p = x;
    q = 0; // q could be the reverse of x if while condition would be while (p >= 0)

    while (p >= 10) {
      q *= 10;
      q += p % 10;
      p /= 10;
    }

    return (q == x/10) && (p == x % 10);
  }

  public static void main(String[] args) {
    System.out.println("1221 is palindrome? : " + isPalindrome(1221) +
        "\n1234 is palindrome? : " + isPalindrome(1234));

    int index = '8' - '0' - 1;
    System.out.println(index);

    /**
     * O(1) space, O(lgn) time, no overflow risk.
     *
     * print:
     * 1221 is palindrome? : true
     * 1234 is palindrome? : false
     *
     */
  }
}
