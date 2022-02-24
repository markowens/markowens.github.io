package com.jmo.Binary;

import com.jmo.Utils.ByteBufferUtil;
import com.jmo.Utils.TextUtils;
import org.apache.hadoop.io.Text;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Base64;
import java.util.Iterator;
import java.util.Random;
import java.util.SortedSet;
import java.util.TreeSet;

public class BinTest {

  public SortedSet<Text> createBinarySplits(int num, int len) {
    SortedSet<Text> splits = new TreeSet<>();
    Random rand = new Random();

    for(int i = 0 ; i < num; i++) {
      byte[] split = new byte[len];
      rand.nextBytes(split);
      splits.add(new Text(split));
    }
    return splits;
  }

  public SortedSet<Text> createTestSplits() {
    SortedSet<Text> splits = new TreeSet<>();
    byte[][] data = {
        {(byte)0xc1, (byte)0xaf, (byte)0xc2, (byte)0x96, (byte)0x99, (byte)0x63, (byte)0x30,
            (byte)0x6c},
        {(byte)0xaa, (byte)0x0d, (byte)0x2e, (byte)0x2f, (byte)0x1b, (byte)0xcd, (byte)0x30,
            (byte)0xe8},
        {(byte)0x1b, (byte)0x3d, (byte)0x38, (byte)0x39, (byte)0x55, (byte)0xf6, (byte)0x8e,
            (byte)0x69},
        {(byte)0x6d, (byte)0x09, (byte)0xce, (byte)0x30, (byte)0x61, (byte)0x5c, (byte)0x35,
            (byte)0x3a},
        {(byte)0xbe, (byte)0x35, (byte)0x11, (byte)0x13, (byte)0xdf, (byte)0xa5, (byte)0xdf,
            (byte)0x8c},
        {(byte)0xe8, (byte)0x29, (byte)0x4e, (byte)0x78, (byte)0x22, (byte)0x51, (byte)0x9c,
            (byte)0xa6}
    };
    for (byte[] b : data) {
      splits.add(new Text(Base64.getEncoder().encodeToString(b)));
    }
    return splits;
  }

  public void printSplits(SortedSet<Text> splits) {
    for (Text split : splits) {
      byte[] bytes1 = TextUtils.getBytes(split);
      System.out.println(">>>> " + getBytesAsString(bytes1, bytes1.length));
      //ByteBuffer buffer = TextUtils.getByteBuffer(split);
      //byte[] bytes2 = ByteBufferUtil.toBytes(buffer);
      //System.out.println(">>>>      : " + getBytesAsString(bytes2, bytes1.length));
      //System.out.println(">>>>      : " + ByteBufferUtil.toText(buffer));
    }
  }

  private void printBytes(byte[] bytes) {
    System.out.println("-----------");
    System.out.println("--> " + new String(bytes));
    System.out.println("--> " + Arrays.toString(bytes));
    String s = Arrays.toString(bytes);
    System.out.println("--> " + getBytesAsString(bytes, bytes.length));
    String bytesAsString = getBytesAsString(s.getBytes(), s.length());
    System.out.println("--> " + bytesAsString);
    System.out.println("-----------");
  }

  private String getBytesAsString(byte[] split, int size) {
    StringBuilder sb = new StringBuilder();
    for (int ii = 0; ii < size; ii++) {
      String str = String.format("%02x", split[ii]);
      sb.append(str);
    }
    return sb.toString();
  }

  public void writeSplitsToFile(Path path, SortedSet<Text> data) throws IOException {
    if (Files.exists(path)) {
      Files.delete(path);
    }
    try (DataOutputStream stream = new DataOutputStream(new FileOutputStream(path.toFile()))) {
      for (Text text : data) {
        byte[] bytes = TextUtils.getBytes(text);
        String encode = Base64.getEncoder().encodeToString(bytes);
        stream.writeBytes(encode + '\n');
      }
    }
  }

  public SortedSet<Text> readEncodedSplitsFromFile(String  path) throws IOException {
    SortedSet<Text> data = new TreeSet<>();
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
      String line;
      while ((line = br.readLine()) != null) {
        //line = line.trim();
        System.out.println("line: " + line);
        byte[] decoded = Base64.getDecoder().decode(line);
        System.out.println("decoded: " + getBytesAsString(decoded, decoded.length));
        data.add(new Text(decoded));
      }
    }
    return data;
  }


  public void tvs(String str) {

    byte[] bytes1 = "0000".getBytes();
    printBytes(bytes1);

    System.out.println("String: "  + str);
    Text t = new Text(str);
    printBytes(str.getBytes());
    System.out.println("\t" + getBytesAsString(str.getBytes(StandardCharsets.UTF_8), str.length()));
    System.out.println("Text:   " + t);
    System.out.println("\t" + getBytesAsString(t.getBytes(), t.getLength()));
    printBytes(t.getBytes());

    ByteBuffer bf = ByteBuffer.wrap(t.getBytes(),0,t.getLength());

    byte[] bytes = ByteBufferUtil.toBytes(bf);
    System.out.println("bytes: " + bytes);
    System.out.println("       " + new String(bytes));
    Text text = ByteBufferUtil.toText(bf);
    System.out.println("text: " + text);
    String s = ByteBufferUtil.toString(bf);
    System.out.println("s   : " + s);
  }

  public void compare(SortedSet<Text> splits) {
    Text current = new Text("");
    Iterator<Text> it = splits.iterator();
    while (it.hasNext()) {
      Text next = it.next();
      System.out.println("next: " + getBytesAsString(next.getBytes(), next.getLength()));
      if (current.toString().compareTo(next.toString()) >= 0) {
        System.out.println("ERROR: order wrong");
      }
    }
  }
}



//    byte[] s = new byte[4];
//    s[0] = 0x48;
//    s[1] = 0x45;
//    s[2] = 0x4c;
//    s[3] = 0x50;
//    splits.add(new Text(s));
//    s[3] = 0x51;
//    splits.add(new Text(s));
//    s[3] = (byte)0x8d;
//    splits.add(new Text(s));
//    return splits;

//    byte[] s = {0x41, 0x42, 0x43, 0x44};
//    splits.add(new Text(s));
//    s[3] = (byte)0x55;
//    s = new byte[]{0x45, 0x46, 0x47, 0x48};
//    splits.add(new Text(s));
//    s = new byte[]{(byte)0x81, (byte)0x82, (byte)0xA3, (byte)0xA4};
//    splits.add(new Text(s));
//    return splits;

