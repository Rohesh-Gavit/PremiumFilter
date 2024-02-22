import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23898744'))
API_HASH = environ.get('API_HASH', '0b13c810c80b548604650cbe3c3db0c3')
BOT_TOKEN = environ.get('BOT_TOKEN', '6633984787:AAHB77PK04bmYBK1qskeIO-DSCWIEguqbl4')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False ))
PICS = (environ.get('PICS', 'https://telegra.ph/file/e02e42f8d74f542608227.jpg https://telegra.ph/file/e02e42f8d74f542608227.jpg https://graph.org/file/992c0f0bbb2421b00b03b.jpg https://graph.org/file/027f1b1a04b5d1d2d8570.jpg https://graph.org/file/58897113b411ebc9ba6ed.jpg https://graph.org/file/e631893dade5692d00f4a.jpg https://graph.org/file/2ea5956313f9d26ba4e24.jpg https://graph.org/file/cde23078b696aaf00487b.jpg  https://graph.org/file/6a76d821af95489a230bb.jpg https://graph.org/file/6f9d3dfa3b6873d047bed.jpg https://graph.org/file/04c5c87962ed4c8d456a2.jpg https://graph.org/file/bd8965942893832a66a65.jpg https://graph.org/file/57128f6d942c1313f51de.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5698613889').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001856938140').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Filmy:oiKn0AkUrgeBGDFq@rohidasgavit.pbz03z1.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL','-1001713712725' ))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '-1001792853580')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><a href='https://t.me/Filmy_Rohesh_Files'>{file_name}</a>

🔰 Join For Back-up
@Filmy_Rohesh
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬</b>

<i>ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ</i> 🚫")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "⚡<b>𝙁𝙄𝙇𝙀 𝙐𝙋𝙇𝙊𝘼𝘿𝙀𝘿 𝘽𝙔 [🌟 @𝙁𝙄𝙇𝙈𝙔_𝙍𝙊𝙃𝙀𝙎𝙃_𝙁𝙄𝙇𝙀𝙎™](https://t.me/Filmy_Rohesh_Files)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>𝙀𝙉𝙏𝙀𝙍𝙏𝘼𝙄𝙉𝙈𝙀𝙉𝙏 𝙆𝙀 𝙇𝙄𝙔𝙀 𝙅𝙊𝙄𝙉𝙀 𝙆𝘼𝙍𝙀 👁️‍🗨️ [⚜️𝙁𝙄𝙇𝙈𝙔 𝙍𝙊𝙃𝙀𝙎𝙃™⚜️](https://t.me/Filmy_Rohesh)</b> ↭  🔥")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
LINK_MODE = is_enabled("LINK_MODE", True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001998858242')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "CUSTOM_FILE_CAPTION Found, https://t.me/Filmy_Rohesh.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

HOW_TO_DOWNLOAD =  environ.get('HOW_TO_DOWNLOAD', 'https://t.me/Filmy_Rohesh')

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS','300'))

FILE_REQ_CHANNEL = int(environ.get('FILE_REQ_CHANNEL', LOG_CHANNEL))

SHORTNER_SITE =  environ.get('SHORTNER_SITE', '') #Put Only Shortner Site domain don't put like this https://tnlink.in/

SHORTNER_API =  environ.get('SHORTNER_API', '')

AUTO_DELETE =  environ.get('AUTO_DELETE', 'True')
