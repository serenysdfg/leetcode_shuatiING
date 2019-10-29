    #include <stdio.h>  
    #include <string.h>  
    int main(int argc, const char * argv[]) {  
        //定义一个结构体  
        struct student {  
            int num;            //学号  
            char name[10];      //姓名  
            int age;            //年龄  
            char sex[2];        //性别  
            float score;        //评分  
        }studD, studE, studF;   //在声明结构体的同时声明了三个student类型的变量  
        //定义student类型的结构体变量  
        struct student studA;   //学生A  
        struct student studB;   //学生B  
        struct student studC;   //学生C  
        studA.num = 1;  
        strcpy(studA.name, "wangxinyu");  
        studA.age = 21;  
        strcpy(studA.sex, "men");  
        studA.score = 89.57;  
        printf("该学生序号:%d\n姓名:%s\n年龄:%d\n性别:%s\n评分:%.2f\n",  
               studA.num, studA.name, studA.age, studA.sex, studA.score);  
        return 0;  
    }  
    
    
 
