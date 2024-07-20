class Solution:
    def numberOfSubsequences (self,S,W):
        # code here 
        res=0
        n=len(S)
        visited=[False]*n
        for i in range(0,n):
            if(S[i]==W[0] and not visited[i]):
                j=i+1
                visited[i]=True
                k=1
                while(j<n and k<len(W)):
                    if(S[j]==W[k] and (not visited[j])):
                        visited[j]=True
                        k+=1
                    j+=1
                if(k==len(W)):
                     res+=1
                else:
                    break

        return res
if __name__ == '__main__': 
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))