package Algorithms.CSAcademy;

import java.util.Scanner;

/**
 * You have recently caught N Pokémon and you also have M Pokémon candy bars.
 * You can evolve any of your Pokémon by paying X candy bars.
 * Alternatively, you can sell any of your Pokémon for a price of Y candy bars.
 * You cannot sell an evolved Pokémon.
 * Compute the maximum number of Pokémon you can evolve.
 *
 * https://csacademy.com/contest/interview-archive/#task/pokemon-evolution/
 *
 * Created by dianaluca on 11/12/16.
 */

public class PokemonEvolution {
  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();   //nr of pokemons
    int M = sc.nextInt();   //nr of candies
    int X = sc.nextInt();   //buy price
    int Y = sc.nextInt();   //sell price

    //evolve pokemons
    long max_upgrade = ((long)N * Y + M) / (X + Y);
    if (max_upgrade > N)
      System.out.println(N);
    else
      System.out.println(max_upgrade);

  }
}
