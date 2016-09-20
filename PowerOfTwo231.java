package LeetCode;

/**
 * Created by dianaluca on 9/18/16.
 */
public class PowerOfTwo231 {
  public static boolean power(int nr) {
    if(nr == 1 ) return true;
    if (nr == 0 || nr%2 != 0) return false;
    return power(nr / 2);
  }

  public static void main(String[] args){
    System.out.println("64 is power of 2? " + power(64));
  }
}
