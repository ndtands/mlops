def norm_model(text: str) -> str:
    dict_model = {
        'Sedan':'Sedan',
        'SUV':'Sedan', 
        'Crossover':'Crossover', 
        'Bán tải / Pickup':'Pickup', 
        'Van/Minivan':'Minivan',
        'Hatchback':'Hatchback', 
        'Truck':'Truck', 
        'Convertible/Cabriolet':'Cabriolet', 
        'Coupe':'Coupe'
    }
    return dict_model[text]

def norm_driver(text: str) -> str:
    dict_driver = {
        'RFD - Dẫn động cầu sau':'RFD',
        'AWD - 4 bánh toàn thời gian':'AWD', 
        'FWD - Dẫn động cầu trước':'FWD', 
        '4WD - Dẫn động 4 bánh':'4WD', 
    }
    return dict_driver[text]

def norm_km(text: str) -> int:
    return int(text.split('Km')[0].strip().replace(',',""))

def norm_status(text: str) -> str:
    dict_norm = {
        'Xe mới' : 'new',
        'Xe đã dùng' : 'old'
    }   
    return dict_norm[text]

def norm_origin(text: str) -> str:
    dict_origin = {
        'Lắp ráp trong nước' : 'domestic',
        'Nhập khẩu' : 'imported',
        'nhập khẩu': 'imported',
    }   
    return dict_origin[text]

def norm_fuel(text: str) -> str:
    if 'Xăng' in text:
        return 'gasoline'
    if 'Dầu' in text:
        return 'diesel'
    else:
        return 'diesel'

def norm_gearbox(text: str) -> str:
    dict_gearbox = {
        'Số tự động' : 'automatic',
        'Số tay' : 'manual',
    }   
    return dict_gearbox[text]