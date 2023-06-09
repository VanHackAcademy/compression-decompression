# VanHack Learning Hub Code Challenge - May 2023

## Compression and Decompression Algorithm

## ***<span style="color:gray">*Question 1*</span>***
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

***You must write an algorithm that uses only constant extra space.***

Example 1:
<br/>
***Input***: chars = ["a","a","b","b","c","c","c"]
<br/>
***Output***: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
<br/>
***Explanation***: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
******


Example 2:
<br/> 
***Input*** chars = ["a"]
<br/>
***Output***: Return 1, and the first character of the input array should be: ["a"]
<br/>
***Explanation***: The only group is "a", which remains uncompressed since it's a single character.
******


Example 3:
<br/>
***Input***: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
<br/>
***Output***: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
<br/>
***Explanation***: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
******

Constraints:
<br/>
1 <= chars.length <= 2000
<br/>
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
<br/>
<br/>
Source [Leetcode 443 - String Compression](https://leetcode.com/problems/string-compression/).
******
******
<br/>

## ***<span style="color:gray">*Question 2*</span>***
Write a function/method to decompress the returned list value from **Question 1** to give you back the original list input.
<br/>

Example 1:
<br/>
***Input***: chars = "a3b4a2c"
<br/>
***Output***: ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'a', 'c']
<br/>
***Explanation***: The first letter "a" is repeated three (3) times, the second letter "b" is repeated four (4) times, the third letter "a" is repeated two (2) times and the last letter "c" is written just once.
******
<br/>

Example 2:
<br/>
***Input***: chars = "e3k8"
<br/>
***Output***: ['e', 'e', 'e', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k']
******
<br/>

Example 3:
<br/>
***Input***: chars = "ab12ek3t6"
<br/>
***Output***: ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'e', 'k', 'k', 'k', 't', 't', 't', 't', 't', 't']
******
<br/>

Example 4:
<br/>
***Input***: chars = "ab"
<br/>
***Output***: ['a', 'b']
******
<br/>

Example 5:
<br/>
***Input***: chars = "c003"
<br/>
***Output***: ['c', 'c', 'c']
******
<br/>

Constraints:
<br/>
1.  The first letter will always be a character.
<br/>
1.  The maximum number of any compressed character is 999
<br/>

******
******


### ***You may decide to take a different path in designing and implementing your solution. Happy coding.***

***VanHack Learning Hub***