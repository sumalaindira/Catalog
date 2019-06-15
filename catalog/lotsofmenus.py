from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Package, Base, MenuItem, User

engine = create_engine('sqlite:///packagedata.db')
"""Bind the engine to the metadata of the Base class so that the
declaratives can be accessed through a DBSession instance"""
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
"""A DBSession() instance establishes all conversations with the database
 and represents a "staging zone" for all the objects loaded into the
 database session object. Any change made against the objects in the
 session won't be persisted into the database until you call
 session.commit(). If you're not happy about the changes, you can
 revert all of them back to the last commit by calling
 session.rollback()"""
session = DBSession()
"""Create First User"""
User1 = User(name="Indira Sumala", email="sumala.indira@gmail.com",
             picture='/static/profile.jpg')
session.add(User1)
session.commit()  
    
"""Menu for FACIAL/CLEAN UP"""
package1 = Package(user_id=1, name="FACIAL/CLEAN UP")
session.add(package1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="PEARL FACIAL",
                     description='''Benefits Of Pearl Facial On Skin. 
                     - Pearl facial is extremely useful on sun-damaged and sun-tanned skin. 
                     It works as an anti-tan face mask. - Due to active enzymes present in the pearl powder,
                     it can help to prevent the appearance of wrinkles and fine lines on the face early.''',
                     price="$25.88",
                     picture="/static/pearl.jpg",
                     package=package1)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="DIAMOND FACIAL",
                     description='''Do not confuse it with Diamond Microdermabrasion (which is a cosmetic
                      procedure using diamonds). I am talking about facial massage gels and creams containing 
                      diamond dust. These are the most luxe skincare ranges in the town right now.
                      Most of the major skin care brands have come up with skin care products and facial
                      kits that contain diamond dust. These have a range of benefits to offer.''',
                     price="$36.46",
                     picture="/static/Daimend_facial_images.jpg",
                     package=package1)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="PLATINUM FACIAL",
                     description='''Platinum facial kit helps to cleanse your skin and restores 
                     the natural balance of skin to keep it healthy. Based on highly advanced technology, 
                     this revolutionary facial kit contains platinum solution along with powerful natural 
                     ingredients which provide super benefits to you skin.''',
                     price="$21.35",
                     picture="/static/platinum.jpg",
                     package=package1)
session.add(menuItem1)
session.commit()



menuItem2 = MenuItem(user_id=1, name="GOLD/SILVER FACIAL",
                     description='''gold is an antioxidant and has anti-inflammatory properties.
                     According to Tabasum Mir, a skincare physician in cosmetic dermatology and cosmetic 
                     laser surgery, the metal can calm acne inflammation, reduce skin redness and protect 
                     against free radicals that lead to wrinkles and sun damage.''',
                     price="$22.99",
                     picture="/static/goldsilver.jpg",
                     package=package1)
session.add(menuItem2)
session.commit()

menuItem2 = MenuItem(user_id=1, name="ANTI TAN FACIAL",
                     description='''The enrich anti tan facial is about the fine art of rehydrating. 
                     your facial skin which has been damaged by the sun's ultraviolet rays. we do this by removing dirt and makeup from your face with Safran cleansing lotion. ... then we mix a frank face pack with rose water and apply it on your face.''',
                     price="$19.00",
                     picture="/static/Anti_tan_facial.jpg",
                     package=package1)
session.add(menuItem2)
session.commit()


"""Menu for MANICURE/PEDICURE"""
package2 = Package(user_id=1, name="MANICURE/PEDICURE")
session.add(package2)
session.commit()

menuItem1 = MenuItem(user_id=1, name="REGULAR PEDICURE/MANICURE",
                     description='''They also help keep hands looking young. During any manicure or pedicure, 
                     you receive a relaxing massage of the hands and feet. This helps to improve blood circulation
                     and improves mobility for the joints. With regular manicures and pedicures, the chances of your 
                     nails developing fungi and other infections are reduced.''',
                     price="$12.56",
                     picture="http://tinyurl.com/yyr8acxn",
                     package=package2)
session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="ANTI - TAN PEDICURE/MANICURE",
                     description='''Several types of pedicures are now available to us now. Most women are not 
                     aware that there are several different types of pedicure procedures that are done using 
                     different ingredients. If you go to a foot spa or even a salon, you will will be handed 
                     menu card that describes many types of pedicures. All these pedicures include cleaning, 
                     filing nails, scrubbing your feet, moisturising and a foot massage. The difference is in the 
                     ngredients used for the pedicure and also the purpose of it.''',
                     price="$19.32",
                     picture="https://tinyurl.com/y3aunpuo",
                     package=package2)
