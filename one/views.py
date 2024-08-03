from django.shortcuts import render
import pickle
import numpy as n
k=pickle.load(open("price.sav",'rb'))
# Create your views here.




def price(request):
    return render(request,"base.html")  


def pred(request):
    if request.method=="POST":
        Bp=int(request.POST['battery_power'])
        blue=int(request.POST['blue'])
        clock_speed=int(request.POST['clock_speed'])
        dual_sim=int(request.POST['dual_sim'])
        fc=int(request.POST['fc'])
        four_g=int(request.POST['four_g'])
        int_memory=int(request.POST['int_memory'])
        m_dep=int(request.POST['m_dep'])
        mobile_wt=int(request.POST['mobile_wt'])
        n_cores=int(request.POST['n_cores'])
        pc=int(request.POST['pc'])
        px_height=int(request.POST['px_height'])
        px_width=int(request.POST['px_width'])
        ram=int(request.POST['ram'])
        sc_h=int(request.POST['sc_h'])
        sc_w=int(request.POST['sc_w'])
        talk_time=int(request.POST['talk_time'])
        three_g=int(request.POST['three_g'])
        touch_screen=int(request.POST['touch_screen'])
        wifi=int(request.POST['wifi'])
        #print(battery_power	blue	clock_speed	dual_sim	fc	four_g	int_memory	m_dep	mobile_wt	n_cores	pc	px_height	px_width	ram	sc_h	sc_w	talk_time	three_g	touch_screen	wifi	price_range)
        
        result=k.predict([[Bp,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]])
        return render(request,"index.html",{"result":result})
    else:
         return render(request,"base.html")   
    
 
   

    
        

  
