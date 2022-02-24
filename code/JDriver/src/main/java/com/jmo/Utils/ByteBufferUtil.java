package com.jmo.Utils;

import org.apache.hadoop.io.Text;

import java.io.ByteArrayInputStream;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static java.nio.charset.StandardCharsets.UTF_8;

public class ByteBufferUtil {
  public static byte[] toBytes(ByteBuffer buffer) {
    if (buffer == null)
      return null;
    if (buffer.hasArray()) {
      // did not use buffer.get() because it changes the position
      return Arrays.copyOfRange(buffer.array(), buffer.position() + buffer.arrayOffset(),
          buffer.limit() + buffer.arrayOffset());
    } else {
      byte[] data = new byte[buffer.remaining()];
      // duplicate inorder to avoid changing position
      buffer.duplicate().get(data);
      return data;
    }
  }

  public static List<ByteBuffer> toByteBuffers(Collection<byte[]> bytesList) {
    if (bytesList == null)
      return null;
    ArrayList<ByteBuffer> result = new ArrayList<>();
    for (byte[] bytes : bytesList) {
      result.add(ByteBuffer.wrap(bytes));
    }
    return result;
  }

  public static List<byte[]> toBytesList(Collection<ByteBuffer> bytesList) {
    if (bytesList == null)
      return null;
    ArrayList<byte[]> result = new ArrayList<>(bytesList.size());
    for (ByteBuffer bytes : bytesList) {
      result.add(toBytes(bytes));
    }
    return result;
  }

  public static Text toText(ByteBuffer byteBuffer) {
    if (byteBuffer == null)
      return null;

    if (byteBuffer.hasArray()) {
      Text result = new Text();
      result.set(byteBuffer.array(), byteBuffer.arrayOffset() + byteBuffer.position(),
          byteBuffer.remaining());
      return result;
    } else {
      return new Text(toBytes(byteBuffer));
    }
  }

  public static String toString(ByteBuffer bytes) {
    if (bytes.hasArray()) {
      return new String(bytes.array(), bytes.arrayOffset() + bytes.position(), bytes.remaining(),
          UTF_8);
    } else {
      return new String(toBytes(bytes), UTF_8);
    }
  }


  public static void write(DataOutput out, ByteBuffer buffer) throws IOException {
    if (buffer.hasArray()) {
      out.write(buffer.array(), buffer.arrayOffset() + buffer.position(), buffer.remaining());
    } else {
      out.write(toBytes(buffer));
    }
  }

  public static ByteArrayInputStream toByteArrayInputStream(ByteBuffer buffer) {
    if (buffer.hasArray()) {
      return new ByteArrayInputStream(buffer.array(), buffer.arrayOffset() + buffer.position(),
          buffer.remaining());
    } else {
      return new ByteArrayInputStream(toBytes(buffer));
    }
  }
}
