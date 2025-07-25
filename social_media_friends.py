def analyze_frienships():

    facebook_friends = {"alice","bob","charlie","diana","eve","frank"}
    instagram_friends = {"bob","charlie","diana","eve","frank","george"}
    twitter_friends = {"charlie","diana","eve","frank","george","harry"}
    linkedin_friends = {"diana","eve","frank","george","harry","isabel"}

    all_platforms = facebook_friends.union(instagram_friends,twitter_friends,linkedin_friends)
    facebook_only = facebook_friends - instagram_friends - twitter_friends - linkedin_friends
    instagram_xor_twitter = (instagram_friends.union(twitter_friends)) - (instagram_friends.intersection(twitter_friends))
    total_unique_friends = len(all_platforms)
    exactly_2_platforms = len(facebook_friends.intersection(instagram_friends)) + len(facebook_friends.intersection(twitter_friends)) + len(facebook_friends.intersection(linkedin_friends)) + len(instagram_friends.intersection(twitter_friends)) + len(instagram_friends.intersection(linkedin_friends)) + len(twitter_friends.intersection(linkedin_friends)) - 6 * len(facebook_friends.intersection(instagram_friends).intersection(twitter_friends).intersection(linkedin_friends))

    return {
        "all_platforms":all_platforms,
        "facebook_only":facebook_only,
        "instagram_xor_twitter":instagram_xor_twitter,
        "total_unique_friends":total_unique_friends,
        "exactly_2_platforms":exactly_2_platforms
    }
result = analyze_frienships()
print("all platforms:",result.get("all_platforms"))
print("Facebook only:",result.get("facebook_only"))
print("Instragram XOR Twitter:",result.get("instagram_xor_twitter"))
print("Total unique friends:",result.get("total_unique_friends"))
print("Exactly 2 platforms:",result.get("exactly_2_platforms"))