session.add(menuItem1)
session.commit()   

menuItem1 = MenuItem(user_id=1, name="CRYSTAL SPA ",
                     description='''A crystal healing spa does not perform miracles. They provide a service 
                     that maximizes one's sense of self. It offers an opportunity to develop a greater aura of 
                     peace and balance, to cleanse and rejuvenate. I personally have experienced an increased 
                     sense of well-being that goes beyond being physically fit. I have walked out of a crystal 
                     healing spa with a deeper understanding of myself and how I want my future to unfold. 
                     I look forward to the time I'm going to spend with my family and friends, and motivating 
                     my clients to live the best possible lives they can.''',
                     price="$19.58",
                     picture="https://tinyurl.com/y46tvwbx",
                     package=package2)
session.add(menuItem1)
session.commit()



"""Menu for FULL WAX"""
package3 = Package(user_id=1, name="FULL WAX")
session.add(package3)
session.commit()

menuItem1 = MenuItem(user_id=1, name="FULL ARMS + FULL LEGS + UNDER ARMS",
                     description='''Waxing is a safe, economical and reliable way of removing body hair. 
                     Unlike shaving, a good wax can keep that unwanted body hair away for as long as 6 weeks. 
                     By adding waxing to your beauty regime, you will make your skin glow with radiance while 
                     feeling smooth, fresh and clean''',
                     price="$25.50",
                     picture="/static/fullwax.jpg",
                     package=package3)
session.add(menuItem1)
session.commit()   
menuItem1 = MenuItem(user_id=1, name="FULL FRONT/BACK",
                     description='''Smooth and even skin. One of the best benefits of waxing is that your skin
                     will feel smooth and even. When waxing, you not only remove unwanted hair you also wax away 
                     any dry and dead skin cells in the process! Irritation and allergies free. 
                     There are minimal chemicals involved in the waxing process, 
                     so rarely does waxing cause any skin irritation or allergy.''',
                     price="$21.99",
                     picture="/static/Artboard.jpg",
                     package=package3)
session.add(menuItem1)
session.commit()   
     
menuItem1 = MenuItem(user_id=1, name="FULL BODY",
                     description='''Stubble free skin  Waxing removes unwanted hair completely, from its roots. 
                     Shaving, on the other hand, often results in stubbles, leaving your skin feeling rough and abrasive.
                     Irritation and allergies-free. There are minimal chemicals involved in the waxing process, 
                     so rarely does waxing cause any skin irritation or allergy.''',
                     price="$15.99",
                     picture="http://tinyurl.com/y6ytax8r",
                     package=package3)
session.add(menuItem1)
session.commit()

"""Menu for HEAD MASSAGE/HAIR SPA"""
package4 = Package(user_id=1, name="HEAD MASSAGE/HAIR SPA")
session.add(package4)
session.commit()

menuItem1 = MenuItem(user_id=1, name="HEAD MASSAGE",
                     description='''The massage increases nourishment and oxygen to the scalp and hair 
                     follicle which in turns stimulates hair growth. It detoxifies the body by stimulating 
                     lymphatic drainage Indian Head Massage stimulates and improves lymphatic drainage and blood 
                     flow to the neck thus helping to remove waste products from the body.''',
                     price="$21.78",
                     picture="http://tinyurl.com/y5rbdbkq",
                     package=package4)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="HEAD & SHOULDER MASSAGE",
                     description='''Indian head massage can also help to improve your overall sense of wellbeing, 
                     hich in turn may also help to lower raised blood pressure and relieve anxiety. ... 
                     Relaxing the muscles in the neck, shoulders, head and back and alleviating tension in these 
                     areas, helps to reduce pain and improves joint mobility.''',
                     price="$17.99",
                     picture="http://tinyurl.com/yxvuyug5",
                     package=package4)
session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="FULL BODY excluding HEAD MASSAGE",
                     description='''Full body massage helps release that tightness in the body without pain and 
                     makes your body flexible. Massage also helps in relieving tiredness, pain and rejuvenate the 
                     ody. ... Relieves Eyestrain: Massage around the head and eye helps to improve eyesight and 
                     avoid redness or irritation, dry or watery eyes.''',
                     price="$24.99",
                     picture="http://tinyurl.com/y4cpmw8a",
                     package=package4)  
session.add(menuItem1)
session.commit()

     
print("added menu items!")    
    