    /**  
    �ҳ������ַ���������������Ӵ��ĳ��� 
    ** author :liuzhiwei   
    ** data   :2011-08-16 
    **/   
    #include "stdio.h"  
    #include "string.h"  
    #include "stdlib.h"  
      
    int longest_common_substring(char *str1, char *str2)  
    {  
        int i,j,k,len1,len2,max,x,y;  
        len1 = strlen(str1);  
        len2 = strlen(str2);  
        int **c = new int*[len1+1];  
        for(i = 0; i < len1+1; i++)  
            c[i] = new int[len2+1];  
        for(i = 0; i < len1+1; i++)  
            c[i][0]=0;        //��0�ж���ʼ��Ϊ0  
        for(j = 0; j < len2+1; j++)  
            c[0][j]=0;        //��0�ж���ʼ��Ϊ0   
        max = -1;  
        for(i = 1 ; i < len1+1 ; i++)  
        {  
            for(j = 1; j < len2+1; j++)  
            {  
                if(str1[i-1]==str2[j-1])     //ֻ��Ҫ�����Ϸ���c[i-1][j-1]�ȽϾͿ�����  
                    c[i][j]=c[i-1][j-1]+1;  
                else                         //��������ʱ��Ҫ����ߵ�c[i][j-1]���ϱߵ�c[i-1][j]ֵ�Ƚϣ����ﲻ��Ҫ  
                    c[i][j]=0;  
                if(c[i][j]>max)  
                {  
                    max=c[i][j];  
                    x=i;  
                    y=j;  
                }  
            }  
        }  
      
        //��������Ӵ�  
        char s[1000];  
        k=max;  
        i=x-1,j=y-1;  
        s[k--]='\0';  
        while(i>=0 && j>=0)  
        {  
            if(str1[i]==str2[j])  
            {  
                s[k--]=str1[i];  
                i--;  
                j--;  
            }  
            else       //ֻҪ��һ������ȣ���˵����ȵĹ����ַ����ˣ���������  
                break;  
        }  
        printf("������Ӵ�Ϊ��");  
        puts(s);  
        for(i = 0; i < len1+1; i++)         //�ͷŶ�̬����Ķ�ά����  
            delete[] c[i];  
        delete[] c;  
        return max;  
    }  
    int main(void)  
    {  
        char str1[1000],str2[1000];  
        printf("�������һ���ַ�����");  
        gets(str1);  
        printf("������ڶ����ַ�����");  
        gets(str2);  
        int len = longest_common_substring(str1, str2);  
        printf("����������Ӵ��ĳ���Ϊ��%d\n",len);  
        system("pause");  
        return 0;  
    }  
