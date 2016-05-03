

metric = 1;
q=40;
c=mat2str(metric);


clr = lines(60);


for Bmf = 10:10:60
    Bmf = Bmf - 10;
    Bmf2=Bmf/100.0;
    b = mat2str(Bmf2);
    name=strcat("Adherentes_Smax_talibanes_",b,"_Z_20.txt"); 
    if(Bmf == 0)
        name=strcat("Adherentes_Smax_talibanes_0.0_Z_20.txt"); 
    endif
     
    data=load(name);

    x=data(:,1);
    y=data(:,2);
    z=data(:,3);
    w=data(:,4);
        
    plot(x,y,'.-','Color',clr(Bmf+1,:));
    title("Smax vs q para distintas cantidades de talibanes, qz=100");
    xlabel("q");
    ylabel("Smax");

    hold on
endfor

    hold off

    str = cellstr( num2str((0.0:0.1:0.5)','Bmf=%g') );
    legend(str)
    saveas(gcf,strcat('Smaxvsq.jpg'));
    
for Bmf = 10:10:60
    Bmf = Bmf - 10;
    Bmf2=Bmf/100.0;
    b = mat2str(Bmf2);
    name=strcat("Adherentes_Smax_talibanes_",b,"_Z_20.txt");  
    if(Bmf == 0)
        name=strcat("Adherentes_Smax_talibanes_0.0_Z_20.txt"); 
    endif
    data=load(name);

    x=data(:,1);
    y=data(:,2);
    z=data(:,3);
    w=data(:,4);
        
    plot(x,w,'.-','Color',clr(Bmf+1,:));
    title("Fraccion de adherentes a la opinion de los talibanes en el primer feature vs q, qz=100");
    xlabel("q");
    ylabel("Fraccion de adherentes");
    axis([0 100 0 1.1])
    
    hold on
endfor

    hold off

    str = cellstr( num2str((0.0:0.1:0.5)','Bmf=%g') );
    legend(str)
    saveas(gcf,strcat('adherentesvsq.jpg'));    
