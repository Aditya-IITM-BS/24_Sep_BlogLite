from flask import jsonify, request, current_app as app
from flask_restful import Api, Resource, fields, marshal_with
from flask_security import auth_required, current_user
from backend.models import Blog, Role, User, db

cache = app.cache

api = Api(prefix='/api')

blog_fields = {
    'id' : fields.Integer,
    'title' : fields.String,
    'caption' : fields.String,
    'image_url' : fields.String,
    'user_id' : fields.Integer,
    'timestamp' : fields.DateTime,
    'author.email' : fields.String,
}

class BlogAPI(Resource):

    @auth_required('token')
    @cache.memoize(timeout = 5)
    @marshal_with(blog_fields)
    def get(self, blog_id):
        blog = Blog.query.get(blog_id)

        if not blog:
            return {"message" : "not found"}, 404
        return blog
    
    @auth_required('token')
    def delete(self, blog_id):

        blog = Blog.query.get(blog_id)

        if not blog:
            return {"message" : "not found"}, 404
        
        if blog.user_id == current_user.id:

            db.session.delete(blog)
            db.session.commit()
        else:
            return {"message" : "not valid user"}, 403
        

class BlogListAPI(Resource):

    @auth_required('token')
    @cache.cached(timeout = 5, key_prefix = "blog_list")
    @marshal_with(blog_fields)
    def get(self ):
        blogs = Blog.query.all()
        return blogs
    
    @auth_required('token')
    def post(self):
        data = request.get_json()
        title = data.get('title')
        caption = data.get('caption')
        image_url = data.get('image_url')

        blog = Blog(title = title, caption = caption, image_url = image_url, user_id = current_user.id)

        db.session.add(blog)
        db.session.commit()
        return jsonify({'message' : 'blog created'})


# user list api

user_list_fields = {
    'id' : fields.Integer,
    'email' : fields.String,
    'num_following' : fields.Integer,
    'num_followed' : fields.Integer,
    'num_post' : fields.Integer,
}

class UserListAPI(Resource):

    # search functionality
    # query parameters url....?key=value&key2=value2
    @marshal_with(user_list_fields)
    def get(self):

        query = request.args.get('query')

        if query:
            users = User.query.join(User.roles).filter(
                Role.name == 'user',
                User.active == True,
                User.email.ilike(f'%{query}%')
            ).all()
        else :
            users = User.query.join(User.roles).filter(Role.name == 'user', User.active == True).all()

        return users


user_fields  = {
    'id' : fields.Integer,
    'email' : fields.String,
    'num_following' : fields.Integer,
    'num_followed' : fields.Integer,
    'num_post' : fields.Integer,
    'blogs' : fields.List(fields.Nested(blog_fields))
}


class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.get(user_id)
        return user

class FeedAPI(Resource):

    @auth_required('token')
    @marshal_with(blog_fields)
    def get(self):
        followed_ids = [ followed.id for followed in current_user.followed]
        blogs = Blog.query.filter(Blog.user_id.in_(followed_ids)).all()
        if not blogs:
            return {'message' : 'no posts from followed users'}, 200
        return blogs


    
api.add_resource(BlogAPI, '/blogs/<int:blog_id>')
api.add_resource(BlogListAPI,'/blogs')
api.add_resource(UserListAPI, '/users')
api.add_resource(UserAPI, '/users/<int:user_id>')
api.add_resource(FeedAPI, '/feed')