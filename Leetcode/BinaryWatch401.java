package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * A binary watch has 4 LEDs on the top which represent the hours (0-11),
 * and the 6 LEDs on the bottom represent the minutes (0-59).
 * Each LED represents a zero or one,
 * with the least significant bit on the right.
 *
 * Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
 * Example:
 * Input: n = 1
 * Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 *
 * Created by dianaluca on 9/22/16.
 */

public class BinaryWatch401 {
  public static List<String> readBinaryWatch(int num) {
    List<String> timeIs = new ArrayList<String>();
    for (int h = 0; h < 12; ++h) {
      for (int m = 0; m < 60; ++m ) {
        if (Integer.bitCount(h) + Integer.bitCount(m) == num)
          timeIs.add(String.format("%d:%02d",h,m));
      }
    }
    return timeIs;
  }

  public static void main(String[] args) {
    List<String> time = readBinaryWatch(5);
    for(String hour : time)
      System.out.println(hour);
  }
}
