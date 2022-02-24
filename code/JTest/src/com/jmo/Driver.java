package com.jmo;

import java.util.Arrays;
import java.util.Collection;
import java.util.EnumSet;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

import com.jmo.Adder;

public class Driver {

  public static void main(String[] args) {
    Driver driver = new Driver();
    //driver.testSetPut();
    //driver.testIters();
    driver.testBin();
  }

  private void testBin() {
    Bin bin = new Bin();
    bin.test();
  }


  /*
      // Check validity of scope
      if (scopeList.size() > 3) // max of three scope settings allowed
        throw new IllegalArgumentException("Too many scope arguments supplied");   
   */
  private void testIters() {
    String options = "profile1";
    String[] parts = options.split(":", 2);
    System.out.println("parts.size(): " + parts.length());
    
    
    List<String> scopeList = Arrays.asList(parts[1].split(","));
    System.out.println("scopeList.size(): " + scopeList.size());
    for (String s : scopeList) {
      System.out.println(">>>" + s + "<<<");
    }
    if (scopeList.size() > 3) // max of three scope settings allowed
      throw new IllegalArgumentException("Too many scope arguments supplied"); 

    //EnumSet<IteratorUtil.IteratorScope> validScopes = EnumSet.allOf(IteratorUtil.IteratorScope.class);
    //System.out.println("valid: " + validScopes.toString());
    for (String scope : scopeList) {
      IteratorUtil.IteratorScope.valueOf(scope.toLowerCase());
//      if (!valid.contains(IteratorUtil.IteratorScope.valueOf(scope.toLowerCase()))) {
//        throw new IllegalArgumentException(("Invalid scope supplied"));
//      }
    }

    //At this point, only valid iterator scope arguments have been passed through
    EnumSet<IteratorUtil.IteratorScope> scopes = EnumSet.noneOf(IteratorUtil.IteratorScope.class);
    if (scopeList.contains("scan"))
      scopes.add(IteratorUtil.IteratorScope.scan);
    if (scopeList.contains("minc"))
      scopes.add(IteratorUtil.IteratorScope.minc);
    if (scopeList.contains("majc"))
      scopes.add(IteratorUtil.IteratorScope.majc);
    if (scopes.isEmpty())
      throw new IllegalArgumentException("You must supply at least one scope to configure an iterator.");

  }

  private Collection<String> setValidScopes() {
    Collection<String> scopes = new HashSet<>();
    scopes.add("all");
    scopes.add("scan");
    scopes.add("minc");
    scopes.add("majc");
    return scopes;
  }

  private Collection<IteratorUtil.IteratorScope> setValScopes() {
    Collection<IteratorUtil.IteratorScope> scopes = new HashSet<>();
    scopes.add(IteratorUtil.IteratorScope.majc);
    scopes.add(IteratorUtil.IteratorScope.minc);
    scopes.add(IteratorUtil.IteratorScope.scan);
    return scopes;
  }

  public void testSetPut() {
    Map<String,String> map = new HashMap<>();
    String put;
    put = map.put("s1", "v1");
    System.out.println(put);
    put = map.put("s2", "v2");
    System.out.println(put);
    put = map.put("s3", "v3");
    System.out.println(put);
    put = map.put("s1", "v6");
    System.out.println(put);
    
    printMap(map);
  }


  private void printMap(Map<String,String> map) {
    for (String s : map.keySet()) {
      System.out.println("- " + s);
    }
  }
  
  public void testObjectPassing() {
    Adder adder1 = new Adder();
    System.out.println(adder1.getSum());
    adder1 = addTo1(4);
    System.out.println(adder1.getSum());
    adder1 = addTo1(5);
    System.out.println(adder1.getSum());
    adder1 = addTo1(1);
    System.out.println(adder1.getSum());

    System.out.println("-===");

    Adder adder2 = new Adder();
    System.out.println(adder2.getSum());
    adder2 = addTo2(4, adder2);
    System.out.println(adder2.getSum());
    adder2 = addTo2(5, adder2);
    System.out.println(adder2.getSum());
    adder2 = addTo2(1, adder2);
    System.out.println(adder2.getSum());
  }

  public Adder addTo1(int x) {
    Adder adder = new Adder();
    adder.incrBy(x);
    return adder;
  }

  public Adder addTo2(int x, Adder adder) {
    adder.incrBy(x);
    return adder;
  }
}
