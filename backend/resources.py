from flask import jsonify, request, current_app as app
from flask_restful import Api, Resource, fields, marshal_with
from flask_security import auth_required, current_user
from backend.models import Blog, db

cache = app.cache

api = Api(prefix='/api')

blog_fields = {
    'id' : fields.Integer,
    'title' : fields.String,
    'caption' : fields.String,
    'image_url' : fields.String,
    'user_id' : fields.Integer,
    'timestamp' : fields.DateTime,
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

    
api.add_resource(BlogAPI, '/blogs/<int:blog_id>')
api.add_resource(BlogListAPI,'/blogs')