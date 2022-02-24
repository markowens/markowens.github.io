package com.jmo;

public class Adder {
  int a;

  public Adder() {
    a = 0;
  }
  
  public Adder(int i) {
      a = i;
  }
  
  public Adder incrBy(int i) {
      a = a + i;
      return this;
  }
  
  public int getSum() {
      return a;
  }
}

