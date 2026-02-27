import random
import string
import json
import time
import requests
import uuid
import base64
import io
import struct
import sys
import os
import re

# ==========================================
# COLORS AND STYLING - CYBERPUNK THEME
# ==========================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

def neon_print(text, color=CYAN, delay=0.005):
    """Neon typing effect with glow"""
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_print(text, color=GREEN):
    """Glitch text effect"""
    glitch_chars = ["█", "▓", "▒", "░", "▀", "▄", "▌", "▐"]
    for char in text:
        if random.random() > 0.9:
            sys.stdout.write(f"{DIM}{random.choice(glitch_chars)}{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def matrix_loading(text="PROCESSING", duration=3):
    """Matrix style loading"""
    chars = ["⎺", "⎻", "⎼", "⎽", "⎼", "⎻"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        color = random.choice([GREEN, CYAN, MAGENTA])
        bar = f"{chars[i % len(chars)]}" * 20
        sys.stdout.write(f"\r{color}{BOLD}[{bar}] {text}...{RESET}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 60 + "\r")

def hologram_box(title, content_list, width=70):
    """3D Hologram style box"""
    print(f"\n{CYAN}{BOLD}╔{'═' * (width-2)}╗{RESET}")
    print(f"{CYAN}{BOLD}║{MAGENTA}{title:^{width-2}}{CYAN}║{RESET}")
    print(f"{CYAN}{BOLD}╠{'═' * (width-2)}╣{RESET}")
    for item in content_list:
        print(f"{CYAN}{BOLD}║{RESET} {item:<{width-4}} {CYAN}{BOLD}║{RESET}")
    print(f"{CYAN}{BOLD}╚{'═' * (width-2)}╝{RESET}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """3D Animated Banner"""
    banner = [
        f"{CYAN}{BOLD}    ░██████╗████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗{RESET}",
        f"{BLUE}{BOLD}    ██╔════╝╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║{RESET}",
        f"{MAGENTA}{BOLD}    ║░██╗░████╗░██║░░░███████║█████═╝░█████╗░░██╔██╗██║{RESET}",
        f"{RED}{BOLD}    ║░╚═╝░██╔╝░██║░░░██╔══██║██╔═██╗░██╔══╝░░██║╚████║{RESET}",
        f"{YELLOW}{BOLD}    ╚██████╔╝░░██║░░░██║░░██║██║░╚██╗███████╗██║░╚███║{RESET}",
        f"{GREEN}{BOLD}    ░╚═════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝{RESET}",
        f"{CYAN}{BOLD}         ░█████╗░██████╗░███████╗███╗░░███╗░█████╗░██████╗░███████╗{RESET}",
        f"{BLUE}{BOLD}         ██╔══██╗██╔══██╗██╔════╝████╗░████║██╔══██╗██╔══██╗██╔════╝{RESET}",
        f"{MAGENTA}{BOLD}         ██║░░╚═╝██████╔╝█████╗░░██╔██╗██║██║░░██║██║░░██║█████╗░░{RESET}",
        f"{RED}{BOLD}         ██║░░██╗██╔══██╗██╔══╝░░██║╚████║██║░░██║██║░░██║██╔══╝░░{RESET}",
        f"{YELLOW}{BOLD}         ╚█████╔╝██║░░██║███████╗██║░╚███║╚█████╔╝██████╔╝███████╗{RESET}",
        f"{GREEN}{BOLD}         ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═════╝░╚══════╝{RESET}",
    ]
    
    for line in banner:
        print(line)
        time.sleep(0.05)
    
    print(f"\n{CYAN}{BOLD}{'═' * 75}{RESET}")
    glitch_print("              [ SYSTEM BREACH PROTOCOL - TOKEN GRENADE V9.0 ]", MAGENTA)
    print(f"{CYAN}{BOLD}{'═' * 75}{RESET}\n")

# ==========================================
# CRYPTO CHECK
# ==========================================
try:
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
except ImportError:
    print(f"{RED}{BOLD}[!] ERROR: 'pycryptodome' module not found.{RESET}")
    print(f"{YELLOW}[*] Run: pip install pycryptodome{RESET}")
    exit()

# ==========================================
# CORE CLASSES
# ==========================================

class FacebookPasswordEncryptor:
    @staticmethod
    def get_public_key():
        try:
            url = 'https://b-graph.facebook.com/pwd_key_fetch'
            params = {
                'version': '2',
                'flow': 'CONTROLLER_INITIALIZATION',
                'method': 'GET',
                'fb_api_req_friendly_name': 'pwdKeyFetch',
                'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
            }
            response = requests.post(url, params=params).json()
            return response.get('public_key'), str(response.get('key_id', '25'))
        except Exception as e:
            raise Exception(f"Public key fetch error: {e}")

    @staticmethod
    def encrypt(password, public_key=None, key_id="25"):
        if public_key is None:
            public_key, key_id = FacebookPasswordEncryptor.get_public_key()

        try:
            rand_key = get_random_bytes(32)
            iv = get_random_bytes(12)
            
            pubkey = RSA.import_key(public_key)
            cipher_rsa = PKCS1_v1_5.new(pubkey)
            encrypted_rand_key = cipher_rsa.encrypt(rand_key)
            
            cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
            current_time = int(time.time())
            cipher_aes.update(str(current_time).encode("utf-8"))
            encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
            
            buf = io.BytesIO()
            buf.write(bytes([1, int(key_id)]))
            buf.write(iv)
            buf.write(struct.pack("<h", len(encrypted_rand_key)))
            buf.write(encrypted_rand_key)
            buf.write(auth_tag)
            buf.write(encrypted_passwd)
            
            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"#PWD_FB4A:2:{current_time}:{encoded}"
        except Exception as e:
            raise Exception(f"Encryption error: {e}")


class FacebookAppTokens:
    APPS = {
        'FB_ANDROID': {'name': 'Facebook For Android', 'app_id': '350685531728'},
        'CONVO_TOKEN V7': {'name': 'Facebook Messenger For Android', 'app_id': '256002347743983'},
        'FB_LITE': {'name': 'Facebook For Lite', 'app_id': '275254692598279'},
        'MESSENGER_LITE': {'name': 'Facebook Messenger For Lite', 'app_id': '200424423651082'},
        'ADS_MANAGER_ANDROID': {'name': 'Ads Manager App For Android', 'app_id': '438142079694454'},
        'PAGES_MANAGER_ANDROID': {'name': 'Pages Manager For Android', 'app_id': '121876164619130'}
    }
    
    @staticmethod
    def get_app_id(app_key):
        app = FacebookAppTokens.APPS.get(app_key)
        return app['app_id'] if app else None
    
    @staticmethod
    def get_all_app_keys():
        return list(FacebookAppTokens.APPS.keys())
    
    @staticmethod
    def extract_token_prefix(token):
        for i, char in enumerate(token):
            if char.islower():
                return token[:i]
        return token


class FacebookLogin:
    API_URL = "https://b-graph.facebook.com/auth/login"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    API_KEY = "882a8490361da98702bf97a021ddc14d"
    SIG = "214049b9f17c38bd767de53752b53946"
    
    BASE_HEADERS = {
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-net-hni": "45201",
        "zero-rated": "0",
        "x-fb-sim-hni": "45201",
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-friendly-name": "authenticate",
        "x-fb-connection-bandwidth": "78032897",
        "x-tigon-is-retry": "False",
        "authorization": "OAuth null",
        "x-fb-connection-type": "WIFI",
        "x-fb-device-group": "3342",
        "priority": "u=3,i",
        "x-fb-http-engine": "Liger",
        "x-fb-client-ip": "True",
        "x-fb-server-cluster": "True"
    }
    
    def __init__(self, uid_phone_mail, password, machine_id=None, convert_token_to=None, convert_all_tokens=False):
        self.uid_phone_mail = uid_phone_mail
        
        if password.startswith("#PWD_FB4A"):
            self.password = password
        else:
            self.password = FacebookPasswordEncryptor.encrypt(password)
        
        if convert_all_tokens:
            self.convert_token_to = FacebookAppTokens.get_all_app_keys()
        elif convert_token_to:
            self.convert_token_to = convert_token_to if isinstance(convert_token_to, list) else [convert_token_to]
        else:
            self.convert_token_to = []
        
        self.session = requests.Session()
        
        self.device_id = str(uuid.uuid4())
        self.adid = str(uuid.uuid4())
        self.secure_family_device_id = str(uuid.uuid4())
        self.machine_id = machine_id if machine_id else self._generate_machine_id()
        self.jazoest = ''.join(random.choices(string.digits, k=5))
        self.sim_serial = ''.join(random.choices(string.digits, k=20))
        
        self.headers = self._build_headers()
        self.data = self._build_data()
    
    @staticmethod
    def _generate_machine_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    
    def _build_headers(self):
        headers = self.BASE_HEADERS.copy()
        headers.update({
            "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; 23113RKC6C Build/PQ3A.190705.08211809) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/480086274;FBCR/MobiFone;FBMF/Redmi;FBBD/Redmi;FBDV/23113RKC6C;FBSV/9;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;FBRV/0;]"
        })
        return headers
    
    def _build_data(self):
        base_data = {
            "format": "json",
            "email": self.uid_phone_mail,
            "password": self.password,
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "locale": "vi_VN",
            "client_country_code": "VN",
            "api_key": self.API_KEY,
            "access_token": self.ACCESS_TOKEN
        }
        
        base_data.update({
            "adid": self.adid,
            "device_id": self.device_id,
            "generate_analytics_claim": "1",
            "community_id": "",
            "linked_guest_account_userid": "",
            "cpl": "true",
            "try_num": "1",
            "family_device_id": self.device_id,
            "secure_family_device_id": self.secure_family_device_id,
            "sim_serials": f'["{self.sim_serial}"]',
            "openid_flow": "android_login",
            "openid_provider": "google",
            "openid_tokens": "[]",
            "account_switcher_uids": f'["{self.uid_phone_mail}"]',
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "enroll_misauth": "false",
            "error_detail_type": "button_with_disabled",
            "source": "login",
            "machine_id": self.machine_id,
            "jazoest": self.jazoest,
            "meta_inf_fbmeta": "V2_UNTAGGED",
            "advertiser_id": self.adid,
            "encrypted_msisdn": "",
            "currently_logged_in_userid": "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "Fb4aAuthHandler",
            "sig": self.SIG
        })
        
        return base_data
    
    def _convert_token(self, access_token, target_app):
        try:
            app_id = FacebookAppTokens.get_app_id(target_app)
            if not app_id:
                return None
            
            response = requests.post(
                'https://api.facebook.com/method/auth.getSessionforApp',
                data={
                    'access_token': access_token,
                    'format': 'json',
                    'new_app_id': app_id,
                    'generate_session_cookies': '1'
                }
            )
            
            result = response.json()
            
            if 'access_token' in result:
                token = result['access_token']
                prefix = FacebookAppTokens.extract_token_prefix(token)
                
                cookies_dict = {}
                cookies_string = ""
                
                if 'session_cookies' in result:
                    for cookie in result['session_cookies']:
                        cookies_dict[cookie['name']] = cookie['value']
                        cookies_string += f"{cookie['name']}={cookie['value']}; "
                
                return {
                    'token_prefix': prefix,
                    'access_token': token,
                    'cookies': {
                        'dict': cookies_dict,
                        'string': cookies_string.rstrip('; ')
                    }
                }
            return None     
        except:
            return None
    
    def _parse_success_response(self, response_json):
        original_token = response_json.get('access_token')
        original_prefix = FacebookAppTokens.extract_token_prefix(original_token)
        
        result = {
            'success': True,
            'original_token': {
                'token_prefix': original_prefix,
                'access_token': original_token
            },
            'cookies': {}
        }
        
        if 'session_cookies' in response_json:
            cookies_dict = {}
            cookies_string = ""
            for cookie in response_json['session_cookies']:
                cookies_dict[cookie['name']] = cookie['value']
                cookies_string += f"{cookie['name']}={cookie['value']}; "
            result['cookies'] = {
                'dict': cookies_dict,
                'string': cookies_string.rstrip('; ')
            }
        
        if self.convert_token_to:
            result['converted_tokens'] = {}
            for target_app in self.convert_token_to:
                converted = self._convert_token(original_token, target_app)
                if converted:
                    result['converted_tokens'][target_app] = converted
        
        return result
    
    def _handle_2fa_manual(self, error_data):
        print(f"\n{YELLOW}{BOLD}{'▓' * 75}{RESET}")
        glitch_print("[!] SECURITY BREACH DETECTED - 2FA REQUIRED", RED)
        print(f"{YELLOW}{BOLD}{'▓' * 75}{RESET}\n")
        
        neon_print("[*] Facebook has dispatched an OTP to your secure device.", CYAN)
        neon_print("[*] Please enter the verification code below.", CYAN)
        print(f"{CYAN}{BOLD}{'─' * 75}{RESET}\n")
        
        try:
            otp_code = input(f"{GREEN}{BOLD}[+] ENTER 2FA CODE ➤ {RESET}").strip()
            print()
        except KeyboardInterrupt:
            return {'success': False, 'error': 'User cancelled OTP input'}

        if not otp_code:
             return {'success': False, 'error': 'Empty OTP provided'}

        matrix_loading("VERIFYING 2FA", 2)

        try:
            data_2fa = {
                'locale': 'vi_VN',
                'format': 'json',
                'email': self.uid_phone_mail,
                'device_id': self.device_id,
                'access_token': self.ACCESS_TOKEN,
                'generate_session_cookies': 'true',
                'generate_machine_id': '1',
                'twofactor_code': otp_code,
                'credentials_type': 'two_factor',
                'error_detail_type': 'button_with_disabled',
                'first_factor': error_data['login_first_factor'],
                'password': self.password,
                'userid': error_data['uid'],
                'machine_id': error_data['login_first_factor']
            }
            
            response = self.session.post(self.API_URL, data=data_2fa, headers=self.headers)
            response_json = response.json()
            
            if 'access_token' in response_json:
                return self._parse_success_response(response_json)
            elif 'error' in response_json:
                return {
                    'success': False,
                    'error': response_json['error'].get('message', 'OTP Verification Failed')
                }
            
        except Exception as e:
            return {'success': False, 'error': f'2FA Processing Error: {str(e)}'}
    
    def login(self):
        try:
            matrix_loading("ENCRYPTING CREDENTIALS", 2)
            response = self.session.post(self.API_URL, headers=self.headers, data=self.data)
            response_json = response.json()
            
            if 'access_token' in response_json:
                return self._parse_success_response(response_json)
            
            if 'error' in response_json:
                error_data = response_json.get('error', {}).get('error_data', {})
                
                if 'login_first_factor' in error_data and 'uid' in error_data:
                    return self._handle_2fa_manual(error_data)
                
                return {
                    'success': False,
                    'error': response_json['error'].get('message', 'Unknown error'),
                    'error_user_msg': response_json['error'].get('error_user_msg')
                }
            
            return {'success': False, 'error': 'Unknown response format'}
            
        except json.JSONDecodeError:
            return {'success': False, 'error': 'Invalid JSON response'}
        except Exception as e:
            return {'success': False, 'error': str(e)}


class CookieTokenExtractor:
    """Extract EAD Token from Cookies"""
    
    @staticmethod
    def extract_from_cookies(cookie_string):
        """Extract token from cookies using Facebook API"""
        try:
            # Parse cookies
            cookies = {}
            for pair in cookie_string.split(';'):
                if '=' in pair:
                    key, value = pair.strip().split('=', 1)
                    cookies[key] = value
            
            # Try to get EAD token using cookies
            session = requests.Session()
            
            # Set cookies in session
            for key, value in cookies.items():
                session.cookies.set(key, value)
            
            # Try multiple endpoints to get token
            endpoints = [
                'https://business.facebook.com/business_locations',
                'https://www.facebook.com/adsmanager',
                'https://www.facebook.com/ads/library'
            ]
            
            tokens_found = []
            
            for endpoint in endpoints:
                try:
                    response = session.get(endpoint, allow_redirects=True, timeout=10)
                    
                    # Look for EAD token in response
                    patterns = [
                        r'"accessToken":"([^"]+)"',
                        r'"token":"([^"]+)"',
                        r'EAAD[^"\s<]+',
                        r'EAA[AV][^"\s<]+'
                    ]
                    
                    for pattern in patterns:
                        matches = re.findall(pattern, response.text)
                        for match in matches:
                            if len(match) > 50 and match not in [t['token'] for t in tokens_found]:
                                token_type = 'EAD' if 'EAAD' in match else 'EAAV' if 'EAAV' in match else 'EAA'
                                tokens_found.append({
                                    'type': token_type,
                                    'token': match,
                                    'source': endpoint
                                })
                except:
                    continue
            
            # Try Graph API with cookies
            if 'c_user' in cookies:
                try:
                    graph_url = f"https://graph.facebook.com/me?access_token={cookies.get('access_token', '')}"
                    # Alternative method using fb_dtsg
                    if 'fb_dtsg' in cookies:
                        fb_dtsg = cookies['fb_dtsg']
                        # Try to exchange for token
                        token_url = 'https://www.facebook.com/dialog/oauth'
                        params = {
                            'client_id': '124024574287414',
                            'redirect_uri': 'fbconnect://success',
                            'scope': 'email',
                            'response_type': 'token',
                            'fb_dtsg': fb_dtsg
                        }
                        resp = session.get(token_url, params=params, allow_redirects=False)
                        if 'access_token=' in resp.headers.get('location', ''):
                            token = re.search(r'access_token=([^&]+)', resp.headers['location'])
                            if token:
                                tokens_found.append({
                                    'type': 'MOBILE',
                                    'token': token.group(1),
                                    'source': 'OAuth Dialog'
                                })
                except:
                    pass
            
            return {
                'success': len(tokens_found) > 0,
                'tokens': tokens_found,
                'cookies': cookies
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e), 'tokens': []}


# ==========================================
# MAIN MENU SYSTEM
# ==========================================

def show_menu():
    """3D Interactive Menu"""
    print(f"\n{CYAN}{BOLD}╔{'═' * 73}╗{RESET}")
    print(f"{CYAN}{BOLD}║{MAGENTA}{'SELECT ACCESS PROTOCOL':^73}{CYAN}║{RESET}")
    print(f"{CYAN}{BOLD}╠{'═' * 73}╣{RESET}")
    print(f"{CYAN}{BOLD}║{RESET}  {GREEN}{BOLD}[1]{RESET} {WHITE}GMAIL/PHONE + PASSWORD + 2FA{RESET}                                    {CYAN}{BOLD}║{RESET}")
    print(f"{CYAN}{BOLD}║{RESET}  {YELLOW}{BOLD}[2]{RESET} {WHITE}COOKIE TOKEN EXTRACTION (EAD){RESET}                                   {CYAN}{BOLD}║{RESET}")
    print(f"{CYAN}{BOLD}╚{'═' * 73}╝{RESET}\n")


def option_1_login():
    """Option 1: Email/Phone + Password + 2FA"""
    print(f"\n{GREEN}{BOLD}{'▓' * 75}{RESET}")
    glitch_print("[ PROTOCOL 1 ] CREDENTIAL-BASED AUTHENTICATION", GREEN)
    print(f"{GREEN}{BOLD}{'▓' * 75}{RESET}\n")
    
    # Input with styling
    uid_phone_mail = input(f"{CYAN}{BOLD}[+] ENTER GMAIL/PHONE NUMBER ➤ {RESET}").strip()
    print(f"{DIM}{'─' * 75}{RESET}\n")
    
    password = input(f"{CYAN}{BOLD}[+] ENTER PASSWORD ➤ {RESET}").strip()
    print(f"{DIM}{'─' * 75}{RESET}\n")
    
    fb_login = FacebookLogin(
        uid_phone_mail=uid_phone_mail,
        password=password,
        convert_all_tokens=True
    )
    
    result = fb_login.login()
    
    if result['success']:
        print(f"\n{GREEN}{BOLD}{'█' * 75}{RESET}")
        glitch_print("[ ACCESS GRANTED ] LOGIN SUCCESSFUL", GREEN)
        print(f"{GREEN}{BOLD}{'█' * 75}{RESET}\n")
        
        hologram_box("PRIMARY TOKEN", [
            f"{YELLOW}TYPE: {RESET}{result['original_token']['token_prefix']}",
            f"{GREEN}{result['original_token']['access_token'][:50]}...{RESET}"
        ])
        
        if 'converted_tokens' in result and result['converted_tokens']:
            print(f"{CYAN}{BOLD}{'▓' * 75}{RESET}")
            glitch_print("[ TOKEN GRENADE ] GENERATING MULTI-APP TOKENS", CYAN)
            print(f"{CYAN}{BOLD}{'▓' * 75}{RESET}\n")
            
            for app_key, token_data in result['converted_tokens'].items():
                print(f"{MAGENTA}{BOLD}◆ {app_key} ({token_data['token_prefix']}){RESET}")
                print(f"{GREEN}{token_data['access_token']}{RESET}\n")
                print(f"{DIM}{'─' * 75}{RESET}\n")
        
        # Cookies
        print(f"{YELLOW}{BOLD}{'▓' * 75}{RESET}")
        glitch_print("[ SESSION COOKIES ]", YELLOW)
        print(f"{YELLOW}{BOLD}{'▓' * 75}{RESET}\n")
        print(f"{CYAN}{result['cookies']['string']}{RESET}\n")
        
    else:
        print(f"\n{RED}{BOLD}{'█' * 75}{RESET}")
        glitch_print("[ ACCESS DENIED ] LOGIN FAILED", RED)
        print(f"{RED}{BOLD}{'█' * 75}{RESET}\n")
        print(f"{YELLOW}Error: {result.get('error')}{RESET}")
        if result.get('error_user_msg'):
            print(f"{YELLOW}Details: {result.get('error_user_msg')}{RESET}")
        print()


def option_2_cookie():
    """Option 2: Cookie to Token"""
    print(f"\n{MAGENTA}{BOLD}{'▓' * 75}{RESET}")
    glitch_print("[ PROTOCOL 2 ] COOKIE EXTRACTION MODULE", MAGENTA)
    print(f"{MAGENTA}{BOLD}{'▓' * 75}{RESET}\n")
    
    neon_print("[*] Paste your Facebook cookies below (format: datr=...; c_user=...; xs=...)", CYAN)
    print(f"{DIM}{'─' * 75}{RESET}\n")
    
    cookies = input(f"{YELLOW}{BOLD}[+] ENTER COOKIES ➤ {RESET}").strip()
    print()
    
    if not cookies:
        print(f"{RED}[!] No cookies provided{RESET}\n")
        return
    
    matrix_loading("EXTRACTING TOKENS", 3)
    
    extractor = CookieTokenExtractor()
    result = extractor.extract_from_cookies(cookies)
    
    if result['success'] and result['tokens']:
        print(f"\n{GREEN}{BOLD}{'█' * 75}{RESET}")
        glitch_print("[ EXTRACTION COMPLETE ] TOKENS FOUND", GREEN)
        print(f"{GREEN}{BOLD}{'█' * 75}{RESET}\n")
        
        for idx, token_info in enumerate(result['tokens'], 1):
            hologram_box(f"TOKEN #{idx} - {token_info['type']}", [
                f"{YELLOW}SOURCE: {RESET}{token_info['source']}",
                f"{GREEN}{token_info['token']}{RESET}"
            ])
        
        # Also try to get user info from cookies
        if 'c_user' in result['cookies']:
            try:
                user_id = result['cookies']['c_user']
                print(f"{CYAN}{BOLD}{'▓' * 75}{RESET}")
                print(f"{CYAN}User ID Extracted: {WHITE}{user_id}{RESET}")
                print(f"{CYAN}{BOLD}{'▓' * 75}{RESET}\n")
            except:
                pass
    else:
        print(f"\n{RED}{BOLD}{'█' * 75}{RESET}")
        glitch_print("[ EXTRACTION FAILED ] NO TOKENS FOUND", RED)
        print(f"{RED}{BOLD}{'█' * 75}{RESET}\n")
        if result.get('error'):
            print(f"{YELLOW}Error: {result['error']}{RESET}\n")
        print(f"{CYAN}[*] Try using Option 1 (Email/Password) for fresh tokens{RESET}\n")


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    clear_screen()
    show_banner()
    
    while True:
        show_menu()
        
        try:
            choice = input(f"{GREEN}{BOLD}[?] SELECT PROTOCOL (1/2) ➤ {RESET}").strip()
            print()
            
            if choice == '1':
                option_1_login()
            elif choice == '2':
                option_2_cookie()
            else:
                print(f"{RED}[!] Invalid selection. Choose 1 or 2.{RESET}\n")
                continue
            
            # Ask to continue
            print(f"{CYAN}{BOLD}{'─' * 75}{RESET}")
            again = input(f"{YELLOW}{BOLD}[?] RUN ANOTHER PROTOCOL? (y/n) ➤ {RESET}").strip().lower()
            print()
            
            if again != 'y':
                print(f"{GREEN}{BOLD}{'█' * 75}{RESET}")
                glitch_print("[ SYSTEM SHUTDOWN ] GOODBYE", CYAN)
                print(f"{GREEN}{BOLD}{'█' * 75}{RESET}\n")
                break
            clear_screen()
            show_banner()
            
        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] Interrupted by user{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Error: {e}{RESET}\n")
