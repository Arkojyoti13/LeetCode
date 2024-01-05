class Solution:
    def check(self,a,b):
        if a>=0 and a<self.n and b>=0 and b<self.m and self.grid[a][b]==0:
            return True
        return False
    def check2(self,a,b):
        if a>=0 and a<self.n and b>=0 and b<self.m and self.grid[a][b]==0 and self.vis[a][b]==0:
            return True
        return False
    def isReachable(self):
        if self.grid[0][0]!=0 or self.grid[self.n-1][self.m-1]!=0:
            return False
        self.stF.appendleft((0,0,-1))
        x=[0,1,-1,0]
        y=[1,0,0,-1]
        tot=1
        while len(self.stF) and tot!=0:
            a,b,depth=self.stF.popleft()
            if depth<0:
                tot-=1
                if a==self.n-1 and b==self.m-1:
                    return True
                if self.vis[a][b] or self.grid[a][b]==1:
                    continue
                self.vis[a][b]=1
                
                for dx,dy in zip(x,y):
                    if self.check2(a+dx,b+dy):
                        self.stF.append((a+dx,b+dy,-1))
                        tot+=1
            else:
                for dx,dy in zip(x,y):
                    if self.check(a+dx,b+dy):
                        self.grid[a+dx][b+dy]=1
                        self.stF.append((a+dx,b+dy,depth+1))
        return False
    def spread(self,count):
        x=[0,1,-1,0]
        y=[1,0,0,-1]
        while len(self.stF):
            a,b,depth=self.stF.popleft()
            self.grid[a][b]=1
            if self.grid[0][0]!=0 or self.grid[self.n-1][self.m-1]!=0:
                return
            if count==depth:
                self.stF.append((a,b,depth))
                return
            for dx,dy in zip(x,y):
                if self.check(a+dx,b+dy):
                    self.stF.append((a+dx,b+dy,depth+1))
        return


        
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        
        self.n=len(grid)
        self.m=len(grid[0])
        stFire=deque()
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]==1:
                    stFire.append((i,j,0))

        lo=0
        hi=((self.n*self.m)//2+5)
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            self.grid=[grid[i][::] for i in range(len(grid))]
            self.vis=[[0 for i in range(self.m)] for j in range(self.n)]
            self.stF=stFire.copy()
            self.spread(mid)
            if self.isReachable():
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        if ans==((self.n*self.m)//2+5):
            return 10**9
        return ans