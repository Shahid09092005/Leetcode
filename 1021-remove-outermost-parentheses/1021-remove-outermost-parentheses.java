class Solution {
    public String removeOuterParentheses(String s) {
        int open=0;
        StringBuilder sb= new StringBuilder("");
        for(char ch:s.toCharArray()){
            if(ch=='('){
                open++;
                if(open>1) sb.append('(');
            }else{
                if(open>1){
                    sb.append(')');
                }
                open--;
            }
        }
        return sb.toString();
    }
}