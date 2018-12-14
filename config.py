import pathlib
import os
import sys

'''配置文件的相关参数'''

PROJECT_ROOT = pathlib.Path(__file__).parent
STATIC_ROOT = os.path.join(str(PROJECT_ROOT), 'static')
PY_PATH = os.path.join(STATIC_ROOT, 'file', 'py')
CSV_PATH = os.path.join(STATIC_ROOT, 'file', 'csv')

sys.path.append(PROJECT_ROOT)
template_dir =(os.path.join(os.path.dirname(__file__), 'views', 'templates'))

'''cookies headers 方面的设置'''
ALIBABA_COOKIES = """bl_uid=4hjC3gOj1jCmIdqgm0qXywU0Reez; __sw_newuno_count__=1; UM_distinctid=162cc509d7e27e-0c51bf3b043ca7-3a614f0b-1fa400-162cc509d7f265; cna=ZXNXE8S96S4CAXFBDvggMQRq; ali_ab=58.62.204.223.1523846560098.8; alisw=swIs1200%3D1%7C; JSESSIONID=HVAZVze-egXZ18KGzzSNPkuuI5-bDWijpQ-0U82; cookie2=13ae38c76cab37e63cc4c5dc0dfbd90d; hng=CN%7Czh-CN%7CCNY%7C156; t=d959a032db234b220c1e1d4d280c6cdf; _tb_token_=59e4b3a5355eb; __cn_logon__=false; alicnweb=homeIdttS%3D73667626261324062786414557300587367436%7Ctouch_tb_at%3D1524204922074%7ChomeIdttSAction%3Dtrue; _tmp_ck_0="21F8ti7O0vmBAlnjwre2n4QP2mCJ1j%2FYk%2B5kXJpnp%2FAhtrokV3nhqtKVLr4y5pMPashUXaS%2Bk91W%2FO93VgT6PeC2EQ5oidpKb6pWak0qgugpbRuCOlBaTotPRNamXlt3Fu3KpUzG%2Flp%2BGx%2Bjg8AsNrn7PwZzks01AzOfVjtTyfnmh%2BC98m27R97HsK%2Br9j9rPbJeZANFCRulQAyLQTE1lzm%2FTBibVr4DFeIIwUr%2BShG9XjQfjVrAUnk6hIUo7uvKANG0wrsJuEQabM639NdW93uosVQWnx0%2FcI6fT8nasyGztjgQysIIPH1X3p03kLM5l7V8SYQQOyqYdeuF%2FZBO3Osu7FWxATUMgS0fZRNM7sMauYdxooGRBjBFzGNh2LFDRs6b74NcPuA%3D"; _csrf_token=1524206882968; h_keys="iphone5#phone#%u5c0f%u7c73%u624b%u673a#phone6s#sumsung#oppo#book#apple#iphone7"; ad_prefer="2018/04/20 14:59:24"; isg=BIeH-nWrkccrNBVGRdZDHyZUFjuRJFGVCB-dGVl07JZ1yKeKYVzrvsWqboiWIDPm"""
DICT_ALIBABA_COOKIES = {}
DICT_ALIBABA_COOKIES_ARRAY = []

for c in ALIBABA_COOKIES.split(';'):
    name, value = c.split('=', 1)
    DICT_ALIBABA_COOKIES['name'] = name
    DICT_ALIBABA_COOKIES['value'] = value
    DICT_ALIBABA_COOKIES['path'] = '/selloffer/offer_search.htm?keywords=phone&n=y&spm=a260k.635.3262836.d102&beginPage=2&offset=0'
    DICT_ALIBABA_COOKIES['httponly'] = False
    DICT_ALIBABA_COOKIES['secure'] = False
    DICT_ALIBABA_COOKIES['domain'] = '.1688.com'

    DICT_ALIBABA_COOKIES_ARRAY.append(DICT_ALIBABA_COOKIES)

'''设置headers， cookies'''
COOKIES = {
    'alibaba': DICT_ALIBABA_COOKIES_ARRAY
}

HEADERS = {
    'alibaba': ''
}