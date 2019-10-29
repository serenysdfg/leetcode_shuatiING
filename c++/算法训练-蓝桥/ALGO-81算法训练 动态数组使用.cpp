    #include<iostream>  
    using namespace std;  
    int main()  
    {  
        int n,i,sum,ave;  
        cin>>n;  
        int *s=new int[n];  
        sum=0;  
        for(i=0;i<n;i++)  
        {  
            cin>>s[i];  
            sum=sum+s[i];  
        }  
        ave=sum/(n+1);  
        cout<<sum<<' '<<ave<<endl;  
        return 0;  
    }  
