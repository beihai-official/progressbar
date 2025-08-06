def run(bar_long=50,wait_time=10,did_bar="█",over_bar="-"):#bar_long为进度条长度，wait_time为进度条总时间,did_bar为进度条前部分样式，over_bar为后部分样式
    current = 0
    import time
    start_time =time.time()
    while current <= bar_long:
        now_time =time.time()
        print(f"{"[INFO]"}{time.strftime("[%H:%M:%S]")}{(did_bar) * current}{(over_bar) * (bar_long - current)}{int(((current / bar_long) * 100))}{"/100"} {"用时:"}{((now_time) - (start_time)):.2f}{"S"}",end='\r',flush=True)
        current += 1
        time.sleep(wait_time/bar_long)
    print(f"""{"[INFO]"}{time.strftime("[%H:%M:%S]")}{(did_bar) * bar_long}{"用时:"}{((time.time()-start_time)):.2f}S Successful""",flush= True)