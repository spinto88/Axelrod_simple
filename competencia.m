

metric = 1;
q=40;
c=mat2str(metric);


clrz = lines(60);
clrmf = lines(60);
str2 = cellstr( num2str((0:10:35)','Z=%g') );


for Bmf = 10:20:75
    f1 = figure(); hold on
    f2 = figure(); hold on
    f3 = figure(); hold on
    Bmf = Bmf - 10;
    Bmf2=Bmf/100.0;
    b = mat2str(Bmf2);
    
    for Z = 1:10:35
        Z = Z - 1;
        zealot = mat2str(Z);
            
        name=strcat("Adherentes_Smax_mf_",b,"_Z_",zealot,".txt"); 
        if(Bmf == 0)
            name=strcat("Adherentes_Smax_mf_0.0_Z_",zealot,".txt"); 
        endif
         
        data=load(name);

        q = data(:,1);
        smax = data(:,2);
        stdsmax = data(:,3);
        ade = data(:,4);
        stdade = data(:,5);
        vac = data(:,6);
        stdvac = data(:,7);
        
        figure(f1);    
        plot(q,smax,'.-','Color',clrz(Z+1,:));
        title("Smax vs q para distintas cantidades de talibanes, qz=100");
        xlabel("q");
        ylabel("Smax");
        axis([0 100 0 1050])
        legend(str2)
        
        figure(f2);        
        plot(q,vac,'.-','Color',clrz(Z+1,:));
        title("Vacunados vs q para distintas cantidades de talibanes, qz=100");
        xlabel("q");
        ylabel("Vacunados");
        axis([0 100 0 1050])
        legend(str2)
        
        figure(f3);        
        plot(q,ade,'.-','Color',clrz(Z+1,:));
        title("Fraccion de adherentes a vacunarse (primer feature = 0) vs q para distintas cantidades de talibanes, qz=100");
        xlabel("q");
        ylabel("Fraccion de adherentes");
        axis([0 100 0 0.13])
        legend(str2)
        
    endfor   
        
    hold off
    hold off

    
    
    saveas(f1,strcat('Smaxvsq_mf=',b,'.jpg'));
    saveas(f2,strcat('Vacunadosvsq_mf=',b,'.jpg'));
    saveas(f3,strcat('Adherentesvsq_mf=',b,'.jpg'));
endfor        
    


    
 
