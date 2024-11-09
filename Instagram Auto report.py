import instaloader
import datetime

def generate_instagram_report(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Load the profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Get profile details
    profile_info = {
        "Username": profile.username,
        "Full Name": profile.full_name,
        "Biography": profile.biography,
        "Followers": profile.followers,
        "Following": profile.followees,
        "Is Private": profile.is_private,
        "Is Verified": profile.is_verified,
        "External URL": profile.external_url
    }

    # Get the latest post
    latest_post = next(profile.get_posts())

    # Get post details
    post_info = {
        "Shortcode": latest_post.shortcode,
        "Caption": latest_post.caption,
        "Comments": latest_post.comments,
        "Likes": latest_post.likes,
        "Date": latest_post.date_utc,
        "Is Video": latest_post.is_video
    }

    # Generate the report
    report = f"""
    Instagram Report for {username}
    Profile Details:
    {profile_info}
    
    Latest Post:
    {post_info}
    """

    return report

# Example usage
username = "example_username"
report = generate_instagram_report(username)
print(report)
