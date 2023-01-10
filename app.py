from flask import Flask, render_template, request, url_for, flash, redirect
import csv



header = ['From','To']
Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar","Mahakavi Kuvempu Road", "Srirampura","Sampige Road","Majestic","Chikpete","Krishna Rajendra Market","National College","Lalbagh Botanical Garden","South End Circle","Jayanagar","Rashtreeya Vidyalaya Road","Banashankari","Jaya Prakash Nagar","Yelachenahalli","Konanakunte Cross","Doddakallasandra","Vajarahalli","Thalaghattapura","Silk Institute"]
Purple_line = ["Kengeri","Kengeri Bus Terminal","Pattanagere","Jnanabharathi","Rajarajeshwari Nagar","Nayandahalli","Mysuru Road","Deepanjali Nagara","Attiguppe"," Vijayanagara","Balagangadhara Natha Swamiji HOS","Magadi Road","City Railway Station","Majestic","Sir M. Visveshwaraya Station","Dr BR Ambedkar Vidhana Soudha","Cubbon Park Sri Chamarajendra Park","MG Road","Trinity","Halasuru","Indiranagara","Swami Vivekananda Road","Baiyappanahalli"]
station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]


app = Flask(__name__)
def price_route(from_station, to_station):

    Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar","Mahakavi Kuvempu Road", "Srirampura","Sampige Road","Majestic","Chikpete","Krishna Rajendra Market","National College","Lalbagh Botanical Garden","South End Circle","Jayanagar","Rashtreeya Vidyalaya Road","Banashankari","Jaya Prakash Nagar","Yelachenahalli","Konanakunte Cross","Doddakallasandra","Vajarahalli","Thalaghattapura","Silk Institute"]
    Purple_line = ["Kengeri","Kengeri Bus Terminal","Pattanagere","Jnanabharathi","Rajarajeshwari Nagar","Nayandahalli","Mysuru Road","Deepanjali Nagara","Attiguppe"," Vijayanagara","Balagangadhara Natha Swamiji HOS","Magadi Road","City Railway Station","Majestic","Sir M. Visveshwaraya Station","Dr BR Ambedkar Vidhana Soudha","Cubbon Park Sri Chamarajendra Park","MG Road","Trinity","Halasuru","Indiranagara","Swami Vivekananda Road","Baiyappanahalli"]
    station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road", "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic","Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park", "MG Road","Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

    print('sdgsdfgfdgdfgfgd')
    no_of_stops=0
    print(from_station)
    print(to_station)
    # --- No of Stops ---
    if ((from_station in Green_line and to_station in Green_line) or (from_station in Purple_line and to_station in Purple_line)):
        no_of_stops = abs(station_name.index(from_station) - station_name.index(to_station)) - 1

    if (from_station in Green_line and to_station in Purple_line):
        no_of_stops = abs( abs(Green_line.index("Majestic") - Green_line.index(from_station)) + abs(Purple_line.index("Majestic") - Purple_line.index(to_station)) -1 )

    if (from_station in Purple_line and to_station in Green_line):
        no_of_stops = abs( abs(Purple_line.index("Majestic") - Purple_line.index(from_station)) + abs(Green_line.index("Majestic") - Green_line.index(to_station)) -1 )
    
    print(no_of_stops)

    if no_of_stops == 0:
        price = 5
    if no_of_stops == 1:
        price = 9
    if no_of_stops == 2:
        price = 14
    if no_of_stops == 3:
        price = 18
    if no_of_stops > 3:
        price = 18 + (no_of_stops - 3)*2
    if to_station == "Majestic":
        price = price + 1
    
    print(price)
    

    # --- Route Selection --- 
    route = []
    to_reverse = []

    if ((from_station in Green_line and to_station in Green_line) or (from_station in Purple_line and to_station in Purple_line)):
        if station_name.index(from_station) < station_name.index(to_station):
            for i in range((station_name.index(from_station)), (station_name.index(to_station)+1)):
                route.append(station_name[i])

        if station_name.index(from_station) > station_name.index(to_station):
            for i in range((station_name.index(from_station)), (station_name.index(to_station)-1), -1):
                route.append(station_name[i])
    
    if (from_station in Green_line and to_station in Purple_line):
        if Green_line.index(from_station) < Green_line.index("Majestic"):
            for i in range((Green_line.index(from_station)), Green_line.index("Majestic")):
                route.append(Green_line[i])
        
        if Green_line.index(from_station) > Green_line.index("Majestic"):
            for i in range((Green_line.index(from_station)), Green_line.index("Majestic"), -1):
                route.append(Green_line[i])

        if Purple_line.index(to_station) < Purple_line.index("Majestic"):
            for i in range((Purple_line.index(to_station)), (Purple_line.index("Majestic")+1)):
                to_reverse.append(Purple_line[i])
        
        if Purple_line.index(to_station) > Purple_line.index("Majestic"):
            for i in range((Purple_line.index(to_station)), (Purple_line.index("Majestic")-1), -1):
                to_reverse.append(Purple_line[i])
    
    if (from_station in Purple_line and to_station in Green_line):
        if Purple_line.index(from_station) < Purple_line.index("Majestic"):
            for i in range((Purple_line.index(from_station)), Purple_line.index("Majestic")):
                route.append(Purple_line[i])
        
        if Purple_line.index(from_station) > Purple_line.index("Majestic"):
            for i in range((Purple_line.index(from_station)), Purple_line.index("Majestic"), -1):
                route.append(Purple_line[i])

        if Green_line.index(to_station) < Green_line.index("Majestic"):
            for i in range((Green_line.index(to_station)), (Green_line.index("Majestic")+1)):
                to_reverse.append(Green_line[i])
        
        if Green_line.index(to_station) > Green_line.index("Majestic"):
            for i in range((Green_line.index(to_station)), (Green_line.index("Majestic")-1), -1):
                to_reverse.append(Green_line[i])

    
    to_reverse.reverse()
    route = route + to_reverse
    print(route)
    return [price,route]

