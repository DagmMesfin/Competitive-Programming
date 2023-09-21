#include<bits/stdc++.h>

using namespace std;

struct loginfo{
	string name;
	string pass;
};


void signup(){
	string username; string pass;
	system("CLS");
	cout<<"\t\t\t\tRegister well!!\n";
	cout<<"\t\t\t\tusername: \n";
	cin>>username;
	cout<<"\t\t\t\tpassword: \n";
	cin>>pass;
	fstream sign;
	sign.open("UserData.csv", ios::in | ios::app);
	sign<<username<<","<<pass<<endl;
	sign.close();
	cout<<"\t\t\t Signup Success!!!";
	system("pause");
}

void login(){
	string username, password;
	bool accessgranted = false;
	log:
	system("CLS");
	cout<<"Username: ";
	cin>>username;
	cout<<"Password: ";
	cin>>password;
	
	ifstream file("UserData.csv");
	vector<string> row;
	vector<loginfo> info;

	string line, word;
	while (getline(file, line)) // to get the line of the csv row
	{
		row.clear();
		stringstream ss(line);

		while (getline(ss, word, ',')) // to get the datas separarated by the comma delimiter
		{
			row.push_back(word); // adding the datas to the row vector
		}

		loginfo d; // creating a structure and giving row values to the properties
		d.name = row[0];
		d.pass = row[1];

		info.push_back(d); // adding the structure to the output structure vector
	}

	file.close();
	for(int i=0; i<info.size(); i++){
		if(username == info[i].name){
			if(password == info[i].pass){
				accessgranted = true;
				break;
	}
}
}

 	if(accessgranted){
 		cout<<"Access Granted!!!\n";
	 }
	 else{
	 	cout<<"User Name or password is not correct! Try again!";
	 	goto log;
	 }
	 system("pause");
}


int main(){
	int serv;
	menu:
	cout<<"\t\t\tWhat do you wanna do?"<<endl;
	cout<<" \t\t\t\t1. Login"<<endl;
	cout<<" \t\t\t\t2. Signup"<<endl;
	cin>>serv;
	switch(serv){
		case 1:
			login();
			break;
		case 2:
			signup();
			goto menu;
			
	}
	system("CLS");
	cout<<"Welcome to the GUI!!! \n Thank you for visiting!!!\n";
	system("pause");
	
}
