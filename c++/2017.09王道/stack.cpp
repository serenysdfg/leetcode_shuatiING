#include <stdio.h>
#include <string.h>
int main()
{
    char a[101],s[101];
    int i,len,mid,next,top;
                
    gets(a); //����һ���ַ���
    len=strlen(a); //���ַ����ĳ���
    mid=len/2-1; //���ַ������е�
                
    top=0;//ջ�ĳ�ʼ��
    //��midǰ���ַ�������ջ
    for(i=0;i<=mid;i++)
        s[++top]=a[i];
                
    //�ж��ַ����ĳ��ȵ�����������ż�������ҳ���Ҫ�����ַ�ƥ�����ʼ�±�
    if(len%2==0)
        next=mid+1;
    else
        next=mid+2;
                               
    //��ʼƥ��
    for(i=next;i<=len-1;i++)
    {
        if(a[i]!=s[top])
            break;
        top--;
    }
                
    //���top��ֵΪ0����˵��ջ�ڵ����е��ַ�����һһƥ����
    if(top==0)
        printf("YES");
    else
        printf("NO");
              
    getchar();getchar();
    return 0;
}
