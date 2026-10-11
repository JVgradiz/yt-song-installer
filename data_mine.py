from main import Song, Thumbnail, Album

# This is my data.python file, that I use, do with this whatever you wish... Or not.

ARTISTS: dict[str, str] = {
        "MOTI": "Man on the Internet",
        "IVYCOMB": "Ivycomb",
        "STEPHANAFRO": "Stephanafro",
        "THAI_MCGRATH": "Thai McGrath",
        "STUPENDIUM": "The Stupendium",
        "MADAME_MACABRE": "Madame Macabre",
        "JIMMY_MAXIMUS": "Jimmy Maximus",
        "CG5": "CG5",
        "LYDIA_THE_BARD": "Lydia the Bard",
        "JUNO_SONGS": "JunoSongs",
        "TENEBRISMO": "Tenebrismo",
        "MUSICLIDE": "Musiclide",
        "JT_MUSIC": "JT Music",
        "LONGEST_SOLO_EVER": "LongestSoloEver",
        "OR3O": "OR3O",
        "PARANOID_DJ": "PARANOiD DJ",
        "CK9C": "CK9C",
        "SHARAX": "SharaX",
        "TRYHARDNINJA": "Tryhardninja",
        "YONKAGOR": "YonKaGor",
        "RECD": "RecD",
        "BLACK_GRYPHON": "Black Gryph0n",
        "THE_LIVING_TOMBSTONE": "The Living Tombstone",
        "ZSHARP": "Z Sharp Studio",
        "ALEX_ROCHON": "Alex Rochon",
        "CHALKEATERS": "The Chalkeaters",
        "SNUFFLES": "Snuffles",
        "VANE_LILY": "Vane Lily",
        "FRIZK": "Frizk",
        "OXYGEN": "oo Oxygen",
        "OODLEZZ": "OodleZz",
        "HEAVEN_PIERCE_HER": "Heaven Pierce Her",
        "KEYGEN_CHURCH": "KEYGEN CHURCH",
        "DM_DOKURO": "DM DOKURO",
        "OLD_MANS_POISON": "Old Man's Poison",
        "MOKA": "Moka",
}

