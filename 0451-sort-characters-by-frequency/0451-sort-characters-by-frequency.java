class Solution {
    public String frequencySort(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        StringBuilder sb = new StringBuilder("");
        for(char ch:s.toCharArray()){
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        for(int i=0;i<map.size();i++){
            int max=0;
            char k=' ';
            int val=0;
            for(char c:map.keySet()){
                if(max<map.get(c)){
                    max=map.get(c);
                    val=max;
                    k= c;
                }
            } // inner loop ends
            // add into sb
            for(int tm =0;tm<val;tm++){
                sb.append(k);
            }
            // now the key(k) with value '0' in HashMap so other character can come
            map.put(k,0);
        }
        return sb.toString();
    }
}