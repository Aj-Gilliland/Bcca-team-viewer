from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass


@dataclass
class Team:
    name: str           #team name
    description: str    #what the team exist for
    duty: str           #what they do in their day to day
    people: list[str]   #people on team








def everyoneHere (request :HttpRequest)->render:
    context = {'teams':[
    Team( 
        'Community', 
        'The Community Team is tasked with planning and organizing bi-weekly events, celebrating birthdays, and coordinating school visits to external educational institutions. They are responsible for creating a positive and engaging environment for the school community, ensuring that everyone can enjoy their time at BCCA.',
        ' Plans bi-weekly events, birthdays, and school visits.',
        ['Jordan','Joby','Aj','Micah','Caleb'] ),

    Team( 
        'Documentation', 
        'Documents events at bcca ,with access to the media accounts and social pages.',
        'Film events, post, and interview students.',
        ['Darrell','Conner','Kaleigh','Blair','Wyatt','Mina','Jay','Joshua'] ),

    Team( 
        'Management', 
        'Hands out work loads and makes efforts on maintaining the student body.',
        'Oversee chores and supply levels',
        ['Owen','Jeremiah','Nick','Ab','Abigail'] ),

    Team( 
        'Procurement', 
        'Accumulates supply for things such as lunch, building maintenance, and events. ',
        'Order in bulk, drive to stores ,set out/plan lunch.',
        ['Kayleah','Adrian','Bryce','Big John','Blaine'] )
    ]}
    return render(request, "teamList.html", context)

def details (request:HttpRequest, teamNum:int )->render:
    teams = [
    Team( 
        'Community', 
        'Provides a good environment and the occasional fun time for the whole school.',
        ' Plans bi-weekly events, birthdays, and school visits.',
        ['Jordan','Joby','Aj','Micah','Caleb'] ),

    Team( 
        'Documentation', 
        'Documents events at bcca ,with access to the media accounts and social pages.',
        'Film events, post, and interview students.',
        ['Darrell','Conner','Kaleigh','Blair','Wyatt','Mina','Jay','Joshua'] ),

    Team( 
        'Management', 
        'Hands out work loads and makes efforts on maintaining the student body.',
        'Oversee chores and supply levels',
        ['Owen','Jeremiah','Nick','Ab','Abigail'] ),

    Team( 
        'Procurement', 
        'Accumulates supply for things such as lunch, building maintenance, and events. ',
        'Order in bulk, drive to stores ,set out/plan lunch.',
        ['Kayleah','Adrian','Bryce','Big John','Blaine'] )
    ]

    context = {
        'team':teams[teamNum-1]}
    
    return render(request, "details.html", context)








