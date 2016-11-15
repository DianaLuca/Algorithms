package Algorithms.related;

import java.util.List;

/**
 * Created by dianaluca on 11/4/16.
 */
public class SwapTwoIndexedValuesInAList {
  public static <E> void swap(List<E> a, int i, int j) {
    E tmp = a.get(i);
    a.set(i, a.get(j));
    a.set(j, tmp);
  }
}
