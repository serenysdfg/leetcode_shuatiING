//猴子吃水果
    #include <stdio.h>  
    #include<iostream>  
    #include<algorithm>  
    #include<vector>  
    #include<string.h>  
    using namespace std;  
      
    struct monkey  
    {  
        char name [100];  
        int strong ;  
        int food;  
    };  
      
    bool cmp(monkey a ,monkey b)  
    {  
        if(a.strong==b.strong)  
            return strcmp(a.name,b.name)<0;  //字母小的先吃 
        else  
            return a.strong>b.strong;  
    }  
      
    int main()  
    {  
        int n , m ;  
        int i ,j ;  
        char name[100];  
        int strong , food;  
        int sum;  
        //priority_queue<monkey> q;  
        vector<monkey> v;  
    //FILE *fp = freopen("test.txt","r", stdin);  
        while(scanf("%d%d",&n,&m)!=EOF)  
        {  
            v.clear();  
            for(i = 0 ; i<n ; i++)  
            {  
                monkey m;  
                scanf("%s %d %d", name , &strong ,&food);  
                strcpy(m.name,name);  
                m.strong = strong;  
                m.food = food;  
                //q.push(m);  
                v.push_back(m);  
            }  
            sort(v.begin(),v.end(),cmp);  //排序 
            //priority_queue<monkey>::iterator it ;  
            for(i = 0 ; i<m ; i++)  
            {  
                scanf("%s", name);  
                sum=1;  
                for(j = 0 ; j<n ;j++)  
                {  
                    if(strcmp(v[j].name , name)==0)  
                    {  
                        printf("%d\n",sum);  
                        break;  
                    }  
                    else  
                    {  
                        sum+=v[j].food;  
                    }     
                }  
            /*  for(it = q.begin();it!=q.end();it++) 
                { 
                    monkey temp = *it; 
                    if(strcmp(temp.name , name)==0) 
                    { 
                        printf("%d\n",sum); 
                        break; 
                    } 
                    else 
                    { 
                        sum+=temp.food; 
                    } 
                }   */  
            }  
        }  
        return 0;  
    }   
