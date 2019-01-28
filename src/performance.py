import socket
import time

def arg_timer(average=False):
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            times = 1000 if average else 1
            for i in range(times):
                func(*args, **kwargs)
            end = time.time()
            if average:
                print("   Start: %.9f\n     End: %.9f\nDuration: %.9f" % (start, end, (end - start) / times))
            else:
                print("   Start: %.9f\n     End: %.9f\nDuration: %.9f" % (start, end, end - start))
        return wrapper
    return timer


@arg_timer(average=True)
def touch():
    s = socket.socket()
    # address = 'www.baidu.com'
    address = '10.81.29.151'
    port = 8080  # port number is a number, not string
    try:
        s.connect((address, port)) 
        # originally, it was 
        # except Exception, e: 
        # but this syntax is not supported anymore. 
    except Exception as e: 
        print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
    finally:
        # s.close()
        pass

if __name__ == '__main__':
    touch()
