package com.jmo;

import com.jmo.Binary.BinTest;
import org.apache.hadoop.io.Text;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.SortedSet;

public class JDriver {

  public JDriver() {}

  public static void main(String[] args) throws IOException {
    System.out.println("Test");
    JDriver driver = new JDriver();
    driver.testBinary();
  }

  private void testBinary() throws IOException {
    BinTest bin = new BinTest();
    //SortedSet<Text> binarySplits = bin.createBinarySplits(3, 4);
    //SortedSet<Text> binarySplits = bin.createTestSplits();
    SortedSet<Text> binarySplits = bin.readEncodedSplitsFromFile("/home/mark/data/bsplits2");
    bin.printSplits(binarySplits);
    //bin.writeSplitsToFile(Paths.get("/tmp/binary"), binarySplits);
    //bin.compare(binarySplits);
  }

}
