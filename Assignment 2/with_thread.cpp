#include<fstream>
#include<thread>
#include<bits/stdc++.h>
using namespace std;
vector<int> v;
vector<int> col_size;
vector<int> p;
bool sort_=false;
struct R
{
	vector<pair<long long int,long long int>> rr;
	vector<int >index;
};
void r_metadata()
{
	ifstream fin;
	fin.open("metadata.txt");
	int c=0;
	string s;
	while(getline(fin,s))
	{
		string p="";
		bool k=false;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]==',')
			{
				k=true;
			}
			else if(k)
			p+=s[i];
		}
		col_size.push_back(stoi(p));
	}
	fin.close();	
}
bool cmp(string a,string b)
{
	string h;
	map<long long int,string> m1,m2;
	int c=1;
	int m=0;
	for(int i=0;i<a.length();i++)
	{
		h="";
		for(int j=0;j<col_size[m];j++)
		{
			h+=a[i];
			i++;
		}
		m1[c]=h;
		i+=1;
		m++;
		c++;
	}
	c=1;
	m=0;
	for(int i=0;i<b.length();i++)
	{
		h="";
		for(int j=0;j<col_size[m];j++)
		{
			h+=b[i];
			i++;
		}
		m2[c]=h;
		i+=1;
		m++;
		c++;
	}
	string s1="",s2="";
	for(int i=0;i<v.size();i++)
	{
		if(i+1==v.size())
		s1=s1+m1[v[i]];
		else
		s1=s1+m1[v[i]]+" ";
	}
	for(int i=0;i<v.size();i++)
	{
		if(i+1==v.size())
		{
			s2=s2+m2[v[i]];
		}
		else
		s2=s2+m2[v[i]]+" ";
	}
	vector<string>g(2);
	g[0]=s1;
	g[1]=s2;
	sort(g.begin(),g.end());
	if(g[0]==s1)
	{
		if(!sort_)
		return true;
		else
		return false;
	}
	if(!sort_)
	return false;
	else
	return true;
}
void compute(R st)
{
	int i=0;
	ifstream fin;
	fin.open("input.txt");
	for(auto it=st.rr.begin();it!=st.rr.end();it++,i++)
	{
		fin.seekg(((*it).first)*100,ios::beg);
		int s=(*it).first;
		vector<string> rd;
		while(s<(((*it).second)))
		{
			string ss;
			if(getline(fin,ss))
			{			
				rd.push_back(ss);
			}
			s++;
		}
		sort(rd.begin(),rd.end(),cmp);
		cout<<"Sublist Sort: "<<st.index[i]+1<<" "<<"Sublist Sort: "<<rd.size()<<endl;
		ofstream fout;
		fout.open(to_string(st.index[i]));
		vector<string>::iterator it1;
		for(it1=rd.begin();it1!=rd.end();it1++)
		{
			fout<<*it1<<"\n";
		}
		fout.close();
	}
	fin.close();
}
class heap
{  
public:
   string x; 
   long long int y;
   heap(){} 
   heap(string x, long long int y) 
   { 
      this->x = x; 
      this->y = y; 
   } 
   string getX() const { return x; } 
   long long int getY() const { return y; } 
}; 
class myComparator 
{ 
public: 
    int operator() (const heap & p1, const heap & p2) 
    { 
	string a=p1.x;
	string b=p2.x;
	string h;
	map<int,string> m1,m2;
	int c=1,m=0;
	for(int i=0;i<a.length();i++)
	{
		h="";
		for(int j=0;j<col_size[m];j++)
		{
			h+=a[i];
			i++;
		}
		m1[c]=h;
		i+=1;
		m++;
		c++;
	}
	c=1;
	m=0;
	for(int i=0;i<b.length();i++)
	{
		h="";
		for(int j=0;j<col_size[m];j++)
		{
			h+=b[i];
			i++;
		}
		m2[c]=h;
		i+=1;
		m++;
		c++;
	}
	string s1="",s2="";
	for(int i=0;i<v.size();i++)
	{
		if(i+1==v.size())
		s1=s1+m1[v[i]];
		else
		s1=s1+m1[v[i]]+" ";
	}
	for(int i=0;i<v.size();i++)
	{
		if(i+1==v.size())
		{
			s2=s2+m2[v[i]];
		}
		else
		s2=s2+m2[v[i]]+" ";
	}
	vector<string>g(2);
	g[0]=s1;
	g[1]=s2;
	sort(g.begin(),g.end());
	if(g[0]==s1)
	{
		if(!sort_)
		return false;
		else
		return true;
	}
	if(!sort_)
	return true;
	else
	return false;
    } 
};
void final_output(int n,string out_file)
{
	vector<ifstream> f(n);
	fstream fout;
	fout.open(out_file,fstream::out);
	priority_queue <heap, vector<heap>, myComparator > q;
	cout<<"Sorting....\n\n";
	for(int i=0;i<n;i++)
	{
		heap a;
		f[i].open(to_string(i));
		a.y=i;
		getline(f[i],a.x);
		q.push(a);
	}
	cout<<"Writing to disk\n\n";
	while(!q.empty())
	{
		fout<<q.top().x<<"\n";
		long long int x=q.top().y;
		q.pop();
		string k;
		if(getline(f[x],k))
		{
			heap a(k,x);
			q.push(a);
		}
	}
	for(int i=0;i<n;i++)
	{
		f[i].close();
	}
	char pp[10]={0};
	for(int i=0;i<n;i++)
	{
		sprintf(pp,"%d", i);
		remove(pp);
	}
	fout.close();
	cout<<"completed execution\n\n";
}
long long int get_row(string inputfile)
{
	ifstream fin;
	fin.open(inputfile);
	int c=0;
	string s;
	while(getline(fin,s))
		c++;
	fin.close();	
	return c;
}
long long int get_column(string inputfile)
{
	ifstream fin;
	fin.open(inputfile);
	int c=0;
	string s;
	getline(fin,s);
	stringstream str(s);
	while(str>>s)
		c++;
	fin.close();	
	return c;
}
int main(int argc, char *argv[])
{
	r_metadata();
	long long int sum1=0;
	for(auto it=col_size.begin();it!=col_size.end();it++)
		sum1+=(*it);
	string inputfile;
	if(argc>=5)
		inputfile=argv[1];
	else
	{
		cout<<"error\n";
		exit(0);
	}		
	long long int no_row = get_row(inputfile);
	string out_file(argv[2]);
	int no_column = get_column(inputfile);
	for(int i=6;i<argc;i++)
	{
		string s(argv[i]);
		s.erase(s.begin());
		v.push_back(stoi(s));
	}	
	long long int x=stoi(argv[3]);
	long long int total_thread=stoi(argv[4]);
	if(!total_thread)
	{
		cout<<"thread not sufficent\n";
		exit(0);
	}
	long long int total_data=(x*1024*1024)/(sum1+(col_size.size()*5));
	long long int total_ =((no_row)/total_data);
	if((no_row)%total_data!=0)
	total_++;
	long long int sum=0;
	ifstream fin;
	fin.open(inputfile);
	int c=0;
	cout<<"start execution"<<endl;	
	cout<<"running Phase-"<<1<<endl;
	cout<<"Number of sub-files (splits): "<<total_<<endl;
	long long int block_size= total_data;
	long long int st=0;
	long long int temp=total_,k=0;	
	string sot=(argv[5]);
	if(sot=="desc")
		sort_=true;
	while(temp>0)
	{
		if(k>=total_thread)
		p[k%total_thread]++;
		else
		p.push_back(1);
		temp--;
		k++;
	}
	thread *t[total_thread];
	k=false;
	int y=0;
	clock_t t1,t2;
	t1 = clock();
	for(int i=0;i<min(total_thread,total_);i++)
	{
		R range;
		for(int j=0;j<p[i];j++)
		{
			range.rr.push_back({st,block_size});
			range.index.push_back(y);
			y++;
			if((block_size+total_data)>=no_row)
			{
				block_size=no_row;
				block_size+=total_data;
				k=true;
			}
			else
			{
				block_size+=total_data;
			}
			st=st+total_data;
		}
		cout<<"sorting #"<<i+1<<" thread"<<endl;
		t[i]= new thread(compute,range);
	}
	for(int i=0;i<min(total_thread,total_);i++)
	t[i]->join();
	cout<<"running phase-2"<<endl<<endl;
	final_output(total_,out_file);
	t2 = clock();
	cout << "\n\n\nProcessor time taken:: "<< (float)(t2-t1)/CLOCKS_PER_SEC << " seconds" << endl;
	fin.close();
return 0;
}
