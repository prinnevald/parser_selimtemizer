

package x.y.z ;  // Like Namespace in C++


import a      ;  // Like #include in C++
import b.c    ;
import d.*    ;
...


public class X
{

  public int    i ;
  public double d ;
  ...


  public static int add ( int a , int b )
  {
    int result = a + b ;

    return result ;
  }

  public static int subtract ( int a , int b )
  {
    ...
  }

  public static void main ( String [] args )
  {
    ...
  }

}

