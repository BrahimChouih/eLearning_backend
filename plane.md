
Accounts(app):
    - Name
    - Picture 
    - Own courses
    - Created at
    - Country
    - Purchased courses



Course(app):
    - title
    - Owner (relation with Account model)
    - create_at 
    - Cover
    - Price
    - Rate (average)
    - category
    - Num reviewers
    - category


Videos(model):
    - title
    - course (relation with Course model) 
    - Video
    - Lesson number
    - Thumbnail



Details (APP):
    Categories(model):
        - Category name
        - Pictuer



    Comments(model):
        - Comment
        - Owner (relation with Account model)
        - comment_on (relation with course app)

