//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class comp implements Comparator<ArrayList<String>> {
    // override the compare() method
    public int compare(ArrayList<String> a, ArrayList<String> b) {
        String x = "";
        String y = "";
        for (int i = 0; i < a.size(); i++) x += a.get(i);
        for (int i = 0; i < b.size(); i++) y += b.get(i);
        return x.compareTo(y);
    }
}

public class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            String[] wordList = new String[n];
            for (int i = 0; i < n; i++) {
                wordList[i] = br.readLine().trim();
            }
            String startWord, targetWord;
            startWord = br.readLine().trim();
            targetWord = br.readLine().trim();
            Solution obj = new Solution();
            ArrayList<ArrayList<String>> ans =
                obj.findSequences(startWord, targetWord, wordList);
            if (ans.size() == 0)
                System.out.println(-1);
            else {
                Collections.sort(ans, new comp());
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < ans.size(); i++) {
                    for (int j = 0; j < ans.get(i).size(); j++) {
                        sb.append(ans.get(i).get(j) + " ");
                    }
                    if (i != ans.size() - 1) sb.append("\n");
                }
                System.out.println(sb);
            }
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    static public ArrayList<ArrayList<String>> ladder(String beginWord, String endWord, List<String> wordList) {
        ArrayList<ArrayList<String>> ans = new ArrayList<>();
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return ans;
        Queue<List<String>> que = new LinkedList<>();
        List<String> path = new ArrayList<>();
        path.add(beginWord);
        que.offer(path);
        wordSet.remove(beginWord);
        Integer minLen = Integer.MAX_VALUE;
        while (!que.isEmpty()) {
            int size = que.size();
            Set<String> levelVisited = new HashSet<>();
            for (int s = 0; s < size; s++) {
                List<String> wordPath = que.poll();
                String lastWord = wordPath.get(wordPath.size() - 1);
                if (lastWord.equals(endWord)) {
                    if (wordPath.size() <= minLen) {
                        minLen = wordPath.size();
                        ans.add(new ArrayList<>(wordPath));
                    }
                    else return ans;
                } 
                else {
                    int len = lastWord.length();
                    for (int i = 0; i < len; i++) {
                        for (char c = 'a'; c <= 'z'; c++) {
                            char newStr[] = lastWord.toCharArray();
                            newStr[i] = c;
                            String newWord = new String(newStr);
                            if (wordSet.contains(newWord)) {
                                wordPath.add(newWord);
                                que.add(new ArrayList<>(wordPath));
                                levelVisited.add(newWord);
                                wordPath.remove(wordPath.size()-1);
                            }
                        }
                    }
                }
            }
            for (String it: levelVisited) wordSet.remove(it);
        }
        return ans;
    }
    
    public ArrayList<ArrayList<String>> findSequences(String startWord,
                                                      String targetWord,
                                                      String[] wordList) {
        // Code here
        List<String> wL = new ArrayList<>();
        for (int i = 0; i < wordList.length; i++)
            wL.add(wordList[i]);
        return ladder(startWord, targetWord, wL);
    }
}