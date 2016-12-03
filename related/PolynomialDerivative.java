package Algorithms.related;

import java.lang.reflect.Array;
import java.util.*;

/**
 * Created by dianaluca on 12/2/16.
 */
public class PolynomialDerivative {

  public static class Term implements Comparable<Term>{
    private int coef;
    private int exponent;

    public Term(int coef, int exponent) {
      this.coef = coef;
      this.exponent = exponent;
    }

    public int getCoef() {
      return coef;
    }

    public int getExponent() {
      return exponent;
    }

    public int evaluate(int x) {
      int res = 1;

      for (int power = 0; power < exponent; ++power)
        res *= x;

      return coef * res;
    }

    public Term multiply(Term other) {
      return new Term(coef * other.coef, exponent + other.exponent);
    }

    public Term getDerivate() {
      if (exponent == 0)
        return new Term (0, 0);
      return new Term(coef * exponent, exponent - 1);
    }

    public int compareTo(Term other) {
      int otherExponent = other.exponent;

      // descending order
      return otherExponent - exponent;

      // ascending order
      // return exponent - otherExponent;
    }

    public String toString() {
      StringBuilder sb = new StringBuilder();
      if (coef == 0) return "";
      sb.append(coef);
      if (exponent == 1)
        sb.append("x");
      else if (exponent != 0)
        sb.append("x^").append(exponent);
      return sb.toString();

    }

    public static Comparator<Term> CoefComparator
        = new Comparator<Term>() {

      public int compare(Term term1, Term term2) {
        return term1.getCoef() - term2.getCoef();
      }
    };

    public static Comparator<Term> ExponentComparator
        = new Comparator<Term>() {

      public int compare(Term term1, Term term2) {
        return term2.getExponent() - term1.getExponent();
      }
    };
  }

  public static class Polynom {
    public ArrayList<Term> polynom = new ArrayList<>(); // Polynom is an ArrayList<Term>

    void readFromStdio () {
      Scanner sc = new Scanner(System.in);
      int N = sc.nextInt();

      for (int i = 0; i < N; i++) {
        int coef = sc.nextInt();
        int exponent = sc.nextInt();
        Term term = new Term(coef, exponent);
        polynom.add(term);
      }

      normalize();
    }

    public int evaluate(int x) {
      int sum = 0;

      for (Term term : polynom) {
        sum += term.evaluate(x);
      }

      return sum;
    }

    public void normalize() {
      Collections.sort(polynom, Term.ExponentComparator);
      ArrayList<Term> compactPolynom = new ArrayList<>();

      int i = 0;
      while(i < polynom.size()) {
        int sumCoef = polynom.get(i).coef;
        int j = i + 1;
        while (j < polynom.size() && polynom.get(i).exponent == polynom.get(j).exponent) {
          sumCoef += polynom.get(j).coef;
          j++;
        }

        compactPolynom.add(new Term(sumCoef, polynom.get(i).exponent));
        i = j;
      }

      polynom = compactPolynom;
    }

    public Polynom multiply(Polynom otherPolynom) {
      Polynom newPolynom = new Polynom();

      for (Term term : polynom) {
        for (Term otherTerm : otherPolynom.polynom) {
          newPolynom.polynom.add(term.multiply(otherTerm));
        }
      }

      newPolynom.normalize();

      return newPolynom;
    }

    public String toString() {
      //TODO: sort polynom
      Collections.sort(polynom, Term.ExponentComparator);

      StringBuilder sb = new StringBuilder();

      for (int i = 0; i < polynom.size(); i++) {
        Term term = polynom.get(i);
        if (i < polynom.size() - 1)
          sb.append(" + ");
      }
      String result = sb.toString();
      if (result.equals(""))
        return "<empty>";
      return result;
    }

    Polynom getDerivative() {
      Polynom newPolynom = new Polynom();
      // this.polynom
      for (Term term : polynom) {
        newPolynom.polynom.add(term.getDerivate());
      }
      return newPolynom;
    }
  }

  /**
   *  3
      4 3
      3 2
      2 1
   * @param args
   */

  public static void main(String[] args) {
    Polynom polynom = new Polynom();
    int x = 2;

    polynom.readFromStdio();

    System.out.println("Polynomial function is:\n" + polynom.toString());
    System.out.printf("Evaluate polynomial function in %d. p(%d) = %d\n",x,x,polynom.evaluate(x));

    System.out.println("Polynomial derivative is:\n" + polynom.getDerivative().toString());
    System.out.printf("Evaluate polynomial function in %d after derivative. p'(%d) = %d\n",x,x,polynom.getDerivative().evaluate(x));


  }
}
