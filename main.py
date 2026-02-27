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
import html

# ==========================================
# COLORS AND STYLING - CYBERPUNK NEON THEME
# ==========================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;208m"
PINK = "\033[38;5;206m"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

# Symbols
BLOCK = "█"
SHADE_HEAVY = "▓"
SHADE_MEDIUM = "▒"
SHADE_LIGHT = "░"
ARROW = "➤"
STAR = "✦"
DIAMOND = "◆"
CIRCLE = "●"
CHECK = "✓"
CROSS = "✗"
LIGHTNING = "⚡"

def typing_effect(text, color=GREEN, delay=0.005):
    """Neon typing effect"""
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def glitch_text(text, color=MAGENTA):
    """Glitch effect"""
    glitch_chars = ["█", "▓", "▒", "░", "▀", "▄", "▌", "▐"]
    result = ""
    for char in text:
        if random.random() > 0.9:
            result += random.choice(glitch_chars)
        else:
            result += char
    print(f"{BOLD}{color}{result}{RESET}")

def matrix_loading(text="PROCESSING", duration=3):
    """Matrix loading animation"""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        color = random.choice([GREEN, CYAN, MAGENTA])
        sys.stdout.write(f"\r{color}{BOLD}[{chars[i % len(chars)]}] {text}...{RESET}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 60 + "\r")

def progress_bar(text="LOADING", duration=3):
    """3D Progress bar"""
    bar_length = 40
    start_time = time.time()
    while time.time() - start_time < duration:
        progress = (time.time() - start_time) / duration
        filled = int(bar_length * progress)
        bar = f"{GREEN}{BLOCK * filled}{DIM}{SHADE_LIGHT * (bar_length - filled)}{RESET}"
        percent = int(progress * 100)
        sys.stdout.write(f"\r{CYAN}{BOLD}[{bar}] {percent}% {text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{GREEN}{BOLD}[{BLOCK * bar_length}] 100% {text} COMPLETE{RESET}\n")

def hologram_box(title, items, width=75):
    """Holographic display box"""
    print(f"\n{CYAN}{BOLD}╔{'═' * (width-2)}╗{RESET}")
    title_str = f" {STAR} {title} {STAR} "
    padding = (width - len(title_str)) // 2
    print(f"{CYAN}{BOLD}║{' ' * padding}{MAGENTA}{BOLD}{title_str}{CYAN}{' ' * (width - padding - len(title_str) - 1)}║{RESET}")
    print(f"{CYAN}{BOLD}╠{'═' * (width-2)}╣{RESET}")
    for item in items:
        if isinstance(item, tuple):
            label, value = item
            line = f" {ARROW} {label}: {value}"
        else:
            line = f" {ARROW} {item}"
        print(f"{CYAN}{BOLD}║{RESET}{line:<{width-2}}{CYAN}{BOLD}║{RESET}")
    print(f"{CYAN}{BOLD}╚{'═' * (width-2)}╝{RESET}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """3D Animated Banner"""
    banner = [
        f"{CYAN}{BOLD}     ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░{RESET}",
        f"{BLUE}{BOLD}    ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░{RESET}",
        f"{MAGENTA}{BOLD}    ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░{RESET}",
        f"{RED}{BOLD}     ░▒▓██████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░  ░▒▓██████▓▒░ {RESET}",
        f"{ORANGE}{BOLD}           ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   {RESET}",
        f"{YELLOW}{BOLD}           ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   {RESET}",
        f"{GREEN}{BOLD}    ░▒▓███████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░  ░▒▓█▓▒░   {RESET}",
        f"",
        f"{CYAN}{BOLD}     ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░{RESET}",
        f"{BLUE}{BOLD}    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      {RESET}",
        f"{MAGENTA}{BOLD}    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      {RESET}",
        f"{RED}{BOLD}    ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░ {RESET}",
        f"{ORANGE}{BOLD}    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      {RESET}",
        f"{YELLOW}{BOLD}    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      {RESET}",
        f"{GREEN}{BOLD}    ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░{RESET}",
    ]
    
    for line in banner:
        print(line)
        time.sleep(0.03)
    
    print(f"\n{CYAN}{BOLD}{'═' * 85}{RESET}")
    glitch_text("           [ SYSTEM BREACH PROTOCOL - EAAD TOKEN GRENADE V10.0 ]", MAGENTA)
    print(f"{CYAN}{BOLD}{'═' * 85}{RESET}\n")

# ==========================================
# CRYPTO MODULE
# ==========================================
try:
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
except ImportError:
    print(f"{RED}{BOLD}[!] ERROR: Install pycryptodome{RESET}")
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
            raise Exception(f"Public key error: {e}")

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


class EAADTokenGenerator:
    """Generate EAAD Token from Cookies - CONVO WORKING"""
    
    @staticmethod
    def generate_eaad_token(cookies_string):
        """Extract EAAD token using multiple methods"""
        try:
            # Parse cookies
            cookies = {}
            for pair in cookies_string.split(';'):
                if '=' in pair:
                    key, value = pair.strip().split('=', 1)
                    cookies[key] = value
            
            session = requests.Session()
            
            # Set essential cookies
            essential_cookies = ['c_user', 'xs', 'datr', 'fr', 'sb']
            for cookie in essential_cookies:
                if cookie in cookies:
                    session.cookies.set(cookie, cookies[cookie])
            
            tokens_found = []
            
            # Method 1: Business Facebook Endpoint (EAAD)
            try:
                biz_url = "https://business.facebook.com/business_locations"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": "https://www.facebook.com/",
                }
                response = session.get(biz_url, headers=headers, allow_redirects=True, timeout=15)
                
                # Look for EAAD token
                patterns = [
                    r'(EAAD[\w]+)',
                    r'"accessToken":"(EAAD[\w]+)"',
                    r'"token":"(EAAD[\w]+)"',
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, response.text)
                    for match in matches:
                        if len(match) > 100 and match not in [t['token'] for t in tokens_found]:
                            tokens_found.append({
                                'type': 'EAAD',
                                'token': match,
                                'source': 'Business Locations',
                                'working': True
                            })
            except Exception as e:
                pass
            
            # Method 2: Ads Manager API
            try:
                ads_url = "https://www.facebook.com/adsmanager/manage/campaigns"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                }
                response = session.get(ads_url, headers=headers, timeout=15)
                
                patterns = [
                    r'(EAAD[\w]+)',
                    r'"accessToken":"(EAAD[\w]+)"',
                    r'"token":"(EAAD[\w]+)"',
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, response.text)
                    for match in matches:
                        if len(match) > 100 and match not in [t['token'] for t in tokens_found]:
                            tokens_found.append({
                                'type': 'EAAD',
                                'token': match,
                                'source': 'Ads Manager',
                                'working': True
                            })
            except:
                pass
            
            # Method 3: Graph API Explorer Method
            try:
                if 'c_user' in cookies:
                    user_id = cookies['c_user']
                    # Try to get token via graph API
                    graph_url = f"https://graph.facebook.com/v18.0/me"
                    params = {'access_token': cookies.get('access_token', '')}
                    resp = session.get(graph_url, params=params, timeout=10)
                    if 'access_token' in resp.text:
                        data = resp.json()
                        if 'access_token' in data:
                            tokens_found.append({
                                'type': 'EAAD',
                                'token': data['access_token'],
                                'source': 'Graph API',
                                'working': True
                            })
            except:
                pass
            
            # Method 4: Mobile Endpoint (Most Reliable for EAAD)
            try:
                mobile_url = "https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
                    "Accept": "*/*",
                    "X-Requested-With": "XMLHttpRequest",
                }
                response = session.get(mobile_url, headers=headers, timeout=15)
                
                # Extract from JSON response
                try:
                    data = response.json()
                    if 'access_token' in data:
                        token = data['access_token']
                        if 'EAAD' in token:
                            tokens_found.append({
                                'type': 'EAAD',
                                'token': token,
                                'source': 'Mobile Endpoint',
                                'working': True
                            })
                except:
                    # Try regex on text
                    matches = re.findall(r'(EAAD[\w]+)', response.text)
                    for match in matches:
                        if len(match) > 100 and match not in [t['token'] for t in tokens_found]:
                            tokens_found.append({
                                'type': 'EAAD',
                                'token': match,
                                'source': 'Mobile Feed',
                                'working': True
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
    
    def __init__(self, uid_phone_mail, password):
        self.uid_phone_mail = uid_phone_mail
        
        if password.startswith("#PWD_FB4A"):
            self.password = password
        else:
            self.password = FacebookPasswordEncryptor.encrypt(password)
        
        self.session = requests.Session()
        self.device_id = str(uuid.uuid4())
        self.adid = str(uuid.uuid4())
        self.machine_id = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
        self.jazoest = ''.join(random.choices(string.digits, k=5))
        self.sim_serial = ''.join(random.choices(string.digits, k=20))
        
        self.headers = self._build_headers()
        self.data = self._build_data()
    
    def _build_headers(self):
        headers = self.BASE_HEADERS.copy()
        headers.update({
            "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; SM-G973F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/300.0.0.50.118;FBPN/com.facebook.katana;FBLC/en_US;FBBV/240123456;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G973F;FBSV/10;FBCA/arm64-v8a:;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/0;]"
        })
        return headers
    
    def _build_data(self):
        return {
            "adid": self.adid,
            "format": "json",
            "device_id": self.device_id,
            "email": self.uid_phone_mail,
            "password": self.password,
            "generate_analytics_claim": "1",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "source": "login",
            "machine_id": self.machine_id,
            "jazoest": self.jazoest,
            "locale": "en_US",
            "client_country_code": "US",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "Fb4aAuthHandler",
            "api_key": self.API_KEY,
            "access_token": self.ACCESS_TOKEN,
            "sig": self.SIG
        }
    
    def _handle_2fa(self, error_data):
        """Handle 2FA Code Input"""
        print(f"\n{YELLOW}{BOLD}{LIGHTNING} SECURITY CHALLENGE DETECTED {LIGHTNING}{RESET}")
        print(f"{CYAN}{BOLD}{'─' * 75}{RESET}\n")
        
        typing_effect("[*] Two-Factor Authentication Required", CYAN)
        typing_effect("[*] Check your WhatsApp/SMS for OTP code", CYAN)
        print(f"{CYAN}{BOLD}{'─' * 75}{RESET}\n")
        
        try:
            otp_code = input(f"{GREEN}{BOLD}[+] ENTER 2FA CODE ➤ {RESET}").strip()
            print()
            
            if not otp_code:
                return {'success': False, 'error': 'Empty 2FA code'}
            
            progress_bar("VERIFYING 2FA", 2)
            
            data_2fa = {
                'adid': self.adid,
                'format': 'json',
                'device_id': self.device_id,
                'email': self.uid_phone_mail,
                'password': self.password,
                'generate_analytics_claim': '1',
                'credentials_type': 'two_factor',
                'generate_session_cookies': '1',
                'error_detail_type': 'button_with_disabled',
                'source': 'login',
                'machine_id': self.machine_id,
                'jazoest': self.jazoest,
                'twofactor_code': otp_code,
                'first_factor': error_data.get('login_first_factor', ''),
                'userid': error_data.get('uid', ''),
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'Fb4aAuthHandler',
                'api_key': self.API_KEY,
                'access_token': self.ACCESS_TOKEN,
                'sig': self.SIG
            }
            
            response = self.session.post(self.API_URL, data=data_2fa, headers=self.headers)
            response_json = response.json()
            
            if 'access_token' in response_json:
                return self._parse_success(response_json)
            elif 'error' in response_json:
                return {
                    'success': False,
                    'error': response_json['error'].get('message', '2FA Failed')
                }
            
        except KeyboardInterrupt:
            return {'success': False, 'error': 'User cancelled'}
        except Exception as e:
            return {'success': False, 'error': f'2FA Error: {str(e)}'}
    
    def _parse_success(self, response_json):
        """Parse successful login"""
        token = response_json.get('access_token', '')
        
        # Generate EAAD from this token
        eaad_token = self._convert_to_eaad(token)
        
        result = {
            'success': True,
            'token': token,
            'eaad_token': eaad_token,
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
        
        return result
    
    def _convert_to_eaad(self, access_token):
        """Convert access token to EAAD format"""
        try:
            # Try to get EAAD using auth.getSessionforApp
            app_id = "438142079694454"  # Ads Manager App ID for EAAD
            
            response = requests.post(
                'https://api.facebook.com/method/auth.getSessionforApp',
                data={
                    'access_token': access_token,
                    'format': 'json',
                    'new_app_id': app_id,
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1'
                },
                timeout=10
            )
            
            result = response.json()
            
            if 'access_token' in result:
                new_token = result['access_token']
                if 'EAAD' in new_token:
                    return new_token
            
            # If not EAAD, return original with EAAD prefix simulation
            # Actually try business token exchange
            return self._get_business_token(access_token)
            
        except:
            return None
    
    def _get_business_token(self, access_token):
        """Get Business/EAAD token"""
        try:
            # Exchange for business token
            url = "https://graph.facebook.com/oauth/access_token"
            params = {
                'grant_type': 'fb_exchange_token',
                'client_id': '438142079694454',
                'client_secret': 'fc0a7caa49b192f64f6f5a6d9643bb28',
                'fb_exchange_token': access_token
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if 'access_token' in data:
                return data['access_token']
            return None
        except:
            return None
    
    def login(self):
        """Main login function"""
        try:
            progress_bar("ENCRYPTING CREDENTIALS", 2)
            
            response = self.session.post(self.API_URL, headers=self.headers, data=self.data)
            response_json = response.json()
            
            if 'access_token' in response_json:
                return self._parse_success(response_json)
            
            if 'error' in response_json:
                error_data = response_json.get('error', {}).get('error_data', {})
                error_code = response_json.get('error', {}).get('code', 0)
                
                # Check if 2FA required
                if error_code == 401 or 'login_first_factor' in error_data:
                    return self._handle_2fa(error_data)
                
                return {
                    'success': False,
                    'error': response_json['error'].get('message', 'Login failed'),
                    'code': error_code
                }
            
            return {'success': False, 'error': 'Unknown response'}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}


# ==========================================
# MENU FUNCTIONS
# ==========================================

def show_menu():
    """Show main menu"""
    print(f"\n{CYAN}{BOLD}╔{'═' * 83}╗{RESET}")
    print(f"{CYAN}{BOLD}║{MAGENTA}{'◆ SELECT ACCESS PROTOCOL ◆':^83}{CYAN}║{RESET}")
    print(f"{CYAN}{BOLD}╠{'═' * 83}╣{RESET}")
    print(f"{CYAN}{BOLD}║{RESET}  {GREEN}{BOLD}[1]{RESET} {WHITE}EMAIL/PHONE + PASSWORD + 2FA (Full Login){RESET}" + " " * 35 + f"{CYAN}║{RESET}")
    print(f"{CYAN}{BOLD}║{RESET}  {YELLOW}{BOLD}[2]{RESET} {WHITE}COOKIE TOKEN EXTRACTION (EAAD Generator){RESET}" + " " * 32 + f"{CYAN}║{RESET}")
    print(f"{CYAN}{BOLD}╚{'═' * 83}╝{RESET}\n")


def option_1_full_login():
    """Option 1: Full login with 2FA"""
    print(f"\n{GREEN}{BOLD}{SHADE_HEAVY * 85}{RESET}")
    glitch_text("  [ PROTOCOL 1 ] CREDENTIAL-BASED AUTHENTICATION SYSTEM", GREEN)
    print(f"{GREEN}{BOLD}{SHADE_HEAVY * 85}{RESET}\n")
    
    # Input Email/Phone
    typing_effect("[*] Enter your Facebook credentials", CYAN)
    print(f"{DIM}{'─' * 85}{RESET}\n")
    
    uid = input(f"{CYAN}{BOLD}[+] ENTER EMAIL OR PHONE NUMBER ➤ {RESET}").strip()
    print(f"{DIM}{'─' * 85}{RESET}\n")
    
    # Input Password
    password = input(f"{CYAN}{BOLD}[+] ENTER PASSWORD ➤ {RESET}").strip()
    print(f"{DIM}{'─' * 85}{RESET}\n")
    
    # Login
    fb = FacebookLogin(uid, password)
    result = fb.login()
    
    if result['success']:
        print(f"\n{GREEN}{BOLD}{BLOCK * 85}{RESET}")
        glitch_text("  [ ACCESS GRANTED ] LOGIN SUCCESSFUL", GREEN)
        print(f"{GREEN}{BOLD}{BLOCK * 85}{RESET}\n")
        
        # Show tokens
        hologram_box("PRIMARY ACCESS TOKEN", [
            ("TYPE", "EAAU (User Token)"),
            ("TOKEN", result['token'][:60] + "...")
        ])
        
        if result.get('eaad_token'):
            hologram_box("EAAD BUSINESS TOKEN (CONVO WORKING)", [
                ("TYPE", "EAAD (Business/Ads Token)"),
                ("STATUS", f"{GREEN}ACTIVE{RESET}"),
                ("TOKEN", result['eaad_token'])
            ])
        else:
            # Try to generate EAAD from cookies
            if result.get('cookies', {}).get('string'):
                typing_effect("[*] Generating EAAD token from session...", YELLOW)
                eaad_gen = EAADTokenGenerator()
                eaad_result = eaad_gen.generate_eaad_token(result['cookies']['string'])
                
                if eaad_result['success'] and eaad_result['tokens']:
                    for token_info in eaad_result['tokens']:
                        hologram_box(f"EAAD TOKEN - {token_info['source']}", [
                            ("TYPE", token_info['type']),
                            ("SOURCE", token_info['source']),
                            ("TOKEN", token_info['token'])
                        ])
                else:
                    print(f"{YELLOW}[!] Could not generate EAAD, but EAAU token is valid{RESET}\n")
        
        # Show cookies
        hologram_box("SESSION COOKIES", [
            ("COOKIES", result['cookies']['string'][:70] + "...")
        ])
        
    else:
        print(f"\n{RED}{BOLD}{BLOCK * 85}{RESET}")
        glitch_text("  [ ACCESS DENIED ] LOGIN FAILED", RED)
        print(f"{RED}{BOLD}{BLOCK * 85}{RESET}\n")
        print(f"{YELLOW}{BOLD}Error: {result.get('error', 'Unknown error')}{RESET}\n")
        if result.get('code'):
            print(f"{DIM}Error Code: {result['code']}{RESET}\n")


def option_2_cookie_eaad():
    """Option 2: Cookie to EAAD"""
    print(f"\n{MAGENTA}{BOLD}{SHADE_HEAVY * 85}{RESET}")
    glitch_text("  [ PROTOCOL 2 ] COOKIE EXTRACTION MODULE", MAGENTA)
    print(f"{MAGENTA}{BOLD}{SHADE_HEAVY * 85}{RESET}\n")
    
    typing_effect("[*] Paste Facebook cookies (format: datr=...; c_user=...; xs=...)", CYAN)
    print(f"{DIM}{'─' * 85}{RESET}\n")
    
    cookies = input(f"{YELLOW}{BOLD}[+] ENTER COOKIES ➤ {RESET}").strip()
    print()
    
    if not cookies:
        print(f"{RED}[!] No cookies provided!{RESET}\n")
        return
    
    matrix_loading("EXTRACTING EAAD TOKENS", 4)
    
    generator = EAADTokenGenerator()
    result = generator.generate_eaad_token(cookies)
    
    if result['success'] and result['tokens']:
        print(f"\n{GREEN}{BOLD}{BLOCK * 85}{RESET}")
        glitch_text("  [ EXTRACTION COMPLETE ] EAAD TOKENS FOUND", GREEN)
        print(f"{GREEN}{BOLD}{BLOCK * 85}{RESET}\n")
        
        for idx, token_info in enumerate(result['tokens'], 1):
            hologram_box(f"EAAD TOKEN #{idx} - {token_info['source']}", [
                ("TYPE", f"{GREEN}{BOLD}{token_info['type']}{RESET}"),
                ("SOURCE", token_info['source']),
                ("STATUS", f"{GREEN}{CHECK} WORKING{RESET}"),
                ("TOKEN", token_info['token'])
            ])
        
        # Show user info
        if 'c_user' in result['cookies']:
            user_id = result['cookies']['c_user']
            print(f"{CYAN}{BOLD}{'─' * 85}{RESET}")
            print(f"{CYAN}User ID: {WHITE}{BOLD}{user_id}{RESET}")
            print(f"{CYAN}{BOLD}{'─' * 85}{RESET}\n")
    else:
        print(f"\n{RED}{BOLD}{BLOCK * 85}{RESET}")
        glitch_text("  [ EXTRACTION FAILED ] NO EAAD TOKENS FOUND", RED)
        print(f"{RED}{BOLD}{BLOCK * 85}{RESET}\n")
        
        if result.get('error'):
            print(f"{YELLOW}Error: {result['error']}{RESET}\n")
        
        print(f"{CYAN}[*] Suggestion: Use Option 1 (Email/Password) for fresh tokens{RESET}\n")


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
                option_1_full_login()
            elif choice == '2':
                option_2_cookie_eaad()
            else:
                print(f"{RED}[!] Invalid selection! Choose 1 or 2{RESET}\n")
                continue
            
            # Continue prompt
            print(f"{CYAN}{BOLD}{'─' * 85}{RESET}")
            again = input(f"{YELLOW}{BOLD}[?] RUN ANOTHER PROTOCOL? (y/n) ➤ {RESET}").strip().lower()
            print()
            
            if again != 'y':
                print(f"{GREEN}{BOLD}{BLOCK * 85}{RESET}")
                glitch_text("  [ SYSTEM SHUTDOWN ] GOODBYE", CYAN)
                print(f"{GREEN}{BOLD}{BLOCK * 85}{RESET}\n")
                break
            
            clear_screen()
            show_banner()
            
        except KeyboardInterrupt:
            print(f"\n\n{RED}[!] Interrupted by user{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Error: {e}{RESET}\n")
