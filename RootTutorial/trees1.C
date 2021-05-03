// The TTree class is what makes Root truly useful
// TNtuple and TNtupleD are simplified TTrees.

// Chris Jillings 2020-05-02

// What makes a tree useful is each "column" can be an arbitrarily complicated object.
// These are called TBranch

TTree* tree = NULL;

TH1F* h1 = NULL;
TH1F* h2 = NULL;

Double_t x;
Int_t i;

struct my_struct {
  Int_t j;
  Float_t array[4];
};
my_struct* msptr = NULL;

TFile* fout;

void MakeTree() {
  h1 = new TH1F("h1","H1",200,-10,10);
  h2 = new TH1F("h2","H2",400,-20,20);

  fout = new TFile("fouttree.root","RECREATE");
  msptr = new my_struct;
  tree = new TTree("treename","Tree Title");
  tree->Branch("xbranch", &x, "x/D");
  tree->Branch("ibranch", &i, "i/I");
  tree->Branch("struct_branch", msptr, "j/I:array[4]/F");    // pointer
  tree->Branch("h1_branch", "TH1F", &h1); // Pointer to pointer
  tree->Branch("h2_branch", "TH1F", &h2); // pointer to pointer



}


void FillTree(Int_t aN) {
  h1->Reset();
  h2->Reset();
  int iloop;
  for( iloop=0 ; iloop<aN ; iloop++ ) {
    i = iloop;
    x = 1.1*iloop;
    msptr->j = 2*iloop;
    for( int jloop=0 ; jloop<4 ; jloop++ ) msptr->array[jloop] = 10*iloop+jloop;
    h1->FillRandom("gaus", 100*(i+1));
    h2->FillRandom("gaus", 200*(i+1));
    tree->Fill();
  }
  fout->Write();
  fout->Close();
}


// Read tree using TBrowser - explain TBrowser
// click on xbranch - 5 entries
// click on i branch - histogram looks different, but still 5 entries
// click on structbranch j
// click on structbranch array = why so many entries?

// Then run MakeClass
// show the files
// root
// .L treename.C
// t.fChain->GetEntries()  // explain what a chain is
// t.h1_branch->Draw()
// t.h2_branch->Draw()

