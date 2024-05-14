from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "introduction-to-web-development",
        "image": "web-dev.jpg",
        "author": "Ninó",
        "date": date(2024, 5, 14),
        "title": "Meow-some Adventures in HTML: Ninó's Introduction to Web Development",
        "excerpt": "Join Ninó on his coding journey as he delves into the basics of HTML, the language of the web. From <head> to <body>, Ninó shares his experiences and insights into crafting purr-fectly structured web pages.",
        "content": """
            Embark on an exciting journey with Ninó as he takes his first steps into the world of web development through HTML. With eager eyes and a curious mind, Ninó immerses himself in the 
            foundational elements of HTML, understanding how each tag contributes to the structure and functionality of a webpage. From the <head> section where metadata resides to the <body> where content 
            comes alive, Ninó explores the intricacies of HTML, marveling at its simplicity and power. With each line of code, Ninó not only learns the syntax of HTML but also gains a deeper appreciation for the art of
             crafting purr-fectly structured web pages. As he shares his experiences and insights, Ninó invites fellow felines and humans alike to join him on this meow-some adventure in web development. Together, let's 
             uncover the wonders of HTML and unleash our creativity on the digital canvas of the web.
            """,
    },
    {
        "slug": "introduction-to-bootstrap",
        "image": "bootstrap.jpg",
        "author": "Ninó",
        "date": date(2024, 4, 14),
        "title": "Feline-friendly Frameworks: Ninó's Journey with Bootstrap",
        "excerpt": "In this post, Ninó discovers the magic of Bootstrap and how it simplifies the process of building responsive and sleek websites. With Bootstrap by his side, Ninó's web development adventures reach new heights!",
        "content": """
            Embark on a thrilling journey with Ninó as he delves into the world of web development with Bootstrap. 
            In this enlightening post, Ninó shares his experience of discovering the magic of Bootstrap and how it revolutionizes the process of creating responsive and sleek websites. 
            With its intuitive grid system, pre-designed components, and extensive library of CSS and JavaScript plugins, Bootstrap becomes Ninó's trusted companion in his quest to craft visually stunning 
            and user-friendly web experiences. With Bootstrap's powerful features and flexible layout options, Ninó's web development adventures soar to new heights. From effortlessly designing mobile-friendly 
            interfaces to streamlining the implementation of complex features, Ninó finds himself empowered to bring his creative visions to life with ease. Join Ninó as he unlocks the full potential of 
            Bootstrap and embraces the endless possibilities it offers for creating feline-friendly websites that captivate and delight users worldwide.
            """,
    },
    {
        "slug": "tips-for-debugging",
        "image": "debugging.png",
        "author": "Ninó",
        "date": date(2024, 4, 21),
        "title": "Purr-fecting the Craft: Ninó's Tips for Debugging",
        "excerpt": "Every coder encounters bugs, and Ninó is no exception! Join him as he shares his top tips and tricks for debugging code like a pro. From console.log() to browser developer tools, Ninó's got you covered.",
        "content": """
            Join Ninó as he ventures into the realm of debugging, armed with a feline's intuition and a coder's determination. 
            In this enlightening post, Ninó shares invaluable insights and techniques honed through countless hours of debugging adventures. 
            From the timeless classic of using console.log() to the sophisticated tools of browser developer consoles, Ninó unveils his arsenal of debugging tricks to help fellow coders 
            tackle bugs with confidence. With Ninó's guidance, navigating through the maze of errors becomes less daunting and more empowering. 
            Whether you're a seasoned developer or a coding novice, Ninó's tips for debugging will equip you with the skills and strategies needed to unravel even the trickiest of bugs. 
            So grab your keyboard and join Ninó on this quest to purr-fect the craft of debugging and unleash your coding potential!
            """,
    }
]

def index(request):
    sorted_posts = sorted(all_posts, key=lambda post: post["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
