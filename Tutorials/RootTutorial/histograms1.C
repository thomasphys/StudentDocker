// A simple set of macros using histograms

// Chris Jillings 2020-04-27

TH1D* h1 = NULL;
TH1D* h2 = NULL;

TH1D* h3 = NULL;

void makeH1() {
  h1 = new TH1D("h1name", "Histogram Title;x title;y title", 10, 0, 20);
  h1->Fill(12);
  h1->Draw();
}

void formatH1() {
  if( h1==NULL) return;
  
  h1->SetLineWidth(3);
  h1->SetLineColor(kMagenta);
}

void makeH2() {
  h2 = new TH1D("h2name", "A second Title;xx;yy", 100,0,10);
  h2->Fill(3);
  h2->Fill(5);
  h2->Fill(7);
  h2->Fill(99);
}
// Right click to look at hitogram formatting interactively.

// View toolbar and add hello alpha^{2}, mention TLatex class

void saveHistograms(const char* fname) {
  TFile* fout = new TFile(fname,"RECREATE");
  if( h1!=NULL) h1->Write();
  if( h2!=NULL) h2->Write();
  fout->Close();
}

// quit root
// restart root with root histograms1.root
// _file0->ls()
// h2->Draw()  - what happens?
// explain use of names to identify objects.


// A more complicated example with histograms


void histogramAndFit() {
  h3 = new TH1D("h3","A Gaussian Peak", 100, -10, 10);
  h3->FillRandom("gaus",5000);
  h3->Draw();
}

// explain log axes - the interactive way - the C++ way
// c1->SetLogy() c1->SetLogy(0)
// Right click a fit with fit panel.
