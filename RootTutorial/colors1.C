/// A bit about colors in root

// SetLineColor, SetMarkerColor etc...
// Click around refernce guide
// Show that histograms, Trees, Graphs etc derive from TAttMarker, TAttLine, etc...


TF2* f2 = NULL;

void MakeFunction() {
  f2 = new TF2("f2","1e6 * TMath::Exp(-(x-2)*(x-2)/4-(y-1)*(y-1))", -10,10, -10, 10);
  f2->Draw("cont");
    
}

// Rerun with gStyle->SetPalette(53)


