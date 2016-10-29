package LeetCodeAlgorithms.related;

/**
 * Created by dianaluca on 10/28/16.
 */
public class PassByValuePassByReference {
  public static class Dog {
    private String name;

    public Dog(String name) {
      this.name = name;
    }

    public String getName() {
      return name;
    }
  }

  public static void foo(Dog d) {
    //d.getName().equals("Max"); // true

    d = new Dog("Fifi");

    //d.getName().equals("Fifi"); // true
  }

  /**
   * Litmus test:
   * There's a simple "litmus test" for whether a language supports pass-by-reference semantics:
   * A traditional swap method or function takes two arguments and
   * swaps them such that variables passed into the function are changed outside the function
   *
   * Results: In Java, Object references are passed by value, and primitives are passed by value.
   */
  public static void swap(Dog A, Dog B) {
    Dog tmp = A;
    A.name = B.name;
    B.name = tmp.name;
  }


  public static void main( String[] args ){
//    Dog aDog = new Dog("Max");
//    foo(aDog);
//    //aDog = new Dog("Fifi");
//
//    if (aDog.getName().equals("Max")) { //true
//      System.out.println( "Java passes by value." );
//
//    } else if (aDog.getName().equals("Fifi")) {
//      System.out.println( "Java passes by reference." );
//    }

    // Litmus Test
    Dog A = new Dog("A");
    Dog B = new Dog("B");
    System.out.println("Dog's A name is: " + A.getName());
    System.out.println("Dog's B name is: " + B.getName());
    //Java is not pass-by-reference
    swap(A, B);
    System.out.println("After swap(A, B)");
    System.out.println("Dog's A name is: " + A.getName());
    System.out.println("Dog's B name is: " + B.getName());

  }
}
