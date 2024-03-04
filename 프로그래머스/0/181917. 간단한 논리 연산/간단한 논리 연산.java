class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = false;
        boolean first = false;
        boolean second = false;
        if(x1||x2) first = true;
        if(x3||x4) second = true;
        if(first&&second) answer = true;
        return answer;
    }
}