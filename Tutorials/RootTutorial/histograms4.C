/// This is the same as histograms3 except it is a 2-d histogram
///
/// Some notes about histograms
/// First - unlike numpy and pandas, looping through indices is easy and encouraged
/// Second - I have been known on occasion to replace (fixed length) arrays with
/// histograms because Histogram::Draw() is just so useful.
///
/// Chris Jillings 2020-05-05

{
  TH2F* h2 = new TH2F("h2","H2",3,0,3,4,10,18);
  h2->Fill(-10, 12);    // out of range in x
  h2->Fill(2,14); h2->Fill(2,14); h2->Fill(2,14);   // three fills at 3
  h2->Fill(1,16,4);   // one fill of weight 4 at 5
  h2->Fill(11,22);         // one overflow in both x and y
  Int_t nbinsx = h2->GetNbinsX();
  Int_t nbinsy = h2->GetNbinsY();
  int i, j;
  printf("i\tj\tcontent   \terror \n");
  for(i=0 ; i<=nbinsx+1 ; i++ ) {
    for( j=1 ; j<=nbinsy+1 ; j++ ) {

      printf("%d\t%d\t%f\t%f\n",i, j,
	     h2->GetBinContent(i, j),
	     h2->GetBinError(i, j));
    }
  }
    
}

// gStyle->SetOptStat(111111);
// h2->Draw();
// Also Setters

// show ProjectionX and ProjectionY
// https://root.cern.ch/doc/master/classTH2.html
