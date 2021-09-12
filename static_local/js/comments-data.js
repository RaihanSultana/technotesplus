var commentsArray = [
    {
        id: 1,
        parent: null,
        created: "2015-01-01",
        modified: "2015-01-01",
        content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed posuere interdum sem. Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien. Mauris varius diam vitae arcu.",
        attachments: [],
        pings: [],
        creator: 6,
        fullname: "Simon Powell",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
        created_by_admin: false,
        created_by_current_user: false,
        upvote_count: 3,
        user_has_upvoted: false,
        is_new: false,
    },
    {
        id: 2,
        parent: null,
        created: "2015-01-02",
        modified: "2015-01-02",
        content:
            "Sed posuere interdum sem. Quisque ligula eros ullamcorper quis, lacinia quis facilisis sed sapien. Mauris varius diam vitae arcu.",
        attachments: [],
        pings: [],
        creator: 5,
        fullname: "Administrator",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
        created_by_admin: true,
        created_by_current_user: false,
        upvote_count: 2,
        user_has_upvoted: false,
        is_new: false,
    },
    {
        id: 3,
        parent: null,
        created: "2015-01-03",
        modified: "2015-01-03",
        content:
            "@Hank Smith sed posuere interdum sem.\nQuisque ligula eros ullamcorper https://www.google.com/ quis, lacinia quis facilisis sed sapien. Mauris varius diam vitae arcu. Sed arcu lectus auctor vitae, consectetuer et venenatis eget #velit.",
        attachments: [],
        pings: {
            3: "Hank Smith",
        },
        creator: 1,
        fullname: "You",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
        created_by_admin: false,
        created_by_current_user: true,
        upvote_count: 2,
        user_has_upvoted: true,
        is_new: false,
    },
];

var usersArray = [
    {
        id: 1,
        fullname: "Current User",
        email: "current.user@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 2,
        fullname: "Jack Hemsworth",
        email: "jack.hemsworth@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 3,
        fullname: "Hank Smith",
        email: "hank.smith@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 4,
        fullname: "Todd Brown",
        email: "todd.brown@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 5,
        fullname: "Administrator",
        email: "administrator@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 6,
        fullname: "Simon Powell",
        email: "simon.powell@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
    {
        id: 7,
        fullname: "Bryan Connery",
        email: "bryan.connery@viima.com",
        profile_picture_url:
            "https://viima-app.s3.amazonaws.com/media/public/defaults/user-icon.png",
    },
];
