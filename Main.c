#include<reg51.h>
#include<intrins.h>
sbit HB_Check=P2^0; 

void Delay20ms()		//@11.0592MHz
{
	unsigned char i, j, k;

	_nop_();
	_nop_();
	i = 1;
	j = 216;
	k = 35;
	do
	{
		do
		{
			while (--k);
		} while (--j);
	} while (--i);
}



void UART_Init()
{
TMOD = 0x20;
SCON = 0x40;
TH1 = 0xFD;
TL1 = TH1;
PCON = 0x00;
EA = 1;
ES = 1;
TR1 = 1;
HB_Check=1;
}

void UART_SendByte(unsigned char Data){
SBUF=Data;
while(TI==0);
TI=0;
}


void main(){
	UART_Init();
	while(1){
	if(HB_Check == 0){
Delay20ms();
		if(HB_Check == 1){

		UART_SendByte(0x7e);
			}
		}
	};
}
 
