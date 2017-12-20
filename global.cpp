int fun(int a){
int cores = gpr_cpu_num_cores();
    if (!cores) cores = 4;
        return new DynamicThreadPool(cores);
}