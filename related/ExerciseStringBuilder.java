package LeetCodeAlgorithms.related;

/**
 * Created by dianaluca on 9/24/16.
 */
public class ExerciseStringBuilder {
  public static void main(String[] args) {
    String s = "hello";

    StringBuilder sb = new StringBuilder(s);
    System.out.println(sb.toString());

    sb.deleteCharAt(1);
    sb.insert(1, 'o');
    System.out.println("after sb.deleteCharAt(1) and sb.insert(1, 'o') : " + sb.toString()); //print "hollo"
  }
}
