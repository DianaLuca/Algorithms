package Algorithms.Hackerrank;
import java.util.*;

/**
 * Given the words in the magazine and the words in the ransom note,
 * print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
 *
 * The first line contains two space-separated integers describing the respective values of m (the number of words in the magazine)
 * and n (the number of words in the ransom note).
 * The second line contains m space-separated strings denoting the words present in the magazine.
 * The third line contains n space-separated strings denoting the words present in the ransom note.
 *
 * Created by dianaluca on 11/16/16.
 */
public class RansomNote {
  Map<String, Integer> magazineMap;
  Map<String, Integer> noteMap;

  public RansomNote(String magazine, String note) {
    magazineMap = new HashMap<String, Integer>();
    for(String word : magazine.split(" ")) {
      int val = magazineMap.get(word) == null ? 0 : magazineMap.get(word);
      magazineMap.put(word, val+1);
    }

    noteMap = new HashMap<String, Integer>();
    for(String word : note.split(" ")) {
      int val = noteMap.get(word) == null ? 0 : noteMap.get(word);
      noteMap.put(word, val+1);
    }
  }

  public boolean solve() {
    for(String key : noteMap.keySet()) {
      if (magazineMap.containsKey(key) && noteMap.get(key) <= magazineMap.get(key)) continue;
      else return false;
    }
    return true;
  }

  /**
   * Sample Input:
   * 6 4
   * give me one grand today night
   * give one grand today
   *
   * Sample Output: Yes
   * @param args
   */
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int m = scanner.nextInt();
    int n = scanner.nextInt();

    // Eat whitespace to beginning of next line
    scanner.nextLine();

    RansomNote s = new RansomNote(scanner.nextLine(), scanner.nextLine());
    scanner.close();

    boolean answer = s.solve();
    if(answer)
      System.out.println("Yes");
    else System.out.println("No");
  }

}
