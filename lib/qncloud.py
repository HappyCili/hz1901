from qiniu import Auth, put_file, etag

from swiper import config


#需要填写你的 Access Key 和 Secret Key
def upload_to_qn(localfile, filename):
    ''' 将文件上传到七牛云 '''
    # 构建鉴权对象
    qn_auth = Auth(config.QN_AccessKey, config.QN_SecretKey)
    # 生成上传 Token，可以指定过期时间等
    token = qn_auth.upload_token(config.QN_BUCKET, filename, 3600)
    # 执行上传过程
    put_file(token, filename, localfile)
    file_url = "/".join([config.QN_BASEURL, filename])

    return file_url