//! @author: @ruhend(Mudigonda Himansh)
//! Assignment 5
//! SRTF

#include <stdio.h>

struct process_info
{
    int p_no;
    int burst_time;
    int arrival_time;
    int remaining_time;
};

void SRTF(struct process_info process_array[])
{
    int processes_left[5];
    int round = 0;
    int Flag = 1;
    printf("%d\n", process_array[0].burst_time);
    while (Flag == 1)
    {
        for (int i = 0; i <= 5; i++)
        {
            if (process_array[i].arrival_time == round)
            {
                processes_left[-1] = i;
            }
            if (process_array[i].remaining_time==0){
                for (int c = 0; c <= 5; c++){
                    
                }
            }
        }
        round++;
    }
}

int main()
{
    int number_of_processes = 5;
    struct process_info process_array[number_of_processes];
    process_array[0].p_no = 1;
    process_array[1].p_no = 2;
    process_array[2].p_no = 3;
    process_array[3].p_no = 4;
    process_array[4].p_no = 5;
    // burst time
    process_array[0].burst_time = 4;
    process_array[1].burst_time = 2;
    process_array[2].burst_time = 3;
    process_array[3].burst_time = 1;
    process_array[4].burst_time = 6;
    // arrival time
    process_array[0].arrival_time = 1;
    process_array[1].arrival_time = 0;
    process_array[2].arrival_time = 0;
    process_array[3].arrival_time = 2;
    process_array[4].arrival_time = 0;
    SRTF(process_array);

    return 0;
}

