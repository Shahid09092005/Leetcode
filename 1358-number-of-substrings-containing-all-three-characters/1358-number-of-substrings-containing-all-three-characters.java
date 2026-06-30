class Solution {
    public int numberOfSubstrings(String s) {
        int cnta=0;
        int cntb=0;
        int cntc=0;
        int ans=0;
        int i=0;
        int len = s.length();
        int st=0;
        while(i<len){
            char currChar = s.charAt(i);
            if(currChar=='a'){
                cnta++;
            }else if(currChar=='b'){
                cntb++;
            }else{
                cntc++;
            }
            while(cnta>0 && cntb>0 && cntc>0){
                int makeSubString=len-i;
                ans+=makeSubString;
                char chAtSt = s.charAt(st);
                if(chAtSt=='a'){
                    cnta--;
                }else if(chAtSt=='b'){
                    cntb--;
                }else{
                    cntc--;
                }
                st++;

            }

            i++;
        }
        return ans;
    }
}