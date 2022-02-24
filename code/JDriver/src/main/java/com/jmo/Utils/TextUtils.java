package com.jmo.Utils;

import org.apache.hadoop.io.Text;

import java.nio.ByteBuffer;

import static java.nio.charset.StandardCharsets.UTF_8;

public class TextUtils {
  public static byte[] getBytes(Text text) {
    byte[] bytes = text.getBytes();
    if (bytes.length != text.getLength()) {
      bytes = new byte[text.getLength()];
      System.arraycopy(text.getBytes(), 0, bytes, 0, bytes.length);
    }
    return bytes;
  }

  public static ByteBuffer getByteBuffer(Text text) {
    if (text == null)
      return null;
    byte[] bytes = text.getBytes();
    return ByteBuffer.wrap(bytes, 0, text.getLength());
  }

}
