/// More file i/o with TNamed objects
///
/// Chris Jillings - 2020-04-29

void MakeAndSaveHistograms() {
  TFile* f1 = new TFile("file1.root","RECREATE");
  TH1F* hptr1 = new TH1F("h1","H1", 10,0,10);
  hptr1->Fill(1);
  TH1F* hptr2 = new TH1F("h2","H2", 10,0,10);
  hptr2->Fill(2);


  TFile* f2 = new TFile("file2.root","RECREATE");
  TH1F* hptr3 = new TH1F("h1","H3", 10,0,10);
  hptr3->Fill(3);
  f1->cd();
  TH1F* hptr4 = new TH1F("h4","H4", 10,0,10);
  hptr4->Fill(4);
  f1->Write(); /// Note one write for all histograms created "under" f1
  f2->Write();
  f1->Close();
  f2->Close();
}

// read identically named histograms from 2 files
void ReadAndPlotHistograms() {
  TFile* fin1 = new TFile("file1.root"); // read-only by default
  TFile* fin2 = new TFile("file2.root"); // read-only by default
  TH1F* hptr1  = (TH1F*)fin1->Get("h1");
  TCanvas* c1 =  new TCanvas("c","c", 1);
  c1->Divide(2,2);
  c1->cd(1);
  hptr1->Draw();
  c1->cd(2);
  TH1F* hptr2  = (TH1F*)fin1->Get("h2");
  hptr2->Draw();
  c1->cd(3);
  // get h1 from file 2.
  TH1F* hptr3  = (TH1F*)fin2->Get("h1");
  hptr3->Draw();
  TH1F* hptr4  = (TH1F*)fin1->Get("h4");
  c1->cd(4);
  hptr4->Draw();
}
// explain why local pointers are a bad idea...
// How to get access to the canvas?

// save canvas to graphics file
// save canvas to a root file

