# made by wangzhi
# TX_Leo
'''生成一个定制的QRCode，并与自己做的html联系起来'''
from MyQR import myqr # 需先安装MyQR库

def QR_myqr():
    myqr.run(
        '''是通过将html_generate.html上传到腾讯云上，然后将其生成一个网页连接，然后将QRcode和这个链接联系起来'''
        'https://qr-code-1306942182.cos-website.ap-beijing.myqcloud.com/', # 二维码指向链接，或无格式文本（但不支持中文）
        version = 5, # 大小1~40
        level='H', # 纠错级别
        picture = 'img.png', # 底图路径
        colorized = True, # 彩色
        contrast = 1.0, # 对比度
        brightness = 1.0, # 亮度
        save_name = 'QR_code.png', # 保存文件名
        save_dir = r'D:\python\projects\fun\QR_code' #保存目录
    )
QR_myqr()