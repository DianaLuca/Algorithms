package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * Write a program that outputs the string representation of numbers from 1 to n.
 * But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
 * For numbers which are multiples of both three and five output “FizzBuzz”.
 *
 * Created by dianaluca on 11/8/16.
 */

public class FizzBuzz412 {
  public List<String> fizzBuzz(int n) {
    List<String> fizzbuzz = new ArrayList<String>();

    for (int i = 1; i<=n; i++ ) {
      if (i % 3 == 0 && i % 5 == 0) {
        fizzbuzz.add("FizzBuzz");
      } else {
        if (i % 3 == 0) fizzbuzz.add("Fizz");
        else if (i % 5 == 0) fizzbuzz.add("Buzz");
        else fizzbuzz.add("" + i);
      }
    }
    return fizzbuzz;
  }
}
