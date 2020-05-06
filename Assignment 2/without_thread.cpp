#include<fstream>
#include<bits/stdc++.h>
using namespace std;
vector<string> rd;
vector<long long int> v;
vector<long long int> col_size;
bool sort_=false;
void r_metadata()
{
	ifstream fin;
	fin.open("metadata.txt");
	long long int c=0;
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
		col_size.push_back(stol(p));
	}
	fin.close();	
}
bool cmp(string a,string b)
{
	string h;
	map<long long int,string> m1,m2;
	long long int c=1;
	long long int m=0;
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
	map<long long int,string> m1,m2;
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
	if(argc>=2)
		inputfile=argv[1];		
	long long int no_row = get_row(inputfile);
	string out_file(argv[2]);
	long long int no_column = get_column(out_file);
	for(int i=5;i<argc;i++)
	{
		string s(argv[i]);
		s.erase(s.begin());
		v.push_back(stoi(s));
	}	
	long long int x=stoi(argv[3]);
	string sot=(argv[4]);
	if(sot=="desc")
		sort_=true;
	long long int total_data=(x*1024*1024)/(sum1+(col_size.size()*5));
	long long int total_ = (no_row)/(total_data);
	if((no_row)%(total_data)!=0)
		total_+=1;
	long long int sum=0;
	ifstream fin;
	fin.open(inputfile);
	cout<<"start execution"<<endl;	
	cout<<"running Phase-"<<1<<endl;
	cout<<"Number of sub-files (splits): "<<total_<<endl;
	clock_t t1,t2;
	t1 = clock();
	for(int i=0;i<total_;i++)
	{
		long long int c=0;
		while((c<total_data)&&(sum<(no_row)))
		{
			string s;
			if(getline(fin,s))
			{			
				c++;
				rd.push_back(s);
				sum++;
			}
		}
		sort(rd.begin(),rd.end(),cmp);
		cout<<"sorting #"<<i+1<<" sublist"<<endl;
		ofstream fout;
		fout.open(to_string(i));
		vector<string>::iterator it;
		for(it=rd.begin();it!=rd.end();it++)
		{
			fout<<*it<<"\n";
		}
		cout<<"Writing to disk #"<<i+1<<endl;
		rd.clear();
		fout.close();
	}
	cout<<"running phase-2"<<endl<<endl;
	final_output(total_,out_file);
	t2 = clock();
	cout << "\n\n\nProcessor time taken:: "<< (float)(t2-t1)/CLOCKS_PER_SEC << " seconds" << endl;
	fin.close();
}
