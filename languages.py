"""Languages in different datasets- with cv LC naming"""

CV_LANGUAGES: list[str] = [
    "ab",
    "ar",
    "as",
    "ast",
    "az",
    "ba",
    "bas",
    "be",
    "bg",
    "bn",
    "br",
    "ca",
    "ckb",
    "cnh",
    "cs",
    "cv",
    "cy",
    "da",
    "de",
    "dv",
    "dyu",
    "el",
    "en",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "fy-NL",
    "ga-IE",
    "gl",
    "gn",
    "ha",
    "hi",
    "hsb",
    "hu",
    "hy-AM",
    "ia",
    "id",
    "ig",
    "is",
    "it",
    "ja",
    "ka",
    "kab",
    "kk",
    "kmr",
    "ko",
    "ky",
    "lg",
    "lo",
    "lt",
    "lv",
    "mdf",
    "mhr",
    "mk",
    "ml",
    "mn",
    "mr",
    "mrj",
    "mt",
    "myv",
    "nan-tw",
    "ne-NP",
    "nl",
    "nn-NO",
    "oc",
    "or",
    "pa-IN",
    "pl",
    "pt",
    "quy",
    "rm-sursilv",
    "rm-vallader",
    "ro",
    "ru",
    "rw",
    "sah",
    "sat",
    "sc",
    "sk",
    "skr",
    "sl",
    "sr",
    "sv-SE",
    "sw",
    "ta",
    "th",
    "ti",
    "tig",
    "tk",
    "tok",
    "tr",
    "tt",
    "twi",
    "ug",
    "uk",
    "ur",
    "uz",
    "vi",
    "vot",
    "yo",
    "yue",
    "zh-CN",
    "zh-HK",
    "zh-TW",
]

WHISPER_LANGUAGES: list[str] = [
    "ar",
    "as",
    "az",
    "ba",
    "be",
    "bg",
    "bn",
    "br",
    "ca",
    "cv",
    "cy",
    "da",
    "de",
    "el",
    "en",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "gl",
    "ha",
    "hi",
    "hu",
    "hy-AM",
    "id",
    "is",
    "it",
    "ja",
    "ka",
    "kk",
    "ko",
    "lo",
    "lt",
    "lv",
    "mk",
    "ml",
    "mn",
    "mr",
    "mt",
    "ne-NP",
    "nl",
    "nn-NO",
    "oc",
    "pa-IN",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "sr",
    "sv-SE",
    "sw",
    "ta",
    "th",
    "tk",
    "tr",
    "tt",
    "uk",
    "ur",
    "uz",
    "vi",
    "yo",
    "zh-CN",
]

FLEURS_LANGUAGES: list[str] = [
    "ar",
    "as",
    "ast",
    "az",
    "be",
    "bg",
    "bn",
    "ca",
    "ckb",
    "cs",
    "cy",
    "da",
    "de",
    "el",
    "en",
    "es",
    "et",
    "fa",
    "fi",
    "fr",
    "ga-IE",
    "gl",
    "ha",
    "hi",
    "hu",
    "hy-AM",
    "id",
    "ig",
    "is",
    "it",
    "ja",
    "ka",
    "kk",
    "ko",
    "ky",
    "lg",
    "lo",
    "lt",
    "lv",
    "mk",
    "ml",
    "mn",
    "mr",
    "mt",
    "ne-NP",
    "nl",
    "oc",
    "or",
    "pa-IN",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "sr",
    "sv-SE",
    "sw",
    "ta",
    "th",
    "tr",
    "uk",
    "ur",
    "uz",
    "vi",
    "yo",
    "yue",
]

VOXPOPULI_LANGUAGES: list[str] = [
    "cs",
    "de",
    "en",
    "es",
    "et",
    "fi",
    "fr",
    "hu",
    "it",
    "lt",
    "nl",
    "pl",
    "ro",
    "sk",
    "sl",
]

# LANGUAGES WITH EXTERNAL TEST SET
LANGUAGES_ALLOWED: list[str] = sorted(list(set(VOXPOPULI_LANGUAGES + FLEURS_LANGUAGES)))
