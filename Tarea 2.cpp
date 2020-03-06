// thread example
#include <iostream>       // std::cout
#include <thread> 
#include <cmath>
#include <ctime>        // std::thread

int v [] = {}; 


void arraygenerator(int len) 
{
  int i=0;
  
  
    while (i < len)    
    {

          v [i] = {i};                       

          ++i; 
	}
	       
 
}

void potencia(int min,  int max)
{
  int i=0;
  
  int d []= {};
  
  for (int i = 0; i < 101; i++)
     {
         if (min<i<max)	{
		 
			 d [i] = {pow(v[i],2)};    
			 std::cout <<d [i]<<" ";
		}
     }
     
}

int main() 
{
  
  int len = 100;
  
  clock_t start1, end1, start2, end2;
  
  arraygenerator(len); 
  
  start1 = clock(); 
  std::thread t1 (potencia,0,len); 
  end2 = clock();
  double time_taken1 = double(end1 - start1) / double(CLOCKS_PER_SEC);
  
  std::cout <<'\n';
  
  start2 = clock();; 
  std::thread t21 (potencia,0,len/4);
  std::thread t22 (potencia,len/4,len/2);
  std::thread t23 (potencia,len/2,3*(len/4));
  std::thread t24 (potencia,(3*len/4),len);
  end2 = clock();
  double time_taken2 = double(end2 - start2) / double(CLOCKS_PER_SEC);

  std::cout <<'\n';
  
  std::cout <<'El unico hilo: '<< time_taken1<<'\n';
  std::cout <<'Hilo de 4: '<< time_taken2<<'\n';
  t1.join();               
  
  t21.join();
  t22.join();
  t23.join();
  t24.join();
  
  
  //t2.join();               // pauses until second finishes

 // std::cout << "foo and bar completed.\n";

  return 0;
}
