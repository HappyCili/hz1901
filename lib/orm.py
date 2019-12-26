from datetime import date, time, datetime


def model_to_dict(model_obj, ignore=()):
    '''
    将一个 model 对象转换成一个字典
    属性操作相关的函数:
         hasattr(obj, att_name)
         setattr(obj, att_name,value)
         getattr(obj, att_name)
    '''
    attr_dict = {}
    for field in model_obj._meta.fields:
        name = field.attname    # 获取所有字段名
        if name not in ignore:
            value = getattr(model_obj, name)    # 根据字段名获取对应的值
            if isinstance(value, (date, time, datetime)):
                value = str(value)
            attr_dict[name] = value
    return attr_dict