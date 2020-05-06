#include<bits/stdc++.h>
#include<fstream>
using namespace std;
#define order 2
fstream fout;
struct Node 
{
	bool isleaf;
	int key[order];
	int count[order];
	int size;
	Node *child[order+1];
	Node()
	{
		isleaf=false;
		size=0;
		for(int i=0;i<order+1;i++)
			child[i] = NULL;
		for(int i=0;i<order;i++)
			count[i]=0;
		for(int i=0;i<order;i++)
			key[i]=INT_MAX;
	}
};
Node *root=NULL;
bool find(int var)
{
	Node *t=root;
	if(t==NULL)
	return false;
	while(t->isleaf==false)
	{
		for(int i=0;i<t->size;i++)
		{
			if(var == t->key[i])
			{
				t=t->child[i+1];
				break;
			}
			if(var < t->key[i])
			{
				t=t->child[i];
				break;
			}
			if(i == t->size-1)
			{
				t=t->child[i+1];
				break;
			}
		}
	}
	for(int i=0;i<t->size;i++)
	{
		if(t->key[i]==var)
		{
			return true;
		}
	}
return false;
}
int count_(int var)
{
	Node *t = root;
	while(t->isleaf==false)
	{
		for(int i=0;i<t->size;i++)
		{
			if(var == t->key[i])
			{
				t=t->child[i+1];
				break;
			}
			if(var < t->key[i])
			{
				t=t->child[i];
				break;
			}
			if(i == t->size-1)
			{
				t=t->child[i+1];
				break;
			}
		}
	}
	for(int i=0;i<t->size;i++)
	{
		if(t->key[i]==var)
		{
			return t->count[i];
		}
	}
return 0;
}
void count(int start,int end1)
{
	Node *t=root;
	if(t==NULL)
	return ;
	while(t->isleaf==false)
	{
		for(int i=0;i<t->size;i++)
		{
			if(start == t->key[i])
			{
				t=t->child[i+1];
				break;
			}
			if(start < t->key[i])
			{
				t=t->child[i];
				break;
			}
			if(i == t->size-1)
			{
				t=t->child[i+1];
				break;
			}
		}
	}
	bool s=1;
	int x=0;
	while(s)
	{
		for(int i=0;i<t->size;i++)
		{
			if(t->key[i]>=start && t->key[i] <=end1)
			{
				x+=t->count[i];
			}
			if(t->key[i] >=end1)
			{s=false;break;}
		}
		if(s && t->child[1] !=NULL)
		t=t->child[1];
		else if(s && t->child[2] !=NULL)
		t=t->child[2];
		else
		break;
	}
	fout<<x<<"\n";
}
Node *parent(Node *t,Node *leaf)
{
	Node *p;
	if(t->isleaf==true || t->child[0]->isleaf== true)
	return NULL;
	for(int i=0;i<t->size+1;i++)
	{
		if(t->child[i]==leaf)
		{
			return t;
		}
		else
		{
			p=parent(t->child[i],leaf);
			if(p!=NULL)
			return p; 	
		}
	}
return p;
}
void insertI(int var,Node *t,Node *leaf)
{
	if(t->size < order)
	{
		int i=0;
		while(var > t->key[i] && i < t->size)
			i++;
		for(int j=t->size;j>i;j--)
		{
			t->key[j]=t->key[j-1];
		}
		for(int j=t->size+1;j>i+1;j--)
		{
			t->child[j]=t->child[j-1];
		}
		t->key[i]=var;
		t->size+=1;
		t->child[i+1]=leaf;
	}
	else
	{
		int temp[order+1];
		Node *temp_c[order+2];
		for(int i=0;i<order;i++)
			temp[i]=t->key[i];
		for(int i=0;i<order+1;i++)
			temp_c[i]=t->child[i];
		int i=0;
		while(var > temp[i] && i < order)
			i++;
		for(int j=order;j>i;j--)
		{
			temp[j]=t->key[j-1];
		}
		for(int j=order+1;j>i+1;j--)
		{
			temp_c[j]=t->child[j-1];
		}
		temp[i]=var;
		temp_c[i+1]=leaf;
		Node *p = new Node;
		p->isleaf=false;
		t->size =1;
		p->size= 1;
		for(int i=0;i<=t->size;i++)
		{
			t->key[i]=temp[i];
		}
		for(int i=0;i<=t->size+1;i++)
		{
			t->child[i]=temp_c[i];
		}
		for(int i=0,j=t->size+1;i<p->size;i++,j++)
		{
			p->key[i]=temp[j];
		}
		for(int i=0,j=t->size+1;i<p->size+1;i++,j++)
		{
			p->child[i]=temp_c[j];
		}
		if(t == root)
		{
			Node *t_1 =new Node;
			t_1->key[0]=temp[1];
			t_1->child[0]=t;
			t_1->child[1]=p;
			t_1->size=1;
			root=t_1;
			root->isleaf=false;
		}
		else
		{
			Node *tt=root;
			Node *pp=parent(tt,t);
			insertI(t->key[1],pp,p);
		}
	}
}


