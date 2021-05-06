/// Sometimes you need y = f(x; a) where x is n dimensional and
/// a is list of parameters.
///
/// Chris Jillings - 2020-04-29

TF1* f1a = NULL;
TF1* f1b = NULL;
TF1* f1c = NULL;
TF1* f1d = NULL;
TF2* f2 = NULL;

void Make1da() {
  f1a = new TF1("f1a", "sin(x)/x", 0, 10);
  f1a->Draw();
}
// show SetGridx SetGridy interactively. From that figure out command

void Make1db() {
  f1b = new TF1("f1b", "pol1(0)+gaus(2)",0,10);
  f1b->SetParameter(0, 2.0);  // b
  f1b->SetParameter(1, 1.0);  // m
  f1b->SetParameter(2,4);     // amplitude
  f1b->SetParameter(3, 4.0);  // mean
  f1b->SetParameter(4, 0.25); //sigma
  f1b->Draw();
}

/// Use functions from TMath
void Make1dc() {
  f1c = new TF1("f1b", "TMath::BetaDist(x,[0],[1])", 0, 1);
  f1c->SetParameter(0, 0.5);  // b
  f1c->SetParameter(1, 0.9);  // m
  f1c->Draw();
}


/// Sometimes you just need to define your own function
/// Explain Double_t, and arguments being pointers/arrays
Double_t myfunction(Double_t* x, Double_t* par) {
  Double_t xx = x[0];
  Double_t f = par[0] + par[1]*xx + par[2]*TMath::Gaus(xx,par[3],par[4],kTRUE);
  return f;
}

void SetupFunction() {
  // 2 parameters. Functin defined between 0 and 10
  f1d = new TF1("f1dname",myfunction, 0, 10, 5);
  f1d->SetParameters(1, 0.1, 20, 3, 1.2);   // Note plural on parameters
  f1d->SetParNames("b","slope","amp","mean","sigma");
  f1d->Draw();
}

TH1F* h;
void FitToTheGeneralFunction() {
  h = new TH1F("h","Test",100,0,10);
  h->FillRandom("f1dname", 20000);
  f1d->SetParameters(4,-1, 6,5,5); /// ie change them 
}


/// Show that the histogram makes a *copy* of the function.

// h->Fit(f1d)
// TFitResultPtr fitResult =  h->Fit(f1d,"LS")
// TMatrixDSym cov = fitResult->GetCovarianceMatrix()
// cov.Print()
