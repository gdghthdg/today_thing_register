import hashlib

# 待加密信息
def encrypt_str(str):

    # 创建md5对象
    m = hashlib.md5()

    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')

    m.update(b)
    str_md5 = m.hexdigest()

    #print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + str_md5)

    # 另一种写法：b‘’前缀代表的就是bytes
    #str_md5 = hashlib.md5(b'change').hexdigest()

    #print('MD5加密后为 ：' + str_md5)
    return str_md5


encrypt_str('172.17.130.107:5900')
encrypt_str('management')
encrypt_str('sa')
encrypt_str('666999')

