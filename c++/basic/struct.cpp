    #include <stdio.h>  
    #include <string.h>  
    int main(int argc, const char * argv[]) {  
        //����һ���ṹ��  
        struct student {  
            int num;            //ѧ��  
            char name[10];      //����  
            int age;            //����  
            char sex[2];        //�Ա�  
            float score;        //����  
        }studD, studE, studF;   //�������ṹ���ͬʱ����������student���͵ı���  
        //����student���͵Ľṹ�����  
        struct student studA;   //ѧ��A  
        struct student studB;   //ѧ��B  
        struct student studC;   //ѧ��C  
        studA.num = 1;  
        strcpy(studA.name, "wangxinyu");  
        studA.age = 21;  
        strcpy(studA.sex, "men");  
        studA.score = 89.57;  
        printf("��ѧ�����:%d\n����:%s\n����:%d\n�Ա�:%s\n����:%.2f\n",  
               studA.num, studA.name, studA.age, studA.sex, studA.score);  
        return 0;  
    }  
    
    
 
