package Algorithms.related;

/**
 * Created by dianaluca on 10/5/16.
 */

public class ResizeArray {
  public int[] a;

  public void resize(int capacity){
    assert (capacity >= a.length);

    int[] tmp = new int[capacity];
    for(int i = 0; i < a.length; i++){
      tmp[i] = a[i];
    }

    a = tmp;
  }

  public static void main(String[] args) {

  }
}
