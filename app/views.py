from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass


@dataclass
class Project:
    name: str           #project name
    description: str    #what the thing does
    people: list[str]   #people who worked on the project
    link: str           #link to github repo


#['Darrell','Conner','Kaleigh','Blair','Wyatt','Mina','Jay','Joshua']
#['Jordan','Joby','Aj','Micah','Caleb']
#for creating data



def homePage (request :HttpRequest)->render:
    context = {'projects':[
        Project(
            'portfolio',
            'A collection of all of our project and our star worker.',
            ['Owen','Jeremiah','Nick','Ab','Abigail'],
            'https://github.com/Aj-Gilliland/Portfolio'),
        Project(
            'BCCA team viewer',
            'This is a collection of information of our different teams and what they do.',
            ['Kayleah','Adrian','Bryce','Big John','Blaine'],
            'https://github.com/Aj-Gilliland/Bcca-team-viewer')
    ]}
    return render(request, "home.html", context)

def details (request:HttpRequest, projectNum:int )->render:
    bigList = [
        Project(
            'portfolio',
            'A collection of all of our project and our star worker.',
            ['Owen','Jeremiah','Nick','Ab','Abigail'],
            'https://github.com/Aj-Gilliland/Portfolio'),
        Project(
            'BCCA team viewer',
            'This is a collection of information of our different teams and what they do.',
            ['Kayleah','Adrian','Bryce','Big John','Blaine'],
            'https://github.com/Aj-Gilliland/Bcca-team-viewer')
    ]

    context = {
        'project':bigList[projectNum-1]}
    
    return render(request, "secondary.html", context)








