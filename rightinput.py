class info:
 """
 #######################################################
 ########## date: 1/07/2020 wednesday (july) ###########
 #######################################################
 .
 .
 .
 .
 why i build this(?):
 	achualy i was making program for each lesson in PHYSICS**
 	I was need to input prompt for int,string,float data type
        using Object Oriented Guidlines (oop)



clases:
	Int(massage,color);
	Float(massage,color);
	String(massage,color);
	
		
Function:	
	int_data();
	float_data();
	str_data();
	              
 """


class Int:
    def __init__(self,massage,color,):
        self.color=color;
        self.massage=massage;

    def int_data(self):
        while(True):
            
            totale_massage=self.color+self.massage;
            try:
                data=int(input(totale_massage));
                return data;
                break;
            except:
                print("\033[31m[!] please input integer value...  :)");
                continue;   

              
class Flaot:
    def __init__(self,massage,color):
        self.color=color;
        self.massage=massage;

    def float_data(self):
        while(True):
            totale_massage=self.color+self.massage;
            try:
                data=float(input(totale_massage));
                return data;
                break;
            except:
                print("\033[31m[!] please input float value...  :)");
                continue; 

                
class String:
    def __init__(self,massage,color):
        self.color=color;
        self.massage=massage;

    def str_data(self):
        while(True):
            totale_massage=self.color+self.massage;
            try:
                data=str(input(totale_massage));
                return data;
                break;
            except:
                print("\033[31m[!] please input string value...  :)");
                continue;       


if __name__=="__main__":
    print(info.__doc__)
 #   a=String("option ","\033[32m");
  #  print(type(a.str_data()))