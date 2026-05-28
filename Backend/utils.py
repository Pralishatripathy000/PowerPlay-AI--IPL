TEAM_NAME_MAP = {
    "RCB": "Royal Challengers Bengaluru",
    "MI": "Mumbai Indians",
    "CSK": "Chennai Super Kings",
    "KKR": "Kolkata Knight Riders",
    "SRH": "Sunrisers Hyderabad",
    "RR": "Rajasthan Royals",
    "DC": "Delhi Capitals",
    "PBKS": "Punjab Kings",
    "GT": "Gujarat Titans",
    "LSG": "Lucknow Super Giants"
}

VENUE_MAP = {
    "M. Chinnaswamy Stadium, Bangalore": "M Chinnaswamy Stadium",
    "MA Chidambaram Stadium, Chennai": "MA Chidambaram Stadium, Chepauk",
    "Rajiv Gandhi International Stadium, Hyderabad": "Rajiv Gandhi International Stadium, Uppal",
    "Ekana Cricket Stadium, Lucknow": "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow",
    "New PCA Cricket Stadium, Mullanpur": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
    "Barsapara Stadium, Guwahati": "Barsapara Cricket Stadium, Guwahati"
}

CITY_MAP = {
    "M Chinnaswamy Stadium": "Bengaluru",
    "Wankhede Stadium, Mumbai": "Mumbai",
    "Barsapara Cricket Stadium, Guwahati": "Guwahati",
    "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur": "Chandigarh",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow": "Lucknow",
    "MA Chidambaram Stadium, Chepauk": "Chennai",
    "Rajiv Gandhi International Stadium, Uppal": "Hyderabad"
}

TOSS_DECISION_MAP = {
    "Bat": "bat",
    "Bowl": "field",
    "bat": "bat",
    "field": "field"
}


def normalize_team_name(team):
    return TEAM_NAME_MAP.get(team, team)


def normalize_venue_name(venue):
    return VENUE_MAP.get(venue, venue)


def get_city_from_venue(venue):
    return CITY_MAP.get(venue, "Unknown")


def normalize_toss_decision(decision):
    return TOSS_DECISION_MAP.get(decision, decision)