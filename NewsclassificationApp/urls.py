from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("UserLogin", views.UserLogin, name="UserLogin"),
	       path("Login.html", views.Login, name="Login"),
	       path("Register.html", views.Register, name="Register"),
	       path("RegisterAction", views.RegisterAction, name="RegisterAction"),	       
	       path("logout", views.logout, name="logout"),
	       path("UploadDataset.html", views.UploadDataset, name="UploadDataset"),
	       path("UploadDatasetAction", views.UploadDatasetAction, name="UploadDatasetAction"),	 
	       path("TrainModels", views.TrainModels, name="TrainModels"),	 
	       path("ClassifyNews.html", views.ClassifyNews, name="ClassifyNews"),
	       path("ClassifyNewsAction", views.ClassifyNewsAction, name="ClassifyNewsAction"),	 
]