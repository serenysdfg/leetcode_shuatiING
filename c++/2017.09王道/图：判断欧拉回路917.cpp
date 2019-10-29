    #include <cstdio>  
    #include <cstdlib>  
    #include <cstring>  
      
    const int maxx = 1005;  
      
    int pre[maxx],cnt,du[maxx];  
      
    void init(int n){  
        int i;  
        memset(du,0,sizeof(du));  
        for(i=1;i<=n;++i){  
            pre[i] = i;  
        }  
    }  
      
    int root(int x){  
        if(x!=pre[x]){  
            pre[x] = root(pre[x]);  
        }  
        return pre[x];  
    }  
      
    void merge(int x,int y){  
        int fa = root(x);  
        int fb = root(y);  
        if(fa!=fb){  
            --cnt;  
            pre[fa] = fb;  
        }  
    }  
      
    int main(){  
        int n,m,x,y,i;  
      
        while(scanf("%d",&n) && n){  
            init(n);  
            cnt = n-1;  
            scanf("%d",&m);  
            for(i=0;i<m;++i){  
                scanf("%d %d",&x,&y);  
                ++du[x];  
                ++du[y];  
                merge(x,y);  
            }  
      
            if(cnt!=0){  
                printf("0\n");  
                continue;  
            }  
      
            bool flg = true;  
      
            for(i=0;i<n;++i){  
                if(du[i]%2!=0){  
                    flg = false;  
                    break;  
                }  
            }  
      
            if(flg){  
                printf("1\n");  
            }else{  
                printf("0\n");  
            }  
        }  
        return 0;  
    }  
