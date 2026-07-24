class Solution {
    public static boolean isPalindrome(int i,int j,String s){
        while(i<j){
            if(s.charAt(i)!=s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
    public String longestPalindrome(String s) {
        if(s.length()==0) return "";
        int st=0;// starting point of the substring that is palindrome
        int len=0;
        for(int i=0;i<s.length();i++){
            for(int j=i;j<s.length();j++){
                if(isPalindrome(i,j,s)){
                    // palindrome is true but check it's length is greater than previous
                    int curlen=j-i+1;
                    if(len<curlen){
                        st=i;
                        len=curlen; 
                    }
                } // if end here 
            } // inner loop ends
        }// second loop ends
        return s.substring(st,st+len);
    }
}