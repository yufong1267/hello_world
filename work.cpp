#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <windows.h>
#include <unistd.h>
#include <conio.h>
// g++ -std=c++11
using namespace std ;
void *keyboard1(void *);
void *keyboard2(void *);
void *display(void *);
int getpoint(int [5][5]);
char keyid ;
int window[5][5]={{1,1,1,1,1},{1,1,1,1,1},{1,1,0,1,1},{1,1,1,1,1},{1,1,1,1,1}};
pthread_mutex_t mutex1=PTHREAD_MUTEX_INITIALIZER;
int main (){
	pthread_t key1,key2,disp;
	pthread_create(&key1,NULL,keyboard1,NULL);
	pthread_create(&key2,NULL,keyboard2,NULL);
	pthread_create(&disp,NULL,display,NULL);

	pthread_join(key1,NULL);
	pthread_join(key2,NULL);
	pthread_join(disp,NULL);
	return 0;	
}
int getpoint(int window[5][5]){
	int point =0;
	for(int i=0;i<5;++i){
		for(int j=0;j<5;++j){
			if(window[i][j]==0){
				point=i*5+j;
			}
		}
	}
	return point;
}
void *display(void *){
	while(1){
		for(int i=0;i<5;++i){
			for(int j=0;j<5;++j){
				printf("%d",window[i][j]);
			}
			printf("\n");
		}
		system("cls");
	}
	
}

void *keyboard1(void *unuse){
	//Up-Arrow 72
	//Dw-Arrow 80
	//Left-Arrow 75
	//Right-Arrow 77
	while(1){
		pthread_mutex_lock(&mutex1);
		keyid =getch();
		pthread_mutex_unlock(&mutex1);
		if(keyid==27)break;
		int point =getpoint(window);
		int x=point /5;
		int y=point %5;
		switch(keyid){
			case 72:
				if(x>0){
					window[x][y]=1;
					window[x-1][y]=0;
				}
				break;
			case 80:
				if(x<4){
					window[x][y]=1;
					window[x+1][y]=0;
				}
				break;
			case 75:
				if(y>0){
					window[x][y]=1;
					window[x][y-1]=0;
				}
				break;	
			case 77:
				if(y<4){
					window[x][y]=1;
					window[x][y+1]=0;
				}
				break;
		}
	}
	usleep(350000);
	pthread_exit(NULL);
	
}

void *keyboard2(void *unuse){
	
	while(1){
		pthread_mutex_lock(&mutex1);
		keyid =getch();
		pthread_mutex_unlock(&mutex1);
		if(keyid==27)break;
		int point =getpoint(window);
		int x=point /5;
		int y=point %5;
		switch(keyid){
			case 'W':
			case 'w':
				if(x>0){
					window[x][y]=1;
					window[x-1][y]=0;
				}
				break;
			case 'S':
			case 's':
				if(x<4){
					window[x][y]=1;
					window[x+1][y]=0;
				}
				break;
			case 'A':
			case 'a':
				if(y>0){
					window[x][y]=1;
					window[x][y-1]=0;
				}
				break;	
			case 'D':
			case 'd':
				if(y<4){
					window[x][y]=1;
					window[x][y+1]=0;
				}
				break;
		}
	}
	usleep(350000);
	pthread_exit(NULL);
	
}