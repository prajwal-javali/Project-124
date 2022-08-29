from flask import Flask ,request , jsonify


# creating the object for the Flask Class
app = Flask(__name__)


tasks = [
    {
       'id' : 1,
        'title' : 'working on a new video game code'
    },
    {
        'id' : 2,
        'title' : "building something out of lego"
    }
]

# defining the route for the func which will add a new task
@app.route("/world" , methods=["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the Data!"
        }) 

    task = {
        'id' : tasks[-1]['id'] + 1 ,
        'title' : "making music"
    }

    tasks.append(task)
    return jsonify({
        "status" : "success",
        "message" : "task added successfully"
    })


# code to define the route for displaying the tasks
@app.route("/getData") 

def returnTask():
    return jsonify({
        "data" : tasks
    })



# route() tells the web application about the endpoint of the URL, associated with the func ---> helloWorld()
@app.route("/")

def helloWorld():
    return "Hello World!"



# run the web
if __name__=="__main__":
    app.run()



{
        'title' : "Do Homework"
}


# -----------------------------------------------------------------

# The GET Method -
# GET is used to request data from a
# specified resource. When you access
# a website’s page, your browser
# makes a get request to your API and
# your API is returning the front-end
# that is displayed in the browser.


# The POST Method -
# POST is used to send data to the
# server to create/update a resource.


# The PUT Method -
# PUT is used to send data to a server
# to create / update a resource.


# The DELETE Method -
# DELETE is used to delete a resource.



# GET is the default method


# Difference between POST and PUT

# The basic difference between PUT
# and POST is that a POST request is
# when you can create multiple copies
# of the same resource.

# A PUT request, on the other hand
# means that you want to create only
# one copy of the resource, i.e. Signing
# Up a unique user



# ------- 0   1   2   3 ---> positive indexing

# x =    23  34  45  89

# <----  -4  -3  -2  -1 ----- negative  indexing  ~ x[-1] --> 89

