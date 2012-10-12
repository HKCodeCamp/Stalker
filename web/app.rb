require 'sinatra'
require "sinatra/reloader" if development?

set :root, File.dirname(__FILE__)
set :static, true
set :views, settings.root + '/views'

get '/' do
  @title = "currently stalked..."
  erb :index, :layout => :layout
end

get '/search' do
  @title = "find a target..."
  erb :search, :layout => :layout
end

get '/detail/:id' do
  @title = "~CELEB NAME~"
  erb :detail, :layout => :layout
end

get '/profile/:id' do
  @title = "my profile"
  erb :profile, :layout => :layout
end

get '/stalk' do
  @title = "found a target..."
  erb :stalk, :layout => :layout
end