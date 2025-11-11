# Last updated: 11/10/2025, 8:00:36 PM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        '''
        on alice's turn, she removes any substring with odd number vowels
        on bob's turn, he removes any non-empty substring with even number vowels


        ex. "leetcode"
             aaaaaaa
             "e" is left, so bob loses

        "eee" -> even vowels -> alice wins
        "eeee" -> bob has no move after alice takes 3
        "eeetet"
         aaaa
             bb
        
        strategy for alice: (even vowel count):
            alice takes longest odd vowel substring 
        

        initial approach:
            if odd vowels, alice wins
            if even, find number of consonants before first vowel and after last vowel
            if min of these two is <= 1, alice wins, else bob wins
        
        final approach:
            if 0 vowels, bob wins
            if odd vowels, alice wins
            if even, find number of consonants before first vowel and after last vowel
            if min of these two is <= 1, alice wins, else bob wins
        
        '''
        return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s