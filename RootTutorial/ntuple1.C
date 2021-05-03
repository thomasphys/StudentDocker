// An ntuple is a 2-d array of numbers, with columns being variables,
// and rows being "events" or "entries".
// Ntuples come as Float_t (32 bit floats) or Double_t (64 bit floats)
//
// Ntuples and trees are amazing
// An ntuple is similar to a python DataFrame, except
// C++ being a compiled library, looping is efficient
//
// Chris Jillings, 2020-05-02

TNtuple *nt = NULL;
TRandom3 *rgen = NULL;


void MakeNtuple() {
  rgen = new TRandom3(); // explain this  https://root.cern.ch/doc/master/classTRandom3.html
  nt = new TNtuple("ntname","NT","x:y:z:px:py:pz"); // explain this line
  int i;
  Float_t x,px,py,pz;
  Double_t y, z;
  for( i=0 ; i<1000 ; i++ ) {
    x  = rgen->Rndm();
    rgen->Circle(y, z, 40);          // pass by reference!    
    px = rgen->Exp(2.2e-6);      // anyone know what this number is?
    py = rgen->Gaus(5.0, 3.0);
    pz = rgen->Binomial(10624, 0.474);  // Any guesses where these numbers come from?
    nt->Fill(x,y,z,px,py,pz);
  }
  nt->SetMarkerStyle(7);
  nt->SetMarkerColor(kRed);
  nt->SetLineColor(kRed);
}

// nt->GetEntries()
// nt->Show(0)

// one dimenstional draw:
// nt->Draw("x")
// nt->Draw("x>>hx(20,0,1)")
// hx->Draw("PE")
// hhx = (TH1F*)gDirectory->Get("hx")
// hhx
// hx

// Two dim draw
// nt->Draw("z:y")
// Three dim draw
// nt->Draw("pz:py:px")

// nt->Draw("px>>hpx(40,0,20e-6)")
// hpx->Fit("expo")
// hpx->Fit("expo","L") -explain difference

// nt->Draw("px>>hpx(40,0,20e-6)")
// nt->SetLineColor(kBlue)
// nt->Draw("px","x<0.5","same")

// More complicated Draw statements...
// nt->Draw("TMath::Sqrt(y*y+z*z)")

// Let's define a cut
// TCut cutq1 = "y>0&&z>=0"
// nt->Draw("x")
// nt->Draw("x",cutq1)
// nt->Draw("x",cutq1&&"10")
// nt->Draw("x",cutq1*"10")




