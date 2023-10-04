from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from deep_web.utility import Connection, handler, client, activate_sheet, run_in_loop
from telethon import TelegramClient, sync, events



class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        activate_sheet()
        handler(events)
        client.run_until_disconnected()
        return render(request, "home.html")


