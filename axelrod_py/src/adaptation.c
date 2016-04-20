
#include "adaptation.h"

int adaptation(axl_mass_media *mm, axl_network mysys, int feat2change)
{
	/* 
	It adapts Mass Media according to the current strategy.

	Three adaptive strategies are defined:
	Global Strategy (number 1): the Media takes the most abundant value in all the features.
	Followers Strategy (number 2): similar to Global, but the Media looks only for those agents who are followers.
	Non-Followers Strategy (number 3): similar to Global, but the Media looks for those agents who are NOT followers yet.

	Number 0 stands for fixed strategy, a Media which is not adaptive, not included here.
	*/

	int i, max_value;
	int *values;
        int q = mm->q;
        int n = mysys.nagents;
        int edit_secc = mm->edit_secc;
        int edit_line = mm->edit_line;
        int change = 0;


        if(feat2change != edit_secc)
	{
		values = (int *)malloc(sizeof(int)*q);

		for(i = 0; i < q; i++) 
			values[i] = 0;
	
		switch(mm->strategy)
		{
			// Global strategy
			case 1:
				for(i = 0; i < n; i++) 
					values[(mysys.agent[i].feat[feat2change])]++;
				break;
	
			// Followers strategy
			case 2:
				for(i = 0; i < n; i++) 
				{
					if(mysys.agent[i].feat[edit_secc] == edit_line)
						values[(mysys.agent[i].feat[feat2change])]++;
				}
				break;

			// Non - followers strategy
			case 3:
				for(i = 0; i < n; i++) 
				{
					if(mysys.agent[i].feat[edit_secc] != edit_line)
						values[(mysys.agent[i].feat[feat2change])]++;
				}
				break;
		}


		max_value = max(q, values, mm->feat[feat2change]);
                
                if(max_value != mm->feat[feat2change])
			change += 1;

	        mm->feat[feat2change] = max_value;

		free(values);
	}
	
        return change;
}
	
int max(int q, int *values, int mm_feature)
{
		/* Auxiliar function: it looks for the maxim value of an array */
		int i, max_value;

                max_value = mm_feature;
		
		for(i = 0; i < q; i++)
		{
			if(values[i] > values[max_value]) 
				max_value = i;
		}
		
		return max_value;       
}
