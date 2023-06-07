class StringCompression:
  def __init__(self) -> None:
    pass


  def compress(self, chars: list[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1
    chars = chars[:ans]
    return ans


  def deCompress(self, chars: list[str]) -> list[str]:
    asciiNumRange = list(range(48, 58))
    asciiCharRange = list(range(97, 123))

    chars = chars[::-1]
    listObj = []
    i = 0

    while i < len(chars):
      currentLetter = chars[i]
      if ord(currentLetter) in asciiCharRange:
        listObj.append(chars[i])
        i += 1
      elif ord(currentLetter) in asciiNumRange:
        numStr = ""
        while i < len(chars) and ord(chars[i]) in asciiNumRange:
          numStr += chars[i]
          i += 1
        listObj.append(int(numStr[::-1]) * chars[i])
        i += 1
      
    return list("".join(listObj[::-1]))


solution = StringCompression()

compress_chars_1 = ["a","a","b","b","c","c","c"]
compress_chars_2 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
compress_chars_3 = ['a', 'b', '1', '2', 'e', 'k', '3', 't', '6']
compress_chars_4 = ['a', 'b']

print("the compressed string value is", solution.compress(compress_chars_1)) # expected answer => 6.....string value => "a2b2c3"....array value => ['a', '2', 'b', '2', 'c', '3']
print("the compressed string value is", solution.compress(compress_chars_2)) # expected answer => 4.....string value => "ab12"....array value => ['a', '2', 'b', '1', '2', 'c', '3']
print("the compressed string value is", solution.compress(compress_chars_3)) # expected answer => 9.....string value => "ab12ek3t6"....array value => ['a', 'b', '1', '2', 'e', 'k', '3', 't', '6']
print("the compressed string value is", solution.compress(compress_chars_4)) # expected answer => 2.....string value => "ab"....array value => ['a', 'b']



decompress_chars_1 = "a3b4a2c"
decompress_chars_2 = "e3k8"
decompress_chars_3 = "ab12ek3t6"
decompress_chars_4 = "ab"
decompress_chars_5 = "c003"

print("the decompressed string value is", solution.edwardo(decompress_chars_1)) # expected answer => ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'a', 'c']
print("the decompressed string value is", solution.edwardo(decompress_chars_2)) # expected answer => ['e', 'e', 'e', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k']
print("the decompressed string value is", solution.edwardo(decompress_chars_3)) # expected answer => ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'e', 'k', 'k', 'k', 't', 't', 't', 't', 't', 't']
print("the decompressed string value is", solution.edwardo(decompress_chars_4)) # expected answer => ['a', 'b']
print("the decompressed string value is", solution.edwardo(decompress_chars_5)) # expected answer => ['c', 'c', 'c']