import md5

def md5_generator(s):
    m = md5.new()
    
    m.update(s)
    
    return m.hexdigest()
    


print md5_generator('alexrobot4@qq.com')
