
curva=1

data=load("Prueba.txt");

    x=data(:,1);
    y=data(:,2);
    ey=data(:,3);
    #z=data(:,4);
    
#Una sola curva

if(curva==1)

    errorbar(x,y,ey,'.');
    title("Smax vs q, 1 feature meterico, primeros vecinos");
    xlabel("q");
    ylabel("smax");
    print -djpg prueba.jpg

endif

#Mas de una curva

if(curva==2)
    data2=load("Data_smax_near_prueba2.txt");
    x2=data2(:,1);
    y2=data2(:,2);
    ey2=data2(:,3);
    z=data2(:,4);
    
    plot(x,y,'.',x2,y2,'.');
    title("Smax vs q, 1 feature metrico, primeros vecinos");
    xlabel("q");
    ylabel("smax");
    legend("near = 4, feature =1","near=1, feature =1")
    print -djpg comparacion.jpg
        
endif

if(curva==3)
    data2=load("Data_smax_near_prueba2.txt");
    x2=data2(:,1);
    y2=data2(:,2);
    ey2=data2(:,3);
    z2=data2(:,4);
    
    data3=load("Data_smax_near_prueba3.txt");
    x3=data3(:,1);
    y3=data3(:,2);
    ey3=data3(:,3);
    z3=data3(:,4);
    
    plot(x,z,'.-',x2,z2,'.-',x3,z3,'.-');
    title("Pasos Sincronicos hasta convergencia vs q, 1 feature metrico, primeros vecinos,1024 agentes");
    xlabel("q");
    ylabel("Pasos Sincronicos hasta convergencia");
    legend("near = 4, feature metrico=1","near=1, feature metrico=1","feature metrico=0")
    print -djpg PasosConvergencia.jpg
        
endif