def get_songs() -> list[Song]:
    return [
        Song("https://music.youtube.com/watch?v=j6acpg3IH6A", "Ship in a Bottle", "Fin Argus", "ship_in_a_bottle"),
        Song("https://music.youtube.com/watch?v=9U3yCs2GauQ", "Secure. Contain. Protect.", ARTISTS["MADAME_MACABRE"]),
        Song("https://music.youtube.com/watch?v=rcDruUTsXmg", "Dung Defender with Lyrics", [ARTISTS["MOTI"], "DarbyCupit"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 4),
        Song("https://music.youtube.com/watch?v=zSQSc3gf03k", "Jevil Anime Opening: Break The Cage", [ARTISTS["THAI_MCGRATH"]], "jevil_anime_opening"),
        Song("https://music.youtube.com/watch?v=WIBusox8PO0", "Brainiac Maniac", "NoteBlock", "brainiac_maniac_noteblock_remix", has_lyrics = False),
        Song("https://music.youtube.com/watch?v=tR87yzVQPho", "Apenas Ouro", ARTISTS["JIMMY_MAXIMUS"], "racoon_mix"),
        Song("https://music.youtube.com/watch?v=9bZILBqDuqw", "Ad Infinitum", ARTISTS["STUPENDIUM"], "ad_infinitum"),
        Song("https://music.youtube.com/watch?v=dxBkBjnbAMs", "Vs Marx with Lyrics", ARTISTS["MOTI"], "vs_marx_kirby_with_lyrics"),
        Song("https://music.youtube.com/watch?v=HSHrv3aX7ac", "Bad Time Trio with Lyrics", ["Bub8les", "Oddbrother", "The Aspen Collective", "Allevant"], "bad_time_trio_with_lyrics"),
        Song("https://music.youtube.com/watch?v=6GCjmcjMSPA", "Power of NEO with Lyrics", ARTISTS["MOTI"], "", Album.UNDERTALE_THE_MUSICAL, 2),
        Song("https://music.youtube.com/watch?v=Iucw1jgsmz0", "Chaos King with Lyrics", ARTISTS["MOTI"], "", Album.DELTARUNE_THE_NOT_MUSICAL, 2),
        Song("https://music.youtube.com/watch?v=p36FgvNaY3Q", "Hollow Knight Anime Opening", ARTISTS["THAI_MCGRATH"], "hollow_knight_anime_opening"),
        Song("https://music.youtube.com/watch?v=DEPXNxex1as", "Monkey's Paw", ["Brodingles", "Cami-Cat", "Nahu Oyrone"], "monkeys_paw"),
        Song("https://music.youtube.com/watch?v=wdwAPupz6EY", "The Court Jester", ["thquib", "FUKASE"], "the_court_jester"),
        Song("https://music.youtube.com/watch?v=Lyj-MZSAA9o", "Level ! Soundtrack REMASTERED", "Dapper Husky", "level!_ust", has_lyrics = False),
        Song("https://music.youtube.com/watch?v=HE78mcZHzfE", "Vs Susie with Lyrics", ARTISTS["MOTI"], "", Album.DELTARUNE_THE_NOT_MUSICAL, 7),
        Song("https://music.youtube.com/watch?v=Y21UNUo7Wn8", "Battle Against a True Hero - Orchestra Remix with Lyrics", "xUnreachablee"),
        Song("https://music.youtube.com/watch?v=CENW2YMprZE", "Push", ARTISTS["CG5"], "push_cg5"),
        # Song("https://music.youtube.com/watch?v=95lRa2Ls2sU", "Push", ARTISTS["CG5"], "push_cg5"), Unlisted
        Song("https://music.youtube.com/watch?v=5HksWwytHq8", "How Far I'll Go - Villain Song Version", ARTISTS["LYDIA_THE_BARD"], "how_far_ill_go_villain_song"),
        Song("https://music.youtube.com/watch?v=JN2CMWSckoo", "NOW'S YOUR CHANCE TO BE A [[LYRICS INCLUDED]]", [ARTISTS["MOTI"], ARTISTS["JUNO_SONGS"], ARTISTS["TENEBRISMO"]], "", Album.DELTARUNE_THE_NOT_MUSICAL, 15, file_name = "nows_your_chance_to_be_a_with_lyrics_junosongs"),
        Song("https://music.youtube.com/watch?v=ZPyWn8gCQR4", "Battle Against a True Hero with Lyrics", ARTISTS["MOTI"], "", Album.UNDERTALE_GENOCIDE_PACKAGE, 4, begin_cut = (3*60+4)*1000+100, end_cut = (2*60+9)*1000+500),
        Song("https://music.youtube.com/watch?v=wE-vn1cu69I", "Broken Machine", ARTISTS["MUSICLIDE"], "broken_machine"),
        Song("https://music.youtube.com/watch?v=6az6uoq2sV4", "Attack of the Killer Queen", [ARTISTS["MOTI"], "LuluGreySings"], "", Album.DELTARUNE_THE_NOT_MUSICAL, 21),
        Song("https://music.youtube.com/watch?v=iWxGwJy7Jv4", "Monster", "KIRA"),
        Song("https://music.youtube.com/watch?v=D0fovk4PLgE", "BATTLE AGAINST THE WORLD - Deltarune Chaper Rewriten REMIX", "RAMIYORU"),
        Song("https://music.youtube.com/watch?v=KYdKDGq_1Cw", "BIG SHOT [[LYRICAL COVER]]", [ARTISTS["MOTI"], ARTISTS["JUNO_SONGS"], ARTISTS["TENEBRISMO"]], "", Album.DELTARUNE_THE_NOT_MUSICAL, 20, file_name = "big_shot_with_lyrics_junosongs"),
        Song("https://music.youtube.com/watch?v=j7_58XXOulY", "We Don't Talk About Bruno - Villain Song Version", ARTISTS["LYDIA_THE_BARD"], "we_dont_talk_about_bruno_villain_song"),
        Song("https://music.youtube.com/watch?v=ge8fKFKiRZI", "To The Bone", ARTISTS["JT_MUSIC"], "to_the_bone"),
        Song("https://music.youtube.com/watch?v=w0jcR3l3wL8", "Knives, Gears and Wires", [ARTISTS["MUSICLIDE"], "Swiblet"], "knives_gears_and_wires"),
        Song("https://music.youtube.com/watch?v=5_J3pPAv1Mc", "The Show That Never Ends", [ARTISTS["LONGEST_SOLO_EVER"], ARTISTS["OR3O"]], "the_show_that_never_ends"),
        Song("https://music.youtube.com/watch?v=rATbtwj1qls", "Just Look My Way", ARTISTS["PARANOID_DJ"], "just_look_my_way"),
        Song("https://music.youtube.com/watch?v=lA2O3t7Usac", "Code Red", ARTISTS["LONGEST_SOLO_EVER"], "code_red_lse"),
        Song("https://music.youtube.com/watch?v=yc3xuaA44YY", "Death's Doorstep", [ARTISTS["MUSICLIDE"], "Tohru"], "deaths_doorstep"),
        Song("https://music.youtube.com/watch?v=Zx1vDGKyX5E", "Your Contract Has Expired with Lyrics", ARTISTS["MOTI"], "a_hat_in_time_musical_bytes_album"),
        Song("https://music.youtube.com/watch?v=cb3XdH78Jb4", "Megalovania with Lyrics", ARTISTS["MOTI"], "", Album.UNDERTALE_GENOCIDE_PACKAGE, 9),
        Song("https://music.youtube.com/watch?v=fhS83VEUB5Y", "To The King", "TyKim"),
        Song("https://music.youtube.com/watch?v=nbUZM5owBAs", "Truth, Beaulty, and Hatred with Lyrics", [ARTISTS["MOTI"], "Caarl", "Jax Tharp"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 5+1),
        Song("https://music.youtube.com/watch?v=lnwio1GQ4po", "Snowgrave NEO with Lyrics", ARTISTS["JUNO_SONGS"]),
        Song("https://music.youtube.com/watch?v=lnwio1GQ4po", "Spamton GIGA with Lyrics", ARTISTS["JUNO_SONGS"]),
        Song("https://music.youtube.com/watch?v=qI_7TmjgC_o", "Grimm with Lyrics", ARTISTS["MOTI"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 7+1),
        Song("https://music.youtube.com/watch?v=TxODdJvMCOE", "Faker & Black Sun with Lyrics", "Churgney Gurgney"),
        Song("https://music.youtube.com/watch?v=ResmeNVHOKQ", "This World of Mine", ARTISTS["MUSICLIDE"], "this_world_of_mine"),
        Song("https://music.youtube.com/watch?v=CLW3FnDa1nQ", "Welcome to The Internet", "Bo Burnham", "inside_album"),
        Song("https://music.youtube.com/watch?v=LJbqYbi9mTA", "Quebre Minha Mente", ARTISTS["JIMMY_MAXIMUS"], "racoon_mix"),
        Song("https://music.youtube.com/watch?v=vQBI9y_bAjU", "Empires", "The Electric Swing Circus", "empires"),
        Song("https://music.youtube.com/watch?v=ImKVnZm_yz4", "Megalovania Piano Cover", "djsmell"),
        Song("https://music.youtube.com/watch?v=7ogpb6rc65E", "Sealed Vessel with Lyrics", [ARTISTS["MOTI"], "Stelyost"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 10),
        Song("https://music.youtube.com/watch?v=jqILrG1vs4k", "Manual Blast with Lyrics", "SayoSkyy"),
        Song("https://music.youtube.com/watch?v=K7eG37qiP-g", "Hypnosis", ARTISTS["LONGEST_SOLO_EVER"], "hypnosis_lse"),
        Song("https://music.youtube.com/watch?v=6Ehi4892HrY", "NOW'S YOUR CHANCE TO BE A GOMOTION REMIX", "gomotion"),
        Song("https://music.youtube.com/watch?v=jLopU2IsrUY", "You Can't hide", [ARTISTS["CK9C"], "Elizabeth Ann"], "you_cant_hide"),
        Song("https://music.youtube.com/watch?v=jPvfmGKBWIE", "Dark Darker Yet Darker", ARTISTS["SHARAX"]),
        Song("https://music.youtube.com/watch?v=6CcrarWJZrU", "Apocalypse CURIE with Lyrics", ARTISTS["JUNO_SONGS"]),
        Song("https://music.youtube.com/watch?v=059BLyrMDvg", "The World Revolving with Lyrics", ARTISTS["MOTI"], "", Album.DELTARUNE_THE_NOT_MUSICAL, 9),
        Song("https://music.youtube.com/watch?v=mQFokUq9LYs", "Echo", "Crusher-P"),
        Song("https://music.youtube.com/watch?v=hVRNjTy8Uuk", "Broken Vessel with Lyrics", [ARTISTS["MOTI"], "Tom Previte", "Ploops", "Emily Go"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 4+1),
        Song("https://music.youtube.com/watch?v=s0KWCdNoqvY", "No Exit", ARTISTS["LONGEST_SOLO_EVER"], "no_exit_lse"),
        Song("https://music.youtube.com/watch?v=mEXZGBR6zd4", "Hornet with Lyrics", [ARTISTS["MOTI"], "Emily Go"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 2),
        Song("https://music.youtube.com/watch?v=7PA38zRrPRM", "Judgement", ARTISTS["TRYHARDNINJA"], "judgement_tryhardninja"),
        Song("https://music.youtube.com/watch?v=oub98zjmQKQ", "Circus Hop", ARTISTS["YONKAGOR"], "circus_hop"),
        Song("https://music.youtube.com/watch?v=h-2LRO8sGCI", "Pillar John's Revenge with Lyrics", ARTISTS["RECD"]),
        Song("https://music.youtube.com/watch?v=trhOkSS-ylg", "ANTIHUMAN", ARTISTS["IVYCOMB"], "antihuman_ivycomb"),
        Song("https://music.youtube.com/watch?v=-og6NEppvrg", "NOTORIOUS", ARTISTS["IVYCOMB"], "notorious_ivycomb"),
        Song("https://music.youtube.com/watch?v=xP4QIuKbwRg", "Too Slow (D-Sides) with Lyrics", ARTISTS["JUNO_SONGS"]),
        Song("https://music.youtube.com/watch?v=0RR4hIhnNzs", "Boogieman with Lyrics", ARTISTS["JUNO_SONGS"]),
        Song("https://music.youtube.com/watch?v=gFOJkIk8fcs", "Insane", [ARTISTS["BLACK_GRYPHON"], "Baasik"], "insane_hazbin_hotel"),
        Song("https://music.youtube.com/watch?v=MURua52_YPg", "My Ordinary Life", ARTISTS["THE_LIVING_TOMBSTONE"], "my_ordinary_life"),
        Song("https://music.youtube.com/watch?v=2UmbRrc-Zd4", "A Million Gruesome Ways To Die", ["Billie Bust Up", ARTISTS["BLACK_GRYPHON"]], "a_million_gruesome_ways_to_die"),
        Song("https://music.youtube.com/watch?v=5Z56MZFMp0k", "Discord", [ARTISTS["THE_LIVING_TOMBSTONE"], "Eurobeat Brony"], "discord_the_living_tombstone"),
        Song("https://music.youtube.com/watch?v=BWhEry67iC0", "Keter Qualities", [ARTISTS["MUSICLIDE"], ARTISTS["STUPENDIUM"], "ZaBlackRose"], "keter_qualities"),
        Song("https://music.youtube.com/watch?v=Diob2vPNHec", "Overthrone", ARTISTS["LONGEST_SOLO_EVER"], "overthrone_lse"),
        Song("https://music.youtube.com/watch?v=IIV3uJoRtro", "HEAVEN SAYS (MANDELA MIX)", ARTISTS["ZSHARP"]),
        Song("https://music.youtube.com/watch?v=hzbKpvoFgQU", "Bury My Mother Pale and Slight", "Amalgemotion"),
        Song("https://music.youtube.com/watch?v=WopMFtLen_Y", "Sweet Little Lies - Ivycomb Remix", [ARTISTS["IVYCOMB"], "Shwabadi"], "sweet_little_lies_ivycomb"),
        Song("https://music.youtube.com/watch?v=6L8gr_e-nSI", "You'll Be Gone", ARTISTS["YONKAGOR"], "youll_be_gone"),
        Song("https://music.youtube.com/watch?v=04U4CjoS7jQ", "Want Some Fun", [ARTISTS["MUSICLIDE"], ARTISTS["ALEX_ROCHON"], "Tohru", "Skitzy"], "want_some_fun"),
        Song("https://music.youtube.com/watch?v=HX9HGP7xpY4", "You're Just Like Pop Music", ARTISTS["YONKAGOR"], "youre_just_like_pop_music"),
        Song("https://music.youtube.com/watch?v=piVJp1Ijuqo", "Luminescence", ARTISTS["IVYCOMB"], "luminescence_ivycomb"),
        Song("https://music.youtube.com/watch?v=PtMcTjAoKBs", "Sleepwalk", "Forest Day", "sleepwalk"),
        Song("https://music.youtube.com/watch?v=fQ3-CyvLkpc", "Stayed Gone", ["Andrew Underberg", "Sam Haft", "Christian Borle", "Amir Talai", "Joel Perez"], "hazbin_hotel_ost_s1"),
        Song("https://music.youtube.com/watch?v=1gQ4Xlr9Ye8", "Blue Bird", [ARTISTS["IVYCOMB"], ARTISTS["MOKA"], ARTISTS["YONKAGOR"]], "blue_bird_ivycomb"),
        Song("https://music.youtube.com/watch?v=wD9yuHkAxxk", "SLUGCAT PINBALL", ARTISTS["IVYCOMB"], "slugcat_pinball"),
        Song("https://music.youtube.com/watch?v=txeHnnCj9Ow", "Fratricide", [ARTISTS["IVYCOMB"], ARTISTS["MOKA"]], "fratricide_ivycomb"),
        Song("https://music.youtube.com/watch?v=YMq-AhRfG9A", "System Error", [ARTISTS["IVYCOMB"], ARTISTS["MOKA"]], "system_error_ivycomb"),
        Song("https://music.youtube.com/watch?v=c5fYDG4HN5c", "Echo - W.D. Gaster", "Punished GSM"),
        Song("https://music.youtube.com/watch?v=8o5CRs0n--U", "Spider Bites", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "spider_bites_ivycomb"),
        Song("https://music.youtube.com/watch?v=5rrxIdkRcDk", "SAHARA", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "sahara_ivycomb"),
        Song("https://music.youtube.com/watch?v=w4vECnueTP4", "LOVESICK", ARTISTS["IVYCOMB"], "lovesick_ivycomb"),
        Song("https://music.youtube.com/watch?v=8BRJgExKCtM", "Cannon Ball with Lyrics", [ARTISTS["MOTI"], "Alex Beckham"]),
        Song("https://music.youtube.com/watch?v=wGz_h1Qrt5g", "In The Mirror", "justan oval", "in_the_mirror"),
        Song("https://music.youtube.com/watch?v=aJtQYbn-ks8", "Golden Land (V2)", "FriedFrick", "musical_masquerave", has_lyrics = False),
        Song("https://music.youtube.com/watch?v=wNti1Z3im-E", "No Eternity", ARTISTS["IVYCOMB"], "no_eternity_ivycomb"),
        Song("https://music.youtube.com/watch?v=FI2D5-5Rg6E", "Everlasting Fun", ARTISTS["LONGEST_SOLO_EVER"], "everlasting_fun"),
        Song("https://music.youtube.com/watch?v=_KAXvMB4434", "TOKYO", ARTISTS["IVYCOMB"], "tokyo_ivycomb"),
        Song("https://music.youtube.com/watch?v=acdxrueuYys", "Open The Door", [ARTISTS["LONGEST_SOLO_EVER"], "DayumDahlia"], "open_the_door_lse"),
        Song("https://music.youtube.com/watch?v=iRZnnh3WyW4", "Wool Over Our Eyes", ARTISTS["STUPENDIUM"], "wool_over_our_eyes"),
        Song("https://music.youtube.com/watch?v=zj0HgKOTGrY", "ANTIVILLAIN", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "antivillain"),
        Song("https://music.youtube.com/watch?v=4YSVyA_CgKA", "Furrýmon: Gotta Smash 'Em All!", [ARTISTS["CHALKEATERS"], ARTISTS["BLACK_GRYPHON"], "PiNKII"] ,"furrýmon"),
        Song("https://music.youtube.com/watch?v=RjTu6hfccl0", "Fighting Insanity", ARTISTS["MUSICLIDE"], "fighting_insanity"),
        Song("https://music.youtube.com/watch?v=6aoCakMvlcM", "Best Friend", ARTISTS["OR3O"], "best_friends_or3o"),
        Song("https://music.youtube.com/watch?v=4VsfEt03VJk", "Memory Merge", ARTISTS["YONKAGOR"], "memory_merge"),
        Song("https://music.youtube.com/watch?v=Y6uiP27zKi0", "SPOTS", ARTISTS["SNUFFLES"], "spots_snuffles"),
        Song("https://music.youtube.com/watch?v=QbEYRi4lCmc", "Won't Go", ARTISTS["SNUFFLES"], "wont_go_snuffles"),
        Song("https://music.youtube.com/watch?v=ki9Jo4trgtA", "Ready or Not?", ARTISTS["SNUFFLES"], "ready_or_not_snuffles"),
        Song("https://music.youtube.com/watch?v=tw5ZsxDSrbI", "Keep on With It", ARTISTS["SNUFFLES"], "keep_on_with_it_snuffles"),
        Song("https://music.youtube.com/watch?v=ezhdzPEG3DQ", "Too Late 2", ARTISTS["SNUFFLES"], "too_late_2_snuffles"),
        Song("https://music.youtube.com/watch?v=0xmakTOaFZk", "Fall End Sea", ARTISTS["SNUFFLES"], "forgive_me_please_snuffles_album", Album.FORGIVE_ME_PLEASE, 1),
        Song("https://music.youtube.com/watch?v=Emk19my67GM", "Just a Little Better", ARTISTS["SNUFFLES"], "forgive_me_please_snuffles_album", Album.FORGIVE_ME_PLEASE, 2),
        Song("https://music.youtube.com/watch?v=IlNl59TIdCg", "But Here I Am", ARTISTS["SNUFFLES"], "forgive_me_please_snuffles_album", Album.FORGIVE_ME_PLEASE, 3),
        Song("https://music.youtube.com/watch?v=xp2SzlnzbkA", "Seven Run", ARTISTS["SNUFFLES"], "seven_run_snuffles"),
        Song("https://music.youtube.com/watch?v=dtVI47rE8JU", "Smile Like You Mean It", ARTISTS["PARANOID_DJ"], "smile_like_you_mean_it"),
        Song("https://music.youtube.com/watch?v=-sM9ocXMHk4", "DATA_REJECT", ARTISTS["IVYCOMB"], "data_reject_ivycomb"),
        Song("https://music.youtube.com/watch?v=22ZjX8MmYxA", "LDR", ARTISTS["IVYCOMB"], "ldr_ivycomb"),
        Song("https://music.youtube.com/watch?v=M5mIYZbYL_4", "BUTHER VANITY", ARTISTS["VANE_LILY"], "buther_vanity"),
        Song("https://music.youtube.com/watch?v=0dUCeqJ14RY", "TOKYO ANNIVERSARY", [ARTISTS["IVYCOMB"], "MRSHLMusic"], "tokyo_aniversary_ivycomb"),
        Song("https://music.youtube.com/watch?v=7jq9c4uyOL4", "I Forgot That You Exist", ARTISTS["YONKAGOR"], "i_forgot_that_you_exist"),
        Song("https://music.youtube.com/watch?v=tjXACkFQnSo", "Forgotten", ARTISTS["IVYCOMB"], "forgotten_ivycomb"),
        Song("https://music.youtube.com/watch?v=r8z8EnpifFY", "Fourth Wall with Lyrics", "MaimyMayo"),
        Song("https://music.youtube.com/watch?v=RtH3seTek58", "CYBERNETIC HEART", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "cybernetic_heart_ivycomb"),
        Song("https://music.youtube.com/watch?v=LglXzrkNub8", "This Thought", [ARTISTS["SNUFFLES"], ARTISTS["FRIZK"]], "this_thought_snuffles"),
        Song("https://music.youtube.com/watch?v=pIcMXpeeLKU", "Let's Get Weird", ARTISTS["LONGEST_SOLO_EVER"], "lets_get_weird_lse"),
        Song("https://music.youtube.com/watch?v=HDxd7GyReYw", "World of Everything", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "world_of_everything_ivycomb"),
        Song("https://music.youtube.com/watch?v=Q43lsU6Xf_0", "Want Some Fun Remastered", [ARTISTS["MUSICLIDE"], ARTISTS["ALEX_ROCHON"], "Tohru", "Skitzy", ARTISTS["OXYGEN"]], "want_some_fun_remastered"),
    	Song("https://music.youtube.com/watch?v=PCcl_c_9GAY", "Digital Land", "Kyle Allen Music", "digital_land"),
    	Song("https://music.youtube.com/watch?v=ypxtbI-NWg4", "FNAF Kids", [ARTISTS["BLACK_GRYPHON"], "DHeusta", ARTISTS["OR3O"], ARTISTS["STUPENDIUM"]], "fnaf_kids"),
    	Song("https://music.youtube.com/watch?v=XSLFuWdQ-SA", "MAKE BELIEVE", ARTISTS["IVYCOMB"], "make_believe_ivycomb"),
    	Song("https://music.youtube.com/watch?v=4FZraJ6qfPs", "The Most Chaotic World Cover", "Kittblush"),
    	Song("https://music.youtube.com/watch?v=CDITKwzQauc", "I don't wanna", ARTISTS["SNUFFLES"], "i_dont_wanna_snuffles"),
    	Song("https://music.youtube.com/watch?v=A3hkYIuRVWo", "Vines", "Shadrow", "vines"),
    	Song("https://music.youtube.com/watch?v=ZOflZ0lKPF0", "In The Light", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "in_the_light"),
    	Song("https://music.youtube.com/watch?v=8mdb34cq7fk", "Y2K", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "y2k", Album.RAISED_BY_ALIENS, 1),
    	Song("https://music.youtube.com/watch?v=nO3b-6eQ9Hg", "Noise Simulator 2002 (Song 2)", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 2),
    	Song("https://music.youtube.com/watch?v=Rk8DvGikIbc", "Take the Crown", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 3),
    	Song("https://music.youtube.com/watch?v=YfAAmai7_yg", "Shadow in the Dark", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 4),
    	Song("https://music.youtube.com/watch?v=qGS9gM-XdEM", "Penny Pinched", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 5),
    	Song("https://music.youtube.com/watch?v=LzsUFAeb_8k", "Vancouver", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 6),
    	Song("https://music.youtube.com/watch?v=cQ_tsftdOmE", "End of the World", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 7),
    	Song("https://music.youtube.com/watch?v=BdBV6PvgwO8", "Raised by Aliens", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 8),
    	Song("https://music.youtube.com/watch?v=z_Nqq8V-LqM", "Free", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 9),
    	Song("https://music.youtube.com/watch?v=89v2Kartybg", "Terminal 18", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 10),
    	Song("https://music.youtube.com/watch?v=lBkamN65Fa8", "Strays", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 11),
    	Song("https://music.youtube.com/watch?v=rbqxcqhrcmI", "Kid Again", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 12),
    	Song("https://music.youtube.com/watch?v=eFm-WbBXguU", "Rubicon", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "raised_by_aliens_album", Album.RAISED_BY_ALIENS, 12),
    	Song("https://music.youtube.com/watch?v=fXjCvKYVp9U", "Linger in the Rain", ARTISTS["YONKAGOR"], "linger_in_the_rain"),
    	Song("https://music.youtube.com/watch?v=bMwcoK1Tw1g", "Come Back To Me", [ARTISTS["LONGEST_SOLO_EVER"], "HalaCG", "Breeton Boi"], "come_back_to_me_shadow"),
    	Song("https://music.youtube.com/watch?v=DZn3hNS286s", "HYPNOFREAK", ARTISTS["IVYCOMB"], "hypnofreak_ivycomb"),
        Song("https://music.youtube.com/watch?v=SATG3rxX1NE", "Shadow Wick: Murderholics", [ARTISTS["CHALKEATERS"], "Caleb Hyles"], "shadow_wick"),
    	Song("https://music.youtube.com/watch?v=hqErigwP78Y", "Nine Sols", "珂拉琪", "nine_sols_ost"),
    	Song("https://music.youtube.com/watch?v=D26OsQXqi-8", "Sun Spots", ARTISTS["IVYCOMB"], "sun_spots_ivycomb", Album.REBIRTH, 6),
    	Song("https://music.youtube.com/watch?v=MxKSoLRNtqk", "All-Stars with Lyrics", ARTISTS["JUNO_SONGS"], begin_cut = 105300),
    	Song("https://music.youtube.com/watch?v=ehnLkHR05Ao", "Wear the Mask", ARTISTS["LONGEST_SOLO_EVER"], "wear_the_mask_lse"),
    	Song("https://music.youtube.com/watch?v=Hq14Fy4uscw", "Burning Souls", "NyxTheShield", "burning_souls"),
    	Song("https://music.youtube.com/watch?v=y6KOV_SMbjE", "Neverland", ARTISTS["IVYCOMB"], "neverland_ivycomb", Album.REBIRTH, 8),
    	Song("https://music.youtube.com/watch?v=x4eVHZCx0N4", "INFAMOUS", [ARTISTS["IVYCOMB"], ARTISTS["YONKAGOR"], ARTISTS["STEPHANAFRO"]], "infamous_ivycomb"),
        Song("https://music.youtube.com/watch?v=iOhRsJYwqgg", "Broken Machine: The Pancake Mix", ARTISTS["MUSICLIDE"], "broken_machine_pancake_mix"),
    	Song("https://music.youtube.com/watch?v=wZzT1lzfjp0", "Hive Knight with Lyrics", ARTISTS["MOTI"], "hollow_knight_musical_bytes_album", Album.HOLLOW_KNIGHT_MUSICAL, 9),
    	Song("https://music.youtube.com/watch?v=K5gYGMg_ZUc", "THE RINGMASTER", [ARTISTS["IVYCOMB"], ARTISTS["OODLEZZ"]], "the_ringmaster"),
    	Song("https://music.youtube.com/watch?v=xF_gHb4_K98", "CTRW+ALT+DESTROY", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 1),
    	Song("https://music.youtube.com/watch?v=O64o8e7DlEw", "Get Rowdy!", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 2),
    	Song("https://music.youtube.com/watch?v=bW2ZsxhHZfo", "Conflux of Choices", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 3),
    	Song("https://music.youtube.com/watch?v=sZvwqOKNxZ0", "Gospel for Triumph", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 4),
    	Song("https://music.youtube.com/watch?v=MrvU-T3KiaE", "Smile's a Sympton", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 5),
    	Song("https://music.youtube.com/watch?v=EWGumcrQ8JY", "Watch Me Fade", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 7),
    	Song("https://music.youtube.com/watch?v=mHla7S8vHEw", "Rebirth", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 9),
    	Song("https://music.youtube.com/watch?v=De_xIZocGhM", "Synergy", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 10),
    	Song("https://music.youtube.com/watch?v=us6pP5TSm-c", "Where it Hurts", ARTISTS["IVYCOMB"], "rebirth_album", Album.REBIRTH, 11),
    	Song("https://music.youtube.com/watch?v=vkubg_0xKUw", "Collared", ARTISTS["VANE_LILY"], "collared"),
    	Song("https://music.youtube.com/watch?v=nWJ1PcSt73E", "The House Always Wins (2023 Remaster)", ARTISTS["STUPENDIUM"], "the_house_aways_wins_remastered"),
    	Song("https://music.youtube.com/watch?v=tdlq_dDtSqw", "The Data Stream", [ARTISTS["STUPENDIUM"], "Cami-Cat"], "the_data_stream"),
    	Song("https://music.youtube.com/watch?v=kBmYt2eNc9I", "The Merry-Go-Round", ARTISTS["STUPENDIUM"], "the_merry_go_round"),
    	Song("https://music.youtube.com/watch?v=YzxwZCY5gUM", "HEAT", ARTISTS["IVYCOMB"], "heat_ivycomb"),
    	Song("https://music.youtube.com/watch?v=xaIPn8uRMBo", "SPOTS 2", ARTISTS["SNUFFLES"], "spots2_snuffles"),
    	Song("https://music.youtube.com/watch?v=IZzgzR1iqYY", "Love Letter", ARTISTS["IVYCOMB"], "love_letter_ivycomb"),
    	Song("https://music.youtube.com/watch?v=GFHeMRAAdtY", "If I Were to Die", ARTISTS["YONKAGOR"], "if_i_were_to_die"),
    	Song("https://music.youtube.com/watch?v=ADYIrhz0c_A", "I cant stop making mistakes", ARTISTS["SNUFFLES"], "i_cant_stop_making_mistakes_snuffles"),
    	Song("https://music.youtube.com/watch?v=BYlWUISY4oM", "Off The Air", [ARTISTS["MUSICLIDE"], ARTISTS["ALEX_ROCHON"], "Finn M-K", "Tohru"], "off_the_air"),
    	Song("https://music.youtube.com/watch?v=YO1dLoYu3PQ", "Fight Til I'm Good Enough", [ARTISTS["THE_LIVING_TOMBSTONE"]], "fight_til_im_good_enough"),
    	Song("https://music.youtube.com/watch?v=U5SjlUnsPZI", "Crimson Galaxies", ARTISTS["IVYCOMB"], "crimson_galaxies"),
    	Song("https://music.youtube.com/watch?v=j9X-8cli1HM", "LAB RAT", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "lab_rat_ivycomb"),
    	Song("https://music.youtube.com/watch?v=0zPpqBDDmbI", "I Still Create", ARTISTS["YONKAGOR"], "i_still_create"),
    	Song("https://music.youtube.com/watch?v=ofIUk7Jzt24", "OUTER SKIES", ARTISTS["IVYCOMB"], "outer_skies_ivycomb"),
    	Song("https://music.youtube.com/watch?v=yJtFKuZoRvg", "Nirvana", ARTISTS["IVYCOMB"], "nirvana_ivycomb"),
    	Song("https://music.youtube.com/watch?v=yrP9VPW0cdo", "So Long", ARTISTS["YONKAGOR"], "so_long"),
    	Song("https://music.youtube.com/watch?v=zr8L899Pg5E", "Cut The Ties", [ARTISTS["JT_MUSIC"], "Andrea Storm Kaden"], "cut_the_ties"),
    	Song("https://music.youtube.com/watch?v=m30ad1EoTVk", "Like a Ghost", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "like_a_ghost"),
    	Song("https://music.youtube.com/watch?v=TojwRLDLL_s", "I Never Feel Alone", [ARTISTS["FRIZK"], ARTISTS["SNUFFLES"]], "i_never_feel_alone_snuffles"),
    	Song("https://music.youtube.com/watch?v=PhvIBk1vW2s", "HOMESICK WANDERLUST", ARTISTS["IVYCOMB"], "homesick_wanderlust"),
    	Song("https://music.youtube.com/watch?v=M3_EAHBRklo", "Down Down Down", [ARTISTS["IVYCOMB"], ARTISTS["OODLEZZ"]], "down_down_down"),
    	Song("https://music.youtube.com/watch?v=AmQZ6ehcfUk", "2MUCH2BEAR", "RedTv53", "2much2bear2", end_cut = 3700),
        Song("https://music.youtube.com/watch?v=eHrGUQnz9eQ", "Cats In Pink", ["Studi01", "CrescentIsCat"], "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 1),
        Song("https://music.youtube.com/watch?v=3bYTIOOdT4A", "Taste of Summer", "Kennyoung", "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 2),
        Song("https://music.youtube.com/watch?v=D7CDftygn1A", "Angel Wings", ARTISTS["IVYCOMB"], "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 3),
        Song("https://music.youtube.com/watch?v=dndYOxmR6bk", "I've Lost Myself", "Frizk", "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 4),
        Song("https://music.youtube.com/watch?v=0NmJFpjAMIc", "Our Season", ARTISTS["YONKAGOR"], "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 5),
        Song("https://music.youtube.com/watch?v=CvO0Ppgz9LE", "Lose", ARTISTS["SNUFFLES"], "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 6),
        Song("https://music.youtube.com/watch?v=eJ_QEjIQ-0E", "Driving Into Starlight", "YamikaDesu", "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 7),
        Song("https://music.youtube.com/watch?v=vexj6f_Svq4", "Constelación", "WHSPRS", "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 8),
        Song("https://music.youtube.com/watch?v=wZGTNKvb1ZM", "Summer's End", "Arctica The Fox", "our_summer_dreams_album", Album.OUR_SUMMER_DREAMS, 9),
        Song("https://music.youtube.com/watch?v=9E0xFvFCUTM", "Order", ARTISTS["HEAVEN_PIERCE_HER"], "order_ultrakill_ost", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=eeMC0SG2cnA", "Tenebre Rosso Sangue", ARTISTS["KEYGEN_CHURCH"], "keygen_church_ultrakill", Album.ULTRAKILL_OST, 2, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=TWS07eY1ElU", "War", ARTISTS["HEAVEN_PIERCE_HER"], "war_ultrakill_ost", Album.ULTRAKILL_OST, 3, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=uYBO_Sk5YiE", "The Tale of a Cruel World", ARTISTS["DM_DOKURO"], "terraria_calamity_ost", Album.THE_TALE_OF_A_CRUEL_WORLD_CALAMITY_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=0k1lQM-0_j0", "The World Looks White", ARTISTS["HEAVEN_PIERCE_HER"], "ultrakill_ost_violence", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=In3SLsHpCSg", "The World Looks Red", ARTISTS["HEAVEN_PIERCE_HER"], "ultrakill_ost_violence", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=Gcj9-iF_lTw", "War Without Reason", ARTISTS["HEAVEN_PIERCE_HER"], "ultrakill_ost_violence", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=u5heWZ9occg", "Wildside", "ALI", "wildside_ali"),
        Song("https://music.youtube.com/watch?v=BlnVP2_dIb4", "Feed the Machine", ARTISTS["OLD_MANS_POISON"], "feed_the_machine_old_mans_poison"),
        Song("https://music.youtube.com/watch?v=vp95QY2MVMk", "THE ANTIHUMAN", [ARTISTS["IVYCOMB"], ARTISTS["STEPHANAFRO"]], "the_antihuman_ivycomb"),
        Song("https://music.youtube.com/watch?v=LgmMoNwU0n0", "Miller-Z-Mixed", [ARTISTS["ZSHARP"], "bubu", "Chase Redding", "SleepyOreo", "whotookrio"], "miller_z_mixed"),
        Song("https://music.youtube.com/watch?v=p1h3Z-48Eec", "MADE TO HATE YOU", [ARTISTS["LONGEST_SOLO_EVER"], "Genichris", "Gianni Matragano"], "made_to_hate_you_lse"),
        Song("https://music.youtube.com/watch?v=ng6nJTrOPo8", "The Moss", "Cosmo Sheldrake", "the_moss_cosmo_sheldrake"),
        Song("https://music.youtube.com/watch?v=QDYUiCPLtxk", "In Absentia ΛΟΓΟΣ", ARTISTS["HEAVEN_PIERCE_HER"], "ultrakill_ost_fraud", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=8QCX2Z-9akY", "Suffering Leaves Suffering Leaves", ARTISTS["HEAVEN_PIERCE_HER"], "ultrakill_ost_violence", Album.ULTRAKILL_OST, 1, has_lyrics = False),
        Song("https://music.youtube.com/watch?v=qUTYWFSVkZ0", "Artist Block", "St4ticFilms", "artist_block_tadc"),
        Song("https://music.youtube.com/watch?v=E0jO_n86UyQ", "Artist Block: Reprise", ["St4ticFilms", "Logan Pettipas"], "artist_block_reprise_tadc"),
    ]

def get_thumbnails() -> list[Thumbnail]:
    return [
        Thumbnail("https://music.youtube.com/watch?v=j6acpg3IH6A", "ship_in_a_bottle"), # Ship in a Bottle
        Thumbnail("https://music.youtube.com/watch?v=zSQSc3gf03k", "jevil_anime_opening"), # Jevil Anime Opening
        Thumbnail("https://music.youtube.com/watch?v=WIBusox8PO0", "brainiac_maniac_noteblock_remix"), # Brainiac Maniac (NoteBlock)
        Thumbnail("https://music.youtube.com/watch?v=9bZILBqDuqw", "ad_infinitum"), # AD INFINITUM
        Thumbnail("https://music.youtube.com/watch?v=dxBkBjnbAMs", "vs_marx_kirby_with_lyrics"), # Vs Marx Kirby with Lyrics
        Thumbnail("https://music.youtube.com/watch?v=HSHrv3aX7ac", "bad_time_trio_with_lyrics"), # Bad Time Trio
        Thumbnail("https://music.youtube.com/watch?v=p36FgvNaY3Q", "hollow_knight_anime_opening"), # Hollow Knight Anime Opening
        Thumbnail("https://music.youtube.com/watch?v=DEPXNxex1as", "monkeys_paw"), # Monkey's Paw
        Thumbnail("https://music.youtube.com/watch?v=wdwAPupz6EY", "the_court_jester"), # The Court Jester
        Thumbnail("https://music.youtube.com/watch?v=GG4sVao65J4", "level!_ust"), # Level! UST
        Thumbnail("https://music.youtube.com/watch?v=CENW2YMprZE", "push_cg5"),
        # Thumbnail("https://music.youtube.com/watch?v=95lRa2Ls2sU", "push_cg5"), # Push (CG5)
        Thumbnail("https://music.youtube.com/watch?v=5HksWwytHq8", "how_far_ill_go_villain_song"), # How Far I'll Go Villain Song
        Thumbnail("https://music.youtube.com/watch?v=wE-vn1cu69I", "broken_machine"), # Broken Machine
        Thumbnail("https://music.youtube.com/watch?v=j7_58XXOulY", "we_dont_talk_about_bruno_villain_song"), # We Don't Talk About Bruno Villain Song
        Thumbnail("https://music.youtube.com/watch?v=ge8fKFKiRZI", "to_the_bone"), # To the Bone
        Thumbnail("https://music.youtube.com/watch?v=w0jcR3l3wL8", "knives_gears_and_wires"), # Knifes, Gears and Wires
        Thumbnail("https://music.youtube.com/watch?v=5_J3pPAv1Mc", "the_show_that_never_ends"), # The Show That Never Ends
        Thumbnail("https://music.youtube.com/watch?v=1W0bgeoDFIw", "just_look_my_way"), # Just Look My Way
        Thumbnail("https://music.youtube.com/watch?v=lA2O3t7Usac", "code_red_lse"), # Code Red
        Thumbnail("https://music.youtube.com/watch?v=yc3xuaA44YY", "deaths_doorstep"), # Death's Doorstep
        Thumbnail("https://music.youtube.com/watch?v=Zx1vDGKyX5E", "a_hat_in_time_musical_bytes_album"), # A Hat in Time Musical Bytes
        Thumbnail("https://music.youtube.com/watch?v=hVRNjTy8Uuk", "hollow_knight_musical_bytes_album"), # Hollow Knight Musical Bytes
        Thumbnail("https://music.youtube.com/watch?v=s0KWCdNoqvY", "no_exit_lse"),
        Thumbnail("https://music.youtube.com/watch?v=ResmeNVHOKQ", "this_world_of_mine"), # This world of mine (Musiclide)
        Thumbnail("https://music.youtube.com/watch?v=CLW3FnDa1nQ", "inside_album"), # Welcome to the internet
        Thumbnail("https://music.youtube.com/watch?v=PMKNQHauP7s", "empires"), # Empires
        Thumbnail("https://music.youtube.com/watch?v=LJbqYbi9mTA", "racoon_mix"), # Racoon Mix
        Thumbnail("https://music.youtube.com/watch?v=K7eG37qiP-g", "hypnosis_lse"), # Hypnosis (LSE)
        Thumbnail("https://music.youtube.com/watch?v=jLopU2IsrUY", "you_cant_hide"), # You Can't Hide
        Thumbnail("https://music.youtube.com/watch?v=7PA38zRrPRM", "judgement_tryhardninja"), # Judgement (TryHardNinja)
        Thumbnail("https://music.youtube.com/watch?v=oub98zjmQKQ", "circus_hop"), # Circus Hop
        Thumbnail("https://music.youtube.com/watch?v=trhOkSS-ylg", "antihuman_ivycomb"), # ANTIHUMAN
        Thumbnail("https://music.youtube.com/watch?v=-og6NEppvrg", "notorious_ivycomb"), # NOTORIOUS
        Thumbnail("https://music.youtube.com/watch?v=gFOJkIk8fcs", "insane_hazbin_hotel"), # Insane
        Thumbnail("https://music.youtube.com/watch?v=MURua52_YPg", "my_ordinary_life"), # My Orfinary Life
        Thumbnail("https://music.youtube.com/watch?v=2UmbRrc-Zd4", "a_million_gruesome_ways_to_die"), # A Million Gruesome Ways To Die
        Thumbnail("https://music.youtube.com/watch?v=5Z56MZFMp0k", "discord_the_living_tombstone"), # Discord (The Living Tombstone)
        Thumbnail("https://music.youtube.com/watch?v=BWhEry67iC0", "keter_qualities"), # Keter Qualities
        Thumbnail("https://music.youtube.com/watch?v=Diob2vPNHec", "overthrone_lse"), # Overthrone
        Thumbnail("https://music.youtube.com/watch?v=WopMFtLen_Y", "sweet_little_lies_ivycomb"), # Sweet Little Lies (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=6L8gr_e-nSI", "youll_be_gone"), # You'll be Gone
        Thumbnail("https://music.youtube.com/watch?v=04U4CjoS7jQ", "want_some_fun"), # Want some fun
        Thumbnail("https://music.youtube.com/watch?v=HX9HGP7xpY4", "youre_just_like_pop_music"), # You're Just Like Pop Music
        Thumbnail("https://music.youtube.com/watch?v=piVJp1Ijuqo", "luminescence_ivycomb"), # Luminescence
        Thumbnail("https://music.youtube.com/watch?v=PtMcTjAoKBs", "sleepwalk"), # Sleepwalk
        Thumbnail("https://music.youtube.com/watch?v=fQ3-CyvLkpc", "hazbin_hotel_ost_s1"),
        Thumbnail("https://music.youtube.com/watch?v=1gQ4Xlr9Ye8", "blue_bird_ivycomb"), # Blue Bird (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=wD9yuHkAxxk", "slugcat_pinball"), # SLUGCAT PINBALL
        Thumbnail("https://music.youtube.com/watch?v=txeHnnCj9Ow", "fratricide_ivycomb"), # Fratricide
        Thumbnail("https://music.youtube.com/watch?v=YMq-AhRfG9A", "system_error_ivycomb"), # System Error (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=8o5CRs0n--U", "spider_bites_ivycomb"), # Spider Bites :3
        Thumbnail("https://music.youtube.com/watch?v=5rrxIdkRcDk", "sahara_ivycomb"), # SAHARA
        Thumbnail("https://music.youtube.com/watch?v=w4vECnueTP4", "lovesick_ivycomb"), # Lovesick (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=wGz_h1Qrt5g", "in_the_mirror"), # In The Mirror
        Thumbnail("https://music.youtube.com/watch?v=aJtQYbn-ks8", "musical_masquerave"), # Golden Land
        Thumbnail("https://music.youtube.com/watch?v=wNti1Z3im-E", "no_eternity_ivycomb"), # No Eternity
        Thumbnail("https://music.youtube.com/watch?v=FI2D5-5Rg6E", "everlasting_fun"), # Everlasting Fun
        Thumbnail("https://music.youtube.com/watch?v=_KAXvMB4434", "tokyo_ivycomb"), # TOKYO (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=acdxrueuYys", "open_the_door_lse"), # Open the Door
        Thumbnail("https://music.youtube.com/watch?v=iRZnnh3WyW4", "wool_over_our_eyes"), # Wool Over our Eyes
        Thumbnail("https://music.youtube.com/watch?v=zj0HgKOTGrY", "antivillain"), # ANTIVILLAIN
        Thumbnail("https://music.youtube.com/watch?v=4YSVyA_CgKA", "furrýmon"), # Furrýmon
        Thumbnail("https://music.youtube.com/watch?v=RjTu6hfccl0", "fighting_insanity"), # Fighting Insanity
        Thumbnail("https://music.youtube.com/watch?v=6aoCakMvlcM", "best_friends_or3o"), # Best Friend (OR3O)
        Thumbnail("https://music.youtube.com/watch?v=4VsfEt03VJk", "memory_merge"), # Memory Merge
        Thumbnail("https://music.youtube.com/watch?v=Y6uiP27zKi0", "spots_snuffles"), # SPOTS (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=QbEYRi4lCmc", "wont_go_snuffles"), # Won't go (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=ki9Jo4trgtA", "ready_or_not_snuffles"), # Ready or Not (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=tw5ZsxDSrbI", "keep_on_with_it_snuffles"), # Keep on With It (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=ezhdzPEG3DQ", "too_late_2_snuffles"), # Too Late 2 (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=0xmakTOaFZk", "forgive_me_please_snuffles_album"), # Please Forgive Me (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=xp2SzlnzbkA", "seven_run_snuffles"), # Seven Run (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=dtVI47rE8JU", "smile_like_you_mean_it"), # Smile Like You Mean It
        Thumbnail("https://music.youtube.com/watch?v=-sM9ocXMHk4", "data_reject_ivycomb"), # DATA_REJECT
        Thumbnail("https://music.youtube.com/watch?v=22ZjX8MmYxA", "ldr_ivycomb"), # LDR
        Thumbnail("https://music.youtube.com/watch?v=M5mIYZbYL_4", "buther_vanity"), # BUTHER VANITY
        Thumbnail("https://music.youtube.com/watch?v=0dUCeqJ14RY", "tokyo_aniversary_ivycomb"), # TOKYO ANIVERSARY (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=7jq9c4uyOL4", "i_forgot_that_you_exist"), # I Forgot that You Exist
        Thumbnail("https://music.youtube.com/watch?v=tjXACkFQnSo", "forgotten_ivycomb"), # Forgotten (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=RtH3seTek58", "cybernetic_heart_ivycomb"), # CYBERNETIC HEARTH
        Thumbnail("https://music.youtube.com/watch?v=LglXzrkNub8", "this_thought_snuffles"), # This Thought (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=pIcMXpeeLKU", "lets_get_weird_lse"), # Let's Get Weird (LSE)
        Thumbnail("https://music.youtube.com/watch?v=HDxd7GyReYw", "world_of_everything_ivycomb"), # World of Everything (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=Q43lsU6Xf_0", "want_some_fun_remastered"), # Want some fun (REMASTERED)
        Thumbnail("https://music.youtube.com/watch?v=PCcl_c_9GAY", "digital_land"), # Digital Land
        Thumbnail("https://music.youtube.com/watch?v=ypxtbI-NWg4", "fnaf_kids"), # FNAF Kids
        Thumbnail("https://music.youtube.com/watch?v=XSLFuWdQ-SA", "make_believe_ivycomb"), # MAKE BELIEVE (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=CDITKwzQauc", "i_dont_wanna_snuffles"), # I Don't Wanna (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=7JflwxgJVU0", "vines"), # Vines (Shadrow)
        Thumbnail("https://music.youtube.com/watch?v=ZOflZ0lKPF0", "in_the_light"), # In the Light
        Thumbnail("https://music.youtube.com/watch?v=8mdb34cq7fk", "y2k"), # Y2K (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=BdBV6PvgwO8", "raised_by_aliens_album"), # Raised by Aliens (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=fXjCvKYVp9U", "linger_in_the_rain"), # Linger in the Rain
        Thumbnail("https://music.youtube.com/watch?v=bMwcoK1Tw1g", "come_back_to_me_shadow"), # Come Back to Me
        Thumbnail("https://music.youtube.com/watch?v=DZn3hNS286s", "hypnofreak_ivycomb"), # HYPNOFREAK
        Thumbnail("https://music.youtube.com/watch?v=SATG3rxX1NE", "shadow_wick"), # Shadow Wick
        Thumbnail("https://music.youtube.com/watch?v=hqErigwP78Y", "nine_sols_ost"), # Nine Sols
        Thumbnail("https://music.youtube.com/watch?v=D26OsQXqi-8", "sun_spots_ivycomb"), # Sun Spots (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=ehnLkHR05Ao", "wear_the_mask_lse"), # Wear the Mask (LSE)
        Thumbnail("https://music.youtube.com/watch?v=Hq14Fy4uscw", "burning_souls"), # Burning Souls
        Thumbnail("https://music.youtube.com/watch?v=y6KOV_SMbjE", "neverland_ivycomb"), # Neverland (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=x4eVHZCx0N4", "infamous_ivycomb"), # INFAMOUS (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=iOhRsJYwqgg", "broken_machine_pancake_mix"), # Broken Machine Pancake Mix
        Thumbnail("https://music.youtube.com/watch?v=K5gYGMg_ZUc", "the_ringmaster"), # THE RINGMASTER
        Thumbnail("https://music.youtube.com/watch?v=mHla7S8vHEw", "rebirth_album"), # Rebirth (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=vkubg_0xKUw", "collared"), # Collared
        Thumbnail("https://music.youtube.com/watch?v=nWJ1PcSt73E", "the_house_aways_wins_remastered"), # The House Aways Wins REMASTERED
        Thumbnail("https://music.youtube.com/watch?v=tdlq_dDtSqw", "the_data_stream"), # The Data Stream
        Thumbnail("https://music.youtube.com/watch?v=kBmYt2eNc9I", "the_merry_go_round"), # The Merry-Go-Round
        Thumbnail("https://music.youtube.com/watch?v=YzxwZCY5gUM", "heat_ivycomb"), # HEAT (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=xaIPn8uRMBo", "spots2_snuffles"), # SPOTS 2
        Thumbnail("https://music.youtube.com/watch?v=IZzgzR1iqYY", "love_letter_ivycomb"), # Love Letter (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=GFHeMRAAdtY", "if_i_were_to_die"), # If i were to Die
        Thumbnail("https://music.youtube.com/watch?v=ADYIrhz0c_A", "i_cant_stop_making_mistakes_snuffles"), # I Can't Stop Making Mistakes (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=BYlWUISY4oM", "off_the_air"), # Off the Air
        Thumbnail("https://music.youtube.com/watch?v=YO1dLoYu3PQ", "fight_til_im_good_enough"), # Fight Til I'm Good Enough
        Thumbnail("https://music.youtube.com/watch?v=U5SjlUnsPZI", "crimson_galaxies"), # Crimson Galaxies
        Thumbnail("https://music.youtube.com/watch?v=j9X-8cli1HM", "lab_rat_ivycomb"), # LAB RAT
        Thumbnail("https://music.youtube.com/watch?v=0zPpqBDDmbI", "i_still_create"), # I Still Create
        Thumbnail("https://music.youtube.com/watch?v=ofIUk7Jzt24", "outer_skies_ivycomb"), # OUTER SKIES
        Thumbnail("https://music.youtube.com/watch?v=yJtFKuZoRvg", "nirvana_ivycomb"), # Nirvana
        Thumbnail("https://music.youtube.com/watch?v=yrP9VPW0cdo", "so_long"), # So Long
        Thumbnail("https://music.youtube.com/watch?v=zr8L899Pg5E", "cut_the_ties"), # Cut the Ties
        Thumbnail("https://music.youtube.com/watch?v=m30ad1EoTVk", "like_a_ghost"), # Like a Ghost
        Thumbnail("https://music.youtube.com/watch?v=TojwRLDLL_s", "i_never_feel_alone_snuffles"), # I Never Feel Alone (Snuffles)
        Thumbnail("https://music.youtube.com/watch?v=PhvIBk1vW2s", "homesick_wanderlust"), # HOMESICK WANDERLUST
        Thumbnail("https://music.youtube.com/watch?v=M3_EAHBRklo", "down_down_down"), # Down Down Down (Ivycomb)
        Thumbnail("https://music.youtube.com/watch?v=0NmJFpjAMIc", "our_summer_dreams_album"), # Our Summer Dreams
        Thumbnail("https://music.youtube.com/watch?v=9E0xFvFCUTM", "order_ultrakill_ost"),
        Thumbnail("https://music.youtube.com/watch?v=eeMC0SG2cnA", "keygen_church_ultrakill"),
        Thumbnail("https://music.youtube.com/watch?v=TWS07eY1ElU", "war_ultrakill_ost"),
        Thumbnail("https://music.youtube.com/watch?v=uYBO_Sk5YiE", "terraria_calamity_ost"),
        Thumbnail("https://music.youtube.com/watch?v=0k1lQM-0_j0", "ultrakill_ost_violence"),
        Thumbnail("https://music.youtube.com/watch?v=u5heWZ9occg", "wildside_ali"),
        Thumbnail("https://music.youtube.com/watch?v=BlnVP2_dIb4", "feed_the_machine_old_mans_poison"),
        Thumbnail("https://music.youtube.com/watch?v=vp95QY2MVMk", "the_antihuman_ivycomb"),
        Thumbnail("https://music.youtube.com/watch?v=LgmMoNwU0n0", "miller_z_mixed"),
        Thumbnail("https://music.youtube.com/watch?v=p1h3Z-48Eec", "made_to_hate_you_lse"),
        Thumbnail("https://music.youtube.com/watch?v=ng6nJTrOPo8", "the_moss_cosmo_sheldrake"),
        Thumbnail("https://music.youtube.com/watch?v=QDYUiCPLtxk", "ultrakill_ost_fraud"),
        Thumbnail("https://music.youtube.com/watch?v=qUTYWFSVkZ0", "artist_block_tadc"),
        Thumbnail("https://music.youtube.com/watch?v=E0jO_n86UyQ", "artist_block_reprise_tadc"),
    ]

def get_config() -> dict[str, bool | int | float | str]:
    return {
        "embed-lrc": False,
    }
