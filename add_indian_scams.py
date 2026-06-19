import pandas as pd

scam_messages = [
    "we found your chiild in police station send 1000 rupay to sent him free",
    "Dear customer, your electricity power will be disconnected at 9:30 PM tonight. Please call our officer immediately to update bill.",
    "Your SBI YONO account has been blocked today. Please click the link to update your PAN card KYC immediately: http://bit.ly/sbi-kyc",
    "Congratulations! You have won the KBC lottery of Rs 25 Lakhs. WhatsApp this number to claim your prize.",
    "Part time job offer: Work from home and earn Rs 5000 daily. Just like YouTube videos. Join our Telegram group now.",
    "Your package from FedEx is held at customs. Please pay the clearance fee of Rs 50 by clicking here.",
    "Dear Customer, your pre-approved personal loan of Rs 5,00,000 is ready for disbursal. Click link to apply.",
    "Your Jio number is selected for free 5G data for 3 months. Click here to activate your free recharge.",
    "Urgent: Your bank account will be suspended. Please complete your e-KYC by downloading this APK file.",
    "Traffic Police Maha challan: You have a pending traffic challan of Rs 2000. Pay online here to avoid court.",
    "Sir your child is involved in a rape case and arrested. Send Rs 50000 on PhonePe to settle the matter.",
    "HDFC Bank: Dear Customer, 50,000 Reward points are expiring today. Redeem them into cash by clicking here.",
    "You have been shortlisted for a data entry job. Salary: 40k/month. Contact HR on WhatsApp.",
    "Electricity department update: Your previous month bill is not updated. Power will be cut at 10 PM. Contact officer.",
    "Dear Sir/Madam, your income tax refund of Rs 15,200 is approved. Click the link to claim it directly to your bank.",
    "Amazon Gift: You are the lucky winner of iPhone 15! Pay delivery charges of Rs 199 to dispatch.",
    "Aadhar card update required. If not done your bank accounts will be frozen. Update here.",
    "Urgent message from CBI: We have an arrest warrant against your name for money laundering. Press 1 to speak to executive.",
    "You have received a payment of Rs 5000 on PhonePe. Click here to receive the money in your bank.",
    "IRCTC refund: Your ticket cancellation amount is pending. Click the link to get refund.",
    "Your free Netflix subscription is expiring. Renew for free by verifying your card details here.",
    "Earn 10,000 daily by rating Google Maps places. Message us on WhatsApp to start.",
    "Jamtara Police Station: We have arrested your son. Send money immediately to release him without FIR.",
    "Dear User, your WhatsApp will expire in 24 hours. Pay 10 Rs to renew your subscription for lifetime.",
    "This is from TRAI. Your mobile number will be deactivated in 2 hours due to illegal activity. Press 9.",
]

ham_messages = [
    "Bhai, kaha hai tu? Jaldi aaja match shuru hone wala hai.",
    "Your OTP for Paytm login is 458921. Do not share it with anyone.",
    "Swiggy: Your order from Meghana Foods is out for delivery.",
    "Meeting is rescheduled to 4 PM IST. Please join the Zoom call on time.",
    "Mummy, main thodi der me ghar aunga. Traffic me fasa hu.",
    "Your salary of Rs 45,000 has been credited to your HDFC Bank account.",
    "Did you submit the assignment? The deadline is tonight.",
    "Happy Diwali to you and your family! May this year bring joy.",
    "Zomato: Arriving in 15 mins! Your delivery partner is on the way.",
    "Can you send me the notes for yesterday's class?",
    "Your cab driver Suresh is arriving in a white Dzire (KA01 AB1234).",
    "Let's go for a movie this weekend. Kalki kaisa rahega?",
    "Electricity Bill of Rs 1250 is generated for consumer number 123456. Due date is 15th.",
    "Your Amazon package will be delivered today by 9 PM. PIN: 1243",
    "Haan bhai, theek hai. Main kal subah call karta hu tujhe.",
]

new_data = []
for msg in scam_messages:
    new_data.append({'v1': 'spam', 'v2': msg})
for msg in ham_messages:
    new_data.append({'v1': 'ham', 'v2': msg})

new_df = pd.DataFrame(new_data)

df = pd.read_csv('spam.csv', encoding='utf-8')

combined_df = pd.concat([df, new_df], ignore_index=True)

combined_df.to_csv('spam.csv', index=False, encoding='utf-8')
print(f"Added {len(scam_messages)} spam and {len(ham_messages)} ham messages. Total rows: {len(combined_df)}")
