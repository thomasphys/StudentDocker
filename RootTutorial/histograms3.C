///
/// Some notes about histograms
/// First - unlike numpy and pandas, looping through indices is easy and encouraged
/// Second - I have been known on occasion to replace (fixed length) arrays with
/// histograms because Histogram::Draw() is just so useful.
///
/// Chris Jillings 2020-05-05

{
  TH1F* h1 = new TH1F("h1","H1",10,0,10);
  h1->Fill(-10);    // out of range
  h1->Fill(3); h1->Fill(3); h1->Fill(3);   // three fills at 3
  h1->Fill(5,4);   // one fill of weight 4 at 5
  h1->Fill(7); h1->Fill(7);   // two fills at 7
  h1->Fill(11);         // one overflow
  Int_t nbins = h1->GetNbinsX();
  int i;
  printf("i\tcontent   \terror    \tleft     \tcenter   \tright\n");
  for(i=0 ; i<=nbins+1 ; i++ ) {
    printf("%d\t%f\t%f\t%f\t%f\t%f\n",i,
	   h1->GetBinContent(i),
	   h1->GetBinError(i),
	   h1->GetXaxis()->GetBinLowEdge(i),
	   h1->GetXaxis()->GetBinCenter(i),
	   h1->GetXaxis()->GetBinUpEdge(i));
  }
    
}

// gStyle->SetOptStat(111111);
// h1->Draw();
// Also Setters