void insert(int var)
{
	if(root==NULL)
	{
		root = new Node();
		root->size=1;
		root->key[0]=var;
		root->isleaf = true;
		root->count[0]=1;
	}
	else
	{	
		Node *t = root;
		Node *p;
		while(t->isleaf==false)
		{
			p=t;
			for(int i=0;i<t->size;i++)
			{
				if(var == t->key[i])
				{
					t=t->child[i+1];
					break;
				}
				if(var < t->key[i])
				{
					t=t->child[i];
					break;
				}
				if(i == t->size-1)
				{
					t=t->child[i+1];
					break;
				}
			}
		}
		for(int i=0;i<t->size;i++)
		{
			if(t->key[i]==var)
			{
				t->count[i]++;
				return;
			}
		}
		if(t->size < order)
		{
			int i=0;
			while(var > t->key[i] && i < t->size)
				i++;
			for(int j=t->size;j>i;j--)
			{
				t->key[j]=t->key[j-1];
				t->count[j]=t->count[j-1];
			}
			t->key[i]=var;
			t->size+=1;
			t->count[i]=1;
			t->child[t->size]=t->child[t->size-1];
			t->child[t->size-1]=NULL;
		}
		else
		{
			Node *leaf=new Node;
			int temp[order+1];
			int temp_count[order+1]={0};
			for(int i=0;i<order;i++)
			{
				temp[i]=t->key[i];
				temp_count[i]=t->count[i];
			}
			
			int i=0;
			while(var > temp[i] && i < order)
				i++;
			for(int j=order;j>i;j--)
			{
				temp[j]=temp[j-1];
				temp_count[j]=temp_count[j-1];
			}
			temp[i]=var;
			temp_count[i]=1;
			t->size=1;
			leaf->size=2;
			
			leaf->isleaf=true;

			t->child[t->size]=leaf;
			leaf->child[leaf->size]=t->child[order];
			t->child[order]=NULL;
			

			for(int i=0;i<t->size;i++)
			{
				t->key[i]=temp[i];
				t->count[i]=temp_count[i];
			}
			for(int i=t->size;i<order;i++)
			{
				t->count[i]=0;
			}
			for(int i=0,j=t->size;i<leaf->size;i++,j++)
			{
				leaf->key[i]=temp[j];
				leaf->count[i]=temp_count[j];
			}	
			for(int i=leaf->size;i<order;i++)
			{
				leaf->count[i]=0;
			}
			if(t == root)
			{
				Node *p = new Node;
				p->child[0]=t;
				p->child[1]=leaf;
				p->size=1;
				p->isleaf=false;
				p->key[0]=leaf->key[0];
				root=p;
			}
			else
			{
				insertI(leaf->key[0],p,leaf);
			}		
		}
	}
}
int main()
{
	ifstream fin;
	fin.open("sampleInput.txt");
	fout.open("output.txt",fstream::out);
	string s;
	while(getline(fin,s))
	{
		stringstream str(s);
		string ss="";
		str >> ss;
		if(ss=="INSERT")
		{
			str>>ss;
			insert(stoi(ss));
		}
		else if(ss=="FIND")
		{
			str >>ss;
			if(find(stoi(ss)))
			{
				fout<<"YES"<<"\n";
			}
			else
			{
				fout<<"NO"<<"\n";
			}
		}
		else if(ss=="COUNT")
		{
			str >>ss;
			int x=count_(stoi(ss));
			fout<<x<<"\n";
		}
		else if(ss=="RANGE")
		{
			string f;
			str >>ss;
			str>>f;
			count(stoi(ss),stoi(f));
		}
		
	}
	fin.close();	
	fout.close();
return 0;
}
