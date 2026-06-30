class Solution {
    public String reverseWords(String s) {
        s=s.trim();
        StringBuilder ans = new StringBuilder("");
        StringBuilder sbt = new StringBuilder("");
        int i=s.length()-1;
        while(i>=0){
            while(i>=0 && s.charAt(i)!=' '){
                sbt.append(s.charAt(i));
                i--;
            }
            // now next index value is space
            while(i>=0 && s.charAt(i)==' ') i--;
            if(ans.length()==0){
                // ans is emply
                ans.append(sbt.reverse());
            }else{
                // before adding any word to ans we first add the space
                ans.append(' ');
                ans.append(sbt.reverse());
            }
            sbt = new StringBuilder("");
        }
        return ans.toString();

    }
}