def stationoperations(from_station,to_station):
    print(from_station)
    Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar","Mahakavi Kuvempu Road", "Srirampura","Sampige Road","Majestic","Chikpete","Krishna Rajendra Market","National College","Lalbagh Botanical Garden","South End Circle","Jayanagar","Rashtreeya Vidyalaya Road","Banashankari","Jaya Prakash Nagar","Yelachenahalli","Konanakunte Cross","Doddakallasandra","Vajarahalli","Thalaghattapura","Silk Institute"]
    Purple_line = ["Kengeri","Kengeri Bus Terminal","Pattanagere","Jnanabharathi","Rajarajeshwari Nagar","Nayandahalli","Mysuru Road","Deepanjali Nagara","Attiguppe"," Vijayanagara","Balagangadhara Natha Swamiji HOS","Magadi Road","City Railway Station","Majestic","Sir M. Visveshwaraya Station","Dr BR Ambedkar Vidhana Soudha","Cubbon Park Sri Chamarajendra Park","MG Road","Trinity","Halasuru","Indiranagara","Swami Vivekananda Road","Baiyappanahalli"]


@app.route('/',methods=('GET','POST'))
def index():
    price=0
    route=[]

    if request.method=="POST":
        from_station = request.form['from']
        to_station = request.form['to']
        with open('passengers.csv','a',encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([from_station,to_station])
        if from_station==to_station:
            return render_template("index.html",price="Sorry to and from station cant be same",route=[])

        funv = price_route(from_station,to_station)
        price = funv[0]
        route = funv[1]


        print(price,"\n",route)
        
    return render_template("index.html",price="Price : "+str(price),route=route)


@app.route('/admin',methods=('GET','POST'))
def table():
    from_s=[]
    to_s=[]
    with open('passengers.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    for i in data:
        from_s.append(i[0])
        to_s.append(i[1])
    from_s_dict = {}
    to_s_dict = {}
    for item in from_s:
        if item in from_s_dict:
            from_s_dict[item] += 1
        else:
            from_s_dict[item] = 1
    
    for item in to_s:
        if item in to_s_dict:
            to_s_dict[item] += 1
        else:
            to_s_dict[item] = 1
    return render_template("table.html",data=data,from_s_dict=from_s_dict,to_s_dict=to_s_dict)


if __name__ == "__main__":
    app.run(debug=True)
    



    


# def price_route(from_station, to_station):
#     print('sdgsdfgfdgdfgfgd')
#     # --- No of Stops ---
#     if ((from_station in Green_line and to_station in Green_line) or (from_station in Purple_line and to_station in Purple_line)):
#         no_of_stops = abs(station_name.index(from_station) - station_name.index(to_station)) - 1

#     if (to_station in Green_line and from_station in Purple_line):
#         no_of_stops = abs( abs(Green_line.index("Majestic") - Green_line.index(from_station)) + abs(Purple_line.index("Majestic") - Purple_line.index()) -1 )

#     if (from_station in Purple_line and to_station in Green_line):
#         no_of_stops = abs( abs(Purple_line.index("Majestic") - Purple_line.index(from_station)) + abs(Green_line.index("Majestic") - Green_line.index(to_station)) -1 )

#     if no_of_stops == 0:
#         price = 5
#     if no_of_stops == 1:
#         price = 9
#     if no_of_stops == 2:
#         price = 14
#     if no_of_stops == 3:
#         price = 18
#     if no_of_stops > 3:
#         price = 18 + (no_of_stops - 3)*2
#     if to_station == "Majestic":
#         price = price + 1

#     # --- Route Selection --- 
#     route = []
#     to_reverse = []

#     if ((from_station in Green_line and to_station in Green_line) or from_station in Purple_line and to_station in Purple_line):
#         if station_name.index(from_station) < station_name.index(to_station):
#             for i in range((station_name.index(from_station)), (station_name.index(to_station)+1)):
#                 route.append(station_name[i])

#         if station_name.index(from_station) > station_name.index(to_station):
#             for i in range((station_name.index(from_station)), (station_name.index(to_station)-1), -1):
#                 route.append(station_name[i])
    
#     if (from_station in Green_line and to_station in Purple_line):
#         if Green_line.index(from_station) < Green_line.index("Majestic"):
#             for i in range((Green_line.index(from_station)), Green_line.index("Majestic")):
#                 route.append(Green_line[i])
        
#         if Green_line.index(from_station) > Green_line.index("Majestic"):
#             for i in range((Green_line.index(from_station)), Green_line.index("Majestic"), -1):
#                 route.append(Green_line[i])

#         if Purple_line.index(to_station) < Purple_line.index("Majestic"):
#             for i in range((Purple_line.index(to_station)), (Purple_line.index("Majestic")+1)):
#                 to_reverse.append(Purple_line[i])
        
#         if Purple_line.index(to_station) > Purple_line.index("Majestic"):
#             for i in range((Purple_line.index(to_station)), (Purple_line.index("Majestic")-1), -1):
#                 to_reverse.append(Purple_line[i])
    
#     if (from_station in Purple_line and to_station in Green_line):
#         if Purple_line.index(from_station) < Purple_line.index("Majestic"):
#             for i in range((Purple_line.index(from_station)), Purple_line.index("Majestic")):
#                 route.append(Purple_line[i])
        
#         if Purple_line.index(from_station) > Purple_line.index("Majestic"):
#             for i in range((Purple_line.index(from_station)), Purple_line.index("Majestic"), -1):
#                 route.append(Purple_line[i])

#         if Green_line.index(to_station) < Green_line.index("Majestic"):
#             for i in range((Green_line.index(to_station)), (Green_line.index("Majestic")+1)):
#                 to_reverse.append(Green_line[i])
        
#         if Green_line.index(to_station) > Green_line.index("Majestic"):
#             for i in range((Green_line.index(to_station)), (Green_line.index("Majestic")-1), -1):
#                 to_reverse.append(Green_line[i])

    
#     to_reverse.reverse()
#     route = route + to_reverse

'''

Create seprate function here with parameters to and from station.
and return the desired values.

'''